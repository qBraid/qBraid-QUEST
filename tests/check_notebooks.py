"""Checks for the QUEST notebooks. No hardware, no credits, no API key needed.

  python tests/check_notebooks.py            # static checks, then run notebooks
  python tests/check_notebooks.py --static   # static checks only (seconds)
  python tests/check_notebooks.py algorithms # only notebooks whose path contains this

Static checks, every notebook:
  - valid notebook JSON, saved without outputs
  - metadata: qbraid.notebook_id, version, level, subjects
  - analytics tags: quest-<folder>-<notebook>-<milestone>, all four milestones present
  - every qBraid hardware submission passes tags=QUEST_JOB_TAGS
  - every code cell compiles (IPython magics are skipped)
  - relative links in the notebooks and the top-level Markdown files resolve
  - no stale internal references (old nbN numbering, "in this series", "Starter N")

Execution: each notebook runs top to bottom in a fresh namespace, stopping at its
first hardware cell. The introductory notebooks leave RUN_ON_HARDWARE = False, so
they run completely. Plots are discarded.
"""
import ast
import contextlib
import io
import json
import os
import pathlib
import re
import sys
import time
import traceback

ROOT = pathlib.Path(__file__).resolve().parents[1]
FOLDERS = ["foundations", "algorithms", "noise_and_hardware", "chemistry_and_physics",
           "machine_learning_and_optimization", "cryptography_and_security"]
MILESTONES = {"setup", "simulate", "hardware", "compare"}
TAG_RE = re.compile(r"^quest-([a-z0-9]+)-([a-z0-9]+)-([a-z]+)$")
# A cell that talks to qBraid hardware. The introductory notebooks guard theirs with
# RUN_ON_HARDWARE, so they are run; for the others, execution stops at the first one.
# Old internal names that readers cannot resolve. Refer to notebooks by name, with a link.
STALE_RE = re.compile(r"\bnb\d{1,2}\b|quest_nb\d|\bStarter \d|in this series|intermediate and advanced series"
                      r"|\b(Foundations|Algorithms|Chemistry( and| &) Physics|Cryptography|Systems)( and \w+)? series\b")
HW_MARKERS = ("device.run(", "devices[", "run_exactly(", ".submit(", "provider.get_device")


def notebooks(filter_text=None):
    out = []
    for folder in FOLDERS:
        for p in sorted((ROOT / folder).glob("*.ipynb")):
            if not filter_text or filter_text in str(p.relative_to(ROOT)):
                out.append(p)
    return out


def code_of(cell):
    return "".join(cell["source"])


def strip_magics(src):
    return "\n".join("" if line.lstrip().startswith(("%", "!")) else line for line in src.splitlines())


def static_checks(path):
    errors = []
    nb = json.loads(path.read_text())
    meta = nb.get("metadata", {}).get("qbraid", {})
    for key in ("notebook_id", "version", "level", "subjects"):
        if key not in meta:
            errors.append(f"metadata qbraid.{key} missing")
    ident = meta.get("notebook_id", "")

    seen = set()
    for i, c in enumerate(nb["cells"]):
        if not c.get("id"):
            errors.append(f"cell {i}: no cell id")
        for t in c.get("metadata", {}).get("tags", []):
            if not t.startswith("quest-"):
                continue
            m = TAG_RE.match(t)
            if not m or m.group(3) not in MILESTONES:
                errors.append(f"cell {i}: malformed tag {t!r}")
            elif f"quest-{m.group(1)}-{m.group(2)}" != ident:
                errors.append(f"cell {i}: tag {t!r} does not match notebook_id {ident!r}")
            else:
                seen.add(m.group(3))
        if c["cell_type"] != "code":
            continue
        if c.get("outputs") or c.get("execution_count"):
            errors.append(f"cell {i}: has outputs")
        src = code_of(c)
        try:
            ast.parse(strip_magics(src))
        except SyntaxError as e:
            errors.append(f"cell {i}: syntax error: {e.msg} (line {e.lineno})")
        n_calls = len(re.findall(r"\bdevice\.(run|submit)\(", src))
        if n_calls != src.count("tags=QUEST_JOB_TAGS"):
            errors.append(f"cell {i}: a hardware submission without tags=QUEST_JOB_TAGS")
    missing = MILESTONES - seen
    if missing:
        errors.append(f"milestone tags missing: {sorted(missing)}")
    if not any("QUEST_JOB_TAGS = " in code_of(c) for c in nb["cells"] if c["cell_type"] == "code"):
        errors.append("QUEST_JOB_TAGS is never defined")
    for i, c in enumerate(nb["cells"]):
        for m in STALE_RE.finditer(code_of(c) if c["cell_type"] == "markdown" else ""):
            errors.append(f"cell {i}: stale reference {m.group(0)!r}")
        if c["cell_type"] == "markdown":
            for link in re.findall(r"\]\(([^)#\s]+)\)", code_of(c)):
                if not link.startswith(("http", "mailto")) and not (path.parent / link).exists():
                    errors.append(f"cell {i}: broken link {link}")
    return errors


def doc_links():
    errors = []
    for name in ("README.md", "NOTEBOOK_DETAILS.md", "RESOURCES.md", "requirements/core.txt", "requirements/chem.txt"):
        p = ROOT / name
        if not p.exists():
            errors.append(f"{name} missing")
            continue
        for m in STALE_RE.finditer(p.read_text()):
            errors.append(f"{name}: stale reference {m.group(0)!r}")
        for link in re.findall(r"\]\(([^)#\s]+)\)", p.read_text()):
            if not link.startswith(("http", "mailto")) and not (ROOT / link).exists():
                errors.append(f"{name}: broken link {link}")
    return errors


def run_notebook(path):
    """Run cells in order until the first hardware cell. Returns (cells run, error or None)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.show = lambda *a, **k: None

    nb = json.loads(path.read_text())
    intro = any("RUN_ON_HARDWARE = False" in code_of(c) for c in nb["cells"] if c["cell_type"] == "code")
    ns = {"__name__": "__main__"}
    ran = 0
    cwd = os.getcwd()
    os.chdir(path.parent)
    try:
        for i, c in enumerate(nb["cells"]):
            if c["cell_type"] != "code":
                continue
            src = strip_magics(code_of(c))
            if not intro and any(m in src for m in HW_MARKERS):
                break
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    exec(compile(src, f"{path.name}:cell{i}", "exec"), ns)
            except Exception:
                return ran, f"cell {i}: " + traceback.format_exc(limit=3).strip().splitlines()[-1]
            finally:
                plt.close("all")
            ran += 1
    finally:
        os.chdir(cwd)
    return ran, None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    static_only = "--static" in sys.argv
    paths = notebooks(args[0] if args else None)
    failed = 0

    print(f"Static checks ({len(paths)} notebooks)")
    for p in paths:
        errs = static_checks(p)
        failed += bool(errs)
        print(f"  {'ok  ' if not errs else 'FAIL'} {p.relative_to(ROOT)}")
        for e in errs:
            print(f"         {e}")
    errs = doc_links()
    failed += bool(errs)
    print(f"  {'ok  ' if not errs else 'FAIL'} links and references in README.md, NOTEBOOK_DETAILS.md, RESOURCES.md, requirements")
    for e in errs:
        print(f"         {e}")

    if not static_only:
        print("\nExecution, up to the first hardware cell")
        for p in paths:
            t0 = time.time()
            ran, err = run_notebook(p)
            failed += bool(err)
            print(f"  {'ok  ' if not err else 'FAIL'} {p.relative_to(ROOT)}  ({ran} cells, {time.time() - t0:.0f} s)")
            if err:
                print(f"         {err}")

    print("\nPASS" if not failed else f"\nFAIL ({failed})")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
