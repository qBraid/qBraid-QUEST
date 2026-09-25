# qBraid QUEST notebooks

Hands-on quantum computing notebooks that run on real quantum hardware through qBraid.

These notebooks come with the QUEST program (Quantum University Education and Support Track), which gives university courses access to the qBraid platform, real quantum devices, and credits to run on them. They are an optional resource for your existing course. Use any of them as they are, or copy, cut and adapt them to fit your syllabus.

Every notebook follows the same pattern: build a circuit, run it on an ideal simulator, run the same circuit on a real device, and compare the two. The gap between the ideal and the measured result is usually the lesson.

There are two sets:

- **Starter notebooks** (8): short, introductory, and designed to work well on today's hardware. Most use one hardware job.
- **Intermediate and advanced notebooks** (10): longer notebooks on algorithms, chemistry, machine learning, cryptography and systems, for upper-level and graduate courses.

A longer list of external material, organised by topic, is in [RESOURCES.md](RESOURCES.md).

---

## Quick start

**On qBraid Lab.** Open a notebook and run it from the top. Each notebook has a **Settings** cell (starters) or a **Setup** cell (intermediate and advanced) where you choose the device and the number of shots. Before any job is submitted, the notebook prints the device status and an estimated cost.

In the starter notebooks, nothing is sent to hardware until you set `RUN_ON_HARDWARE = True`. In the intermediate and advanced notebooks, hardware jobs are submitted when their hardware cells run.

**Locally.**

```bash
git clone --recurse-submodules https://github.com/qBraid/qBraid-QUEST.git
cd qBraid-QUEST
pip install -r requirements/core.txt
```

The VQE notebook (`quest_nb3`) also needs the chemistry packages:

```bash
pip install -r requirements/chem.txt
```

Running on hardware from your own machine needs a qBraid API key. Tested with qiskit 2.5.2, qiskit-aer 0.17.2 and qbraid 0.12.2.

---

## Devices and costs

Prices are in qBraid credits (100 credits = $1), as published on 25 September 2026. Device availability and prices change; each notebook checks the current status and price before submitting.

| Device | qBraid ID | Type | Qubits | Cost of one job | Notes |
|---|---|---|---|---|---|
| Rigetti Cepheus-1-108Q | `rigetti:rigetti:qpu:cepheus-1-108q` | Superconducting | 107 | Billed by execution time: 12,000 credits per minute of device time. Small jobs cost about 10 credits in our tests. | Cheapest option. In our tests it handled about 20 to 30 two-qubit gates in a general circuit before results became noise. |
| IQM Garnet | `aws:iqm:qpu:garnet` | Superconducting | 20 | 30 per job + 0.145 per shot: about 45 credits at 100 shots, 175 at 1,000 | Reliable and fast in our tests. |
| AQT IBEX Q1 | `aws:aqt:qpu:ibex-q1` | Trapped ion | 12 | 30 per job + 2.35 per shot: about 265 credits at 100 shots | Every qubit connects to every other. Runs in scheduled windows, so it is often unavailable. |
| IonQ Forte Enterprise 1 | `aws:ionq:qpu:forte-enterprise-1` | Trapped ion | 36 | 30 per job + 8 per shot: about 830 credits at 100 shots | Minimum of 100 shots per job. Best used as a single instructor demonstration. |
| IBM Quantum devices | through your own IBM account | Superconducting | 120 to 156 | Uses your IBM allocation, not qBraid credits | Starter 8 shows how to run on IBM from qBraid Lab. |

Simulators are free.

**Credits for your course** are held by your course's organization on qBraid. Transfer credits to each student's account before they run hardware jobs; until then, students see a balance of zero.

---

## Starter notebooks

Introductory notebooks, each designed to give a clear result on current hardware. Costs are for one run at the notebook's default settings.

| | Notebook | What students do | Default device | Qubits | Two-qubit gates | Cost of one run |
|---|---|---|---|---|---|---|
| 1 | [Does the machine lie? Measuring readout error](starter_01_readout_error.ipynb) | Prepare known states and count how often the device reports the wrong bit | Rigetti Cepheus | 8 | 0 | about 10 credits |
| 2 | [Rotating a qubit](starter_02_rotation_sweep.ipynb) | Sweep a rotation angle and fit the measured curve's contrast | IQM Garnet | 9 | 0 | about 103 credits |
| 3 | [Measuring in different bases](starter_03_measurement_bases.ipynb) | Measure three states in three bases; see why one measurement cannot reveal a whole state | IQM Garnet | 9 | 0 | about 103 credits |
| 4 | [Interference and the phase you cannot see](starter_04_interference.ipynb) | Measure a one-qubit interference fringe and its visibility | IQM Garnet | 12 | 0 | about 103 credits |
| 5 | [Noise on real hardware](starter_05_noise_on_hardware.ipynb) | Simulate readout error, gate error and decoherence, then match a device to one of them | Rigetti Cepheus | 4 | 6 to 48 | about 40 credits |
| 6 | [Deutsch-Jozsa and Bernstein-Vazirani](starter_06_deutsch_jozsa_bernstein_vazirani.ipynb) | Answer a question about a hidden function with one query | Rigetti Cepheus | 4 | 0 to 3 | about 30 credits |
| 7 | [Grover's search on three qubits](starter_07_grover_three_qubits.ipynb) | Find a marked item among 8, and see what happens with a second iteration | IQM Garnet | 3 | about 12 to 19 | about 103 credits |
| 8 | [Quantum phase estimation, on qBraid and on IBM](starter_08_phase_estimation_ibm.ipynb) | Estimate a phase on a qBraid device, and optionally on an IBM device with your own account | IQM Garnet | 4 | about 15 to 20 | about 103 credits |

Starters 1 to 4 run every experiment on separate qubits of one circuit, so each is a single hardware job. Starter 5 is adapted from the qBraid Error-Mitigation series.

---

## Intermediate and advanced notebooks

Longer notebooks for upper-level undergraduate and graduate courses. Each opens with a table giving its level, prerequisites, devices, cost and notes from our hardware tests. Sections marked *Optional, advanced* can be skipped.

| Notebook | Topic | Level | Default devices | Cost of one run | Notes from our tests |
|---|---|---|---|---|---|
| [nb1](intermediate_advanced/quest_nb1_grover_three_qpus.ipynb) | Grover's search on real devices, and how each device's layout changes the circuit | Intermediate | Rigetti, Garnet | about 210 credits on Garnet, plus Rigetti | The 4-qubit circuit was too long for Rigetti; Garnet gave a clear result. Starter 7 works on both. |
| [nb2](intermediate_advanced/quest_nb2_qpe_textbook_to_nisq.ipynb) | Quantum phase estimation: precision against noise; zero-noise extrapolation | Intermediate to advanced | Rigetti | about 70 credits | Hardware error 0.02 to 0.06, far above the simulator. The zero-noise extrapolation step gave near-random results on Rigetti. |
| [nb3](intermediate_advanced/quest_nb3_vqe_h2_full_pipeline.ipynb) | VQE for H₂, from the molecule to the ground-state energy | Advanced | Garnet | about 890 credits | Needs the chemistry packages. |
| [nb4](intermediate_advanced/quest_nb4_tfim_quench_dynamics.ipynb) | Quench dynamics of the transverse-field Ising model | Advanced | Garnet | about 820 credits | Hardware followed the exact result closely at early times. |
| [nb5](intermediate_advanced/quest_nb5_vqc_iris.ipynb) | A variational classifier on the Iris dataset, against a classical baseline | Intermediate to advanced | Garnet | about 1,790 credits; lower the shots or test samples to reduce this | Garnet classified 7 of 10 samples correctly; Rigetti was at chance. |
| [nb6](intermediate_advanced/quest_nb6_qaoa_maxcut.ipynb) | QAOA for Max-Cut: landscape, warm starts, classical comparison | Advanced | Garnet | about 320 credits | Above the random baseline on Garnet; at or below it on Rigetti. |
| [nb7](intermediate_advanced/quest_nb7_bb84_qber_vs_eve.ipynb) | BB84: telling device noise apart from an eavesdropper | Intermediate | Rigetti, Garnet | about 1,050 credits on Garnet, plus Rigetti | Error rate 5% to 11% on Rigetti, rising with channel length at first; below 2% on Garnet. |
| [nb8](intermediate_advanced/quest_nb8_shor_rsa_reality.ipynb) | Shor's algorithm, RSA, and what factoring 15 proves | Intermediate to advanced | Rigetti, Garnet | about 350 credits on Garnet, plus Rigetti | The compiled circuit beat random guessing on both devices (0.48 and 0.98 against 0.25); the full circuit did not. |
| [nb9](intermediate_advanced/quest_nb9_device_benchmarking.ipynb) | Benchmarking a device with mirror circuits, and choosing its best qubits | Advanced | Rigetti, Garnet | about 820 credits on Garnet, plus Rigetti | On Rigetti the best four qubits gave a key error rate of 0.07 and the worst four 0.24. On Garnet all qubits scored alike. |
| [nb10](intermediate_advanced/quest_nb10_compilation_measured.ipynb) | Improving on the default compiler, and measuring whether it helps | Advanced | Rigetti, Garnet | about 640 credits on Garnet, plus Rigetti | The reordered circuit scored slightly better on Rigetti and the same on Garnet. |

Rigetti runs are billed by execution time and cost about 10 credits per job in our tests. The notebooks that compare devices can include AQT's trapped-ion device by uncommenting one line; it runs in scheduled windows and costs more per shot.

---

## Using these notebooks in your course

- **Adapt freely.** Delete sections, change parameters, or lift the "Questions to try" into an assignment. Grading stays in your own course system; each starter suggests what students could hand in.
- **Check the cost for your class size before assigning.** A starter at about 100 credits per run costs about 3,000 credits for a class of 30. Lower `SHOTS` to reduce the cost on devices billed per shot.
- **Queues vary.** A small job can return in seconds or wait more than an hour. For in-class use, submit before the session.
- **Devices change.** If a device is offline, pick another in the Settings or Setup cell. AQT runs in scheduled windows.
- **Notebooks are distributed without outputs,** so students open a clean copy.

---

## Related qBraid tutorial series

These series are included in this repository as submodules under `tutorials/`.

| Series | What it covers |
|---|---|
| [Error-Mitigation](tutorials/Error-Mitigation) | Four notebooks: types of noise, readout mitigation, zero-noise extrapolation, and the full set on real hardware. Starter 5 is adapted from its first notebook. |
| [Clifford Noise Reduction](tutorials/Clifford-Noise-Reduction) | CliNR, a method between error mitigation and full error correction, run on trapped-ion hardware. |
| [Shor-Style Syndrome Extraction](tutorials/Shor-Style-Syndrome-Extraction) | Fault-tolerant syndrome extraction for the Steane code, from first principles. |
| [Generalized Superfast Encoding](tutorials/Generalized-Superfast-Encoding) | A fermion-to-qubit mapping that also works as an error-detecting code. |
| [Q-Cliff](tutorials/Q-Cliff) | Building Clifford-based ansätze, with worked VQE examples for LiH and H₄. |
| [Quantum Reservoir Computing](tutorials/Quantum-Reservoir-Computing) | Hybrid classical and quantum reservoirs for time-series prediction. |
| [IEEE QCE23 tutorial](tutorials/IEEE_QCE23_qBraid_Tutorial) | A two-session workshop with exercises and worked solutions. |
| [IEEE QCE25 tutorial](tutorials/IEEE_QCE25_QC_on_QC_Tutorial) | Quantum chemistry on quantum computers: fermion-to-qubit mappings and VQE. |
| [qBraid Lab demos](qbraid-lab-demo) | Using the platform: job submission, devices, and other SDKs through one interface. |

For external material, from textbooks to other frameworks, see [RESOURCES.md](RESOURCES.md).

---

## Repository layout

```
qBraid-QUEST/
├── README.md                  this file
├── RESOURCES.md               curated external material, by topic
├── starter_01 ... starter_08  the eight starter notebooks
├── intermediate_advanced/     the ten intermediate and advanced notebooks
├── requirements/              packages for all notebooks, plus the chemistry packages for nb3
├── tutorials/                 qBraid tutorial series (submodules)
└── qbraid-lab-demo/           platform demonstrations (submodule)
```

Each notebook carries a stable `notebook_id` and `version` in its metadata, so you can cite a specific version in a syllabus.

---

## Contributing

Corrections to physics, text, exercises or device settings are welcome as small pull requests.

If you have course material you would like to share with other instructors, such as notebooks, problem sets, labs or syllabi, please open an issue describing it first, so we can agree where it fits.

---

## Attribution

The QUEST notebooks are released for educational use. The tutorial series under `tutorials/` and `qbraid-lab-demo/` are separate repositories under their own licenses; check each before redistributing. External material listed in RESOURCES.md belongs to its authors.
