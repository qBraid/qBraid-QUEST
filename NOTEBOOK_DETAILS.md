# Notebook details

Details for planning a course with the QUEST notebooks: devices and prices, what each notebook needs, what our hardware tests showed, and practical advice. For the list of notebooks, see the [README](README.md).

## Devices and costs

Prices are in qBraid credits (100 credits = $1), as published on 25 September 2026. Device availability and prices change; each notebook checks the current status and price before submitting.

| Device | qBraid ID | Type | Qubits | Cost of one job | Notes |
|---|---|---|---|---|---|
| Rigetti Cepheus-1-108Q | `rigetti:rigetti:qpu:cepheus-1-108q` | Superconducting | 107 | Billed by execution time: 12,000 credits per minute of device time. Small jobs cost about 10 credits in our tests. | Cheapest option. In our tests it handled about 20 to 30 two-qubit gates in a general circuit before results became noise. Queues range from seconds to over an hour. |
| IQM Garnet | `aws:iqm:qpu:garnet` | Superconducting | 20 | 30 per job + 0.145 per shot: about 45 credits at 100 shots, 175 at 1,000 | Fast and reliable in our tests. Accepts *verbatim* programs that run exactly as written (see below). |
| AQT IBEX Q1 | `aws:aqt:qpu:ibex-q1` | Trapped ion | 12 | 30 per job + 2.35 per shot: about 265 credits at 100 shots | Every qubit connects to every other. Runs in scheduled windows, so it is often unavailable. |
| IonQ Forte Enterprise 1 | `aws:ionq:qpu:forte-enterprise-1` | Trapped ion | 36 | 30 per job + 8 per shot: about 830 credits at 100 shots | Minimum of 100 shots per job. Best used as a single instructor demonstration. |
| IBM Quantum devices | through your own IBM account | Superconducting | 120 to 156 | Uses your IBM allocation, not qBraid credits | The phase estimation notebook shows how to run on IBM from qBraid Lab. |

Simulators are free.

**Credits for your course** are held by your course's organization on qBraid. Transfer credits to each student's account before they run hardware jobs; until then, students see a balance of zero.

### Device compilers can change your circuit

Before a device runs a circuit, its compiler rewrites it into the device's native gates. It also removes gates that have no overall effect. That is usually helpful, but it removes experiments built from gates that cancel, such as a circuit followed by its inverse, even when the circuit contains barriers. In our tests both Rigetti Cepheus and IQM Garnet did this.

Three notebooks depend on circuits like these (noise and hardware, and the BB84 notebook). On IQM Garnet they submit a *verbatim* program, which the device runs gate for gate on physical qubits the notebook names. Rigetti has no such mode through qBraid, so those notebooks either skip Rigetti or run only the parts the compiler leaves intact. Every notebook that does this prints, after each job, how many gates it sent and how many the device ran.

## Notebook details

Costs are for one run at the notebook's default settings. "Test results" are from our own runs; hardware changes, so treat them as a guide.

### Foundations

| Notebook | Default device | Qubits | Two-qubit gates | Hardware jobs | Cost of one run | Test results |
|---|---|---|---|---|---|---|
| [Measuring readout error](foundations/intro_01_measuring_readout_error.ipynb) | Rigetti Cepheus | 8 | 0 | 1 | about 10 credits | Per-qubit readout error 1% to 13% on Rigetti; 1% to 3% on Garnet. |
| [Rotating a qubit](foundations/intro_02_rotating_a_qubit.ipynb) | IQM Garnet | 9 | 0 | 1 | about 103 credits | Clear sinusoidal curves on both devices. |
| [Measuring in different bases](foundations/intro_03_measurement_bases.ipynb) | IQM Garnet | 9 | 0 | 1 | about 103 credits | Expected results on both devices. |
| [Interference and phase](foundations/intro_04_interference_and_phase.ipynb) | IQM Garnet | 12 | 0 | 1 | about 103 credits | Visibility 0.92 on Garnet, 0.96 on Rigetti. |

These four run every experiment on separate qubits of one circuit, so each is a single hardware job.

### Algorithms

| Notebook | Default device | Qubits | Two-qubit gates | Hardware jobs | Cost of one run | Test results |
|---|---|---|---|---|---|---|
| [Deutsch-Jozsa and Bernstein-Vazirani](algorithms/intro_01_deutsch_jozsa_bernstein_vazirani.ipynb) | Rigetti Cepheus | 4 | 0 to 3 | 3 | about 30 credits | Correct answers on Rigetti, with the balanced function the noisiest. |
| [Grover's search on three qubits](algorithms/intro_02_grover_search_three_qubits.ipynb) | IQM Garnet | 3 | about 12 to 19 | 1 | about 103 credits | Marked item clearly found on both devices. |
| [Phase estimation, on qBraid and IBM](algorithms/intro_03_phase_estimation_qbraid_and_ibm.ipynb) | IQM Garnet | 4 | about 15 to 20 | 1 | about 103 credits | Correct phase as the most likely result on both devices. |
| [Grover's search on real devices](algorithms/intermediate_01_grover_on_real_devices.ipynb) | Rigetti, Garnet | 4 | 14 before compiling; up to 300 after | 4 per device | about 210 credits on Garnet, plus Rigetti | Garnet gave a clear result. On Rigetti the 4-qubit circuit was too long and gave random output; the three-qubit notebook works on both. |
| [Phase estimation: precision against noise](algorithms/intermediate_02_phase_estimation_precision_vs_noise.ipynb) | Rigetti | 2 to 5 | 4 to 36 before compiling | 7 | about 70 credits | Correct up to 3 or 4 counting qubits on Rigetti, random beyond. Zero-noise extrapolation had nothing to extrapolate at those sizes. |

### Noise and hardware

| Notebook | Default device | Qubits | Two-qubit gates | Hardware jobs | Cost of one run | Test results |
|---|---|---|---|---|---|---|
| [Noise on real hardware](noise_and_hardware/intro_01_noise_on_real_hardware.ipynb) | Rigetti Cepheus | 4 | 3 to 24 | 4 | about 40 credits on Rigetti; about 410 on Garnet at 1,000 shots | Every gate ran as sent. Rigetti: score 0.62 at 1 layer, near 0 (random) from 4 layers. Garnet: 0.94 at 1 layer, 0.45 at 16. A mirror-circuit version of this experiment was removed by both devices' compilers, which is why the notebook uses random layers on hardware. |
| [Benchmarking a device](noise_and_hardware/advanced_01_device_benchmarking.ipynb) | IQM Garnet, verbatim | 4 to 8 | 4 to 32 | 16 | about 2,200 credits | Survival 0.82 at 4 two-qubit gates, 0.74 at 16. Ranking separated the qubits (0.98 against 0.79). BB84 on the best and worst four: QBER 1.0% and 1.75%, both far below the 11% threshold. Without verbatim programs, both devices' compilers removed the mirror circuits. |
| [Improving on the compiler](noise_and_hardware/advanced_02_improving_the_compiler.ipynb) | Rigetti, Garnet | 8 | 44 to 56 | 2 per device | about 640 credits on Garnet, plus Rigetti | Garnet (our compilations run verbatim, 56 and 44 two-qubit gates): 53% and 66% of the ideal advantage kept. Rigetti: recompiled to over 100 two-qubit gates; both at random guessing. |

The noise notebook is adapted from the qBraid [Error-Mitigation series](tutorials/Error-Mitigation).

### Chemistry and physics

| Notebook | Default device | Qubits | Two-qubit gates | Hardware jobs | Cost of one run | Test results |
|---|---|---|---|---|---|---|
| [VQE for H₂](chemistry_and_physics/advanced_01_vqe_h2_ground_state.ipynb) | IQM Garnet | 4 | 6 | 5 | about 890 credits | Needs `requirements/chem.txt`. Energy within the expected range on Garnet. |
| [Ising quench dynamics](chemistry_and_physics/advanced_02_ising_quench_dynamics.ipynb) | IQM Garnet | 4 | 24 | 8 | about 820 credits | Hardware followed the exact result closely at early times on Garnet; on Rigetti the output was indistinguishable from random. |

### Machine learning and optimization

| Notebook | Default device | Qubits | Two-qubit gates | Hardware jobs | Cost of one run | Test results |
|---|---|---|---|---|---|---|
| [Variational classifier on Iris](machine_learning_and_optimization/intermediate_01_variational_classifier_iris.ipynb) | IQM Garnet | 4 | 6 | 10 | about 1,790 credits; lower the shots or test samples to reduce this | Garnet classified 7 of 10 samples correctly; Rigetti was near chance. |
| [QAOA for Max-Cut](machine_learning_and_optimization/advanced_01_qaoa_maxcut.ipynb) | IQM Garnet | 8 | 36 before compiling | 1 | about 320 credits | Above the random baseline on Garnet; at the random baseline on Rigetti. |

### Cryptography and security

| Notebook | Default device | Qubits | Two-qubit gates | Hardware jobs | Cost of one run | Test results |
|---|---|---|---|---|---|---|
| [BB84: noise or eavesdropper?](cryptography_and_security/intermediate_01_bb84_noise_vs_eavesdropper.ipynb) | Garnet (verbatim), Rigetti | 4 | 0 | 6 on Garnet, 1 on Rigetti | about 1,050 credits on Garnet, plus about 10 on Rigetti | Garnet (verbatim): QBER 1.75% with no channel, 2.0% with a 128-gate channel. Rigetti, no channel: 6.75%. |
| [Shor's algorithm and factoring 15](cryptography_and_security/intermediate_02_shor_factoring_15.ipynb) | Rigetti, Garnet | 3 to 5 | 10 (compiled) to 77 (full) | 2 per device | about 350 credits on Garnet, plus Rigetti | The compiled circuit beat random guessing on both devices; the full circuit did not, which is the notebook's point. |

## Using the notebooks in a course

- **Adapt freely.** Delete sections, change parameters, or lift the "Questions to try" into an assignment. Grading stays in your own course system; each introductory notebook suggests what students could hand in.
- **Check the cost for your class size before assigning.** A notebook at about 100 credits per run costs about 3,000 credits for a class of 30. Lower the shots to reduce the cost on devices billed per shot.
- **Queues vary.** A small job can return in seconds or wait more than an hour. For in-class use, submit before the session.
- **Devices change.** If a device is offline, pick another in the Settings or Setup cell.
- **Notebooks are distributed without outputs,** so students open a clean copy.
- **Cite a version.** Each notebook carries a stable `notebook_id` and `version` in its metadata.

## Related qBraid tutorial series

Included in this repository as submodules under `tutorials/`.

| Series | What it covers |
|---|---|
| [Error-Mitigation](tutorials/Error-Mitigation) | Types of noise, readout mitigation, zero-noise extrapolation, and the full set on real hardware. |
| [Clifford Noise Reduction](tutorials/Clifford-Noise-Reduction) | CliNR, a method between error mitigation and full error correction, run on trapped-ion hardware. |
| [Shor-Style Syndrome Extraction](tutorials/Shor-Style-Syndrome-Extraction) | Fault-tolerant syndrome extraction for the Steane code, from first principles. |
| [Generalized Superfast Encoding](tutorials/Generalized-Superfast-Encoding) | A fermion-to-qubit mapping that also works as an error-detecting code. |
| [Q-Cliff](tutorials/Q-Cliff) | Building Clifford-based ansätze, with worked VQE examples for LiH and H₄. |
| [Quantum Reservoir Computing](tutorials/Quantum-Reservoir-Computing) | Hybrid classical and quantum reservoirs for time-series prediction. |
| [IEEE QCE23 tutorial](tutorials/IEEE_QCE23_qBraid_Tutorial) | A two-session workshop with exercises and worked solutions. |
| [IEEE QCE25 tutorial](tutorials/IEEE_QCE25_QC_on_QC_Tutorial) | Quantum chemistry on quantum computers: fermion-to-qubit mappings and VQE. |
| [qBraid Lab demos](qbraid-lab-demo) | Using the platform: job submission, devices, and other SDKs through one interface. |

## Repository layout

```
qBraid-QUEST/
├── README.md
├── NOTEBOOK_DETAILS.md                  this file
├── RESOURCES.md                         external material, by topic
├── foundations/
├── algorithms/
├── noise_and_hardware/
├── chemistry_and_physics/
├── machine_learning_and_optimization/
├── cryptography_and_security/
├── requirements/                        core.txt for all notebooks; chem.txt for the VQE notebook
├── tutorials/                           qBraid tutorial series (submodules)
└── qbraid-lab-demo/                     platform demonstrations (submodule)
```

Tested with qiskit 2.5.2, qiskit-aer 0.17.2 and qbraid 0.12.2 and 0.13.
