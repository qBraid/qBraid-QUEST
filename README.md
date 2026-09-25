# qBraid QUEST notebooks

[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/qBraid/qBraid-QUEST.git)

Hands-on quantum computing notebooks that run on real quantum hardware through qBraid.

These notebooks come with [QUEST](https://quest.qbraid.com) (Quantum University Education & Support Track), a qBraid program that gives university courses access to the qBraid platform, real quantum devices, and credits to run on them. Use any of them as they are, or copy, cut and adapt them to fit your syllabus.

To apply to QUEST for the Spring term, please see [quest.qbraid.com](https://quest.qbraid.com/#apply).

## What is here

18 Jupyter notebooks in six subject areas: foundations, algorithms, noise and hardware, chemistry and physics, machine learning and optimization, and cryptography and security. They range from introductory notebooks for a first course in quantum computing to advanced notebooks for graduate courses.

Every notebook follows the same pattern: build a circuit, run it on an ideal simulator, run the same circuit on a real quantum device, and compare the two. The gap between the ideal and the measured result is usually the lesson. Each notebook states its level, prerequisites, devices and cost at the top. The introductory notebooks end with questions for students; the others end with ideas for going further.

New to quantum computing? Start with the four notebooks in [foundations](foundations/).

## Repository layout

```
qBraid-QUEST/
├── README.md
├── NOTEBOOK_DETAILS.md                  every notebook: level, device, cost, test results
├── RESOURCES.md                         textbooks, courses and other external material
├── foundations/                         measurement, rotations, bases, interference
├── algorithms/                          Deutsch-Jozsa, Bernstein-Vazirani, Grover, phase estimation
├── noise_and_hardware/                  noise, benchmarking, compilation
├── chemistry_and_physics/               VQE for H2, Ising model dynamics
├── machine_learning_and_optimization/   variational classifier, QAOA
├── cryptography_and_security/           BB84, Shor's algorithm
├── requirements/                        core.txt for all notebooks; chem.txt for the VQE notebook
├── tests/                               checks that run without hardware or credits
├── tutorials/                           longer qBraid tutorial series (submodules)
└── qbraid-lab-demo/                     qBraid platform demonstrations (submodule)
```

Each notebook's file name gives its level (`intro`, `intermediate` or `advanced`) and topic.

## Where to find more

- **[Notebook details](NOTEBOOK_DETAILS.md):** the full list of notebooks with their devices, qubits, costs and results from our hardware tests; device prices; and advice on using the notebooks in a course.
- **[Resources](RESOURCES.md):** textbooks, courses and other external material, by topic.
- **[qBraid tutorial series](tutorials/):** longer tutorials on error mitigation, error correction, chemistry and more.

## Quick start

**On qBraid Lab:** open a notebook and run it from the top. Each notebook has a Settings or Setup cell where you choose the device and the number of shots, and it prints the device status and an estimated cost before submitting anything.

**Locally:**

```bash
git clone --recurse-submodules https://github.com/qBraid/qBraid-QUEST.git
cd qBraid-QUEST
pip install -r requirements/core.txt      # add requirements/chem.txt for the VQE notebook
```

Running on hardware from your own machine needs a qBraid API key.

## Contributing

**Found a mistake in the code or text, or a notebook that no longer runs?** Please open an issue with the notebook, the device, and what happened.

**Have course material to share?** We would like this collection to grow with material from the instructors who use it. If you teach with QUEST, contact the QUEST team through [quest.qbraid.com](https://quest.qbraid.com) and we will help you add it. Otherwise, open an issue to get in touch.

## License

The QUEST notebooks are released for educational use. The tutorial series under `tutorials/` and `qbraid-lab-demo/` are separate repositories under their own licenses.
