# qBraid QUEST notebooks

Hands-on quantum computing notebooks that run on real quantum hardware through qBraid.

These notebooks come with the QUEST program (Quantum University Education and Support Track), which gives university courses access to the qBraid platform, real quantum devices, and credits to run on them. Use any of them as they are, or copy, cut and adapt them to fit your syllabus.

Every notebook follows the same pattern: build a circuit, run it on an ideal simulator, run the same circuit on a real device, and compare the two. The gap between the ideal and the measured result is usually the lesson.

**New to quantum computing?** Start with the four notebooks in [foundations](foundations/).

## Notebooks

Notebooks are grouped by subject. The prefix gives the level: `intro`, `intermediate` or `advanced`.

**Foundations**

| Notebook | Level | Students |
|---|---|---|
| [Measuring readout error](foundations/intro_01_measuring_readout_error.ipynb) | Introductory | prepare known states and count how often the device reports the wrong bit |
| [Rotating a qubit](foundations/intro_02_rotating_a_qubit.ipynb) | Introductory | sweep a rotation angle and fit the measured curve |
| [Measuring in different bases](foundations/intro_03_measurement_bases.ipynb) | Introductory | measure three states in three bases |
| [Interference and phase](foundations/intro_04_interference_and_phase.ipynb) | Introductory | measure an interference fringe and its visibility |

**Algorithms**

| Notebook | Level | Students |
|---|---|---|
| [Deutsch-Jozsa and Bernstein-Vazirani](algorithms/intro_01_deutsch_jozsa_bernstein_vazirani.ipynb) | Introductory | answer a question about a hidden function with one query |
| [Grover's search on three qubits](algorithms/intro_02_grover_search_three_qubits.ipynb) | Introductory | find a marked item among 8 |
| [Phase estimation, on qBraid and IBM](algorithms/intro_03_phase_estimation_qbraid_and_ibm.ipynb) | Introductory | estimate a phase, optionally also on an IBM device |
| [Grover's search on real devices](algorithms/intermediate_01_grover_on_real_devices.ipynb) | Intermediate | see how each device's layout changes the circuit |
| [Phase estimation: precision against noise](algorithms/intermediate_02_phase_estimation_precision_vs_noise.ipynb) | Intermediate | trade precision against circuit size; try zero-noise extrapolation |

**Noise and hardware**

| Notebook | Level | Students |
|---|---|---|
| [Noise on real hardware](noise_and_hardware/intro_01_noise_on_real_hardware.ipynb) | Introductory | simulate three kinds of noise, then measure how a device degrades with depth |
| [Benchmarking a device](noise_and_hardware/advanced_01_device_benchmarking.ipynb) | Advanced | benchmark with mirror circuits, rank qubits, and measure what the choice is worth |
| [Improving on the compiler](noise_and_hardware/advanced_02_improving_the_compiler.ipynb) | Advanced | beat the default compilation and test whether it helps on hardware |

**Chemistry and physics**

| Notebook | Level | Students |
|---|---|---|
| [VQE for H₂](chemistry_and_physics/advanced_01_vqe_h2_ground_state.ipynb) | Advanced | go from a molecule to its ground-state energy |
| [Ising quench dynamics](chemistry_and_physics/advanced_02_ising_quench_dynamics.ipynb) | Advanced | simulate the time evolution of a spin chain |

**Machine learning and optimization**

| Notebook | Level | Students |
|---|---|---|
| [Variational classifier on Iris](machine_learning_and_optimization/intermediate_01_variational_classifier_iris.ipynb) | Intermediate | train a quantum classifier and compare it with a classical one |
| [QAOA for Max-Cut](machine_learning_and_optimization/advanced_01_qaoa_maxcut.ipynb) | Advanced | explore the landscape, warm starts and a classical comparison |

**Cryptography and security**

| Notebook | Level | Students |
|---|---|---|
| [BB84: noise or eavesdropper?](cryptography_and_security/intermediate_01_bb84_noise_vs_eavesdropper.ipynb) | Intermediate | measure how much of the key a device's own noise costs |
| [Shor's algorithm and factoring 15](cryptography_and_security/intermediate_02_shor_factoring_15.ipynb) | Intermediate | see what factoring 15 on hardware does and does not prove |

## Quick start

**On qBraid Lab:** open a notebook and run it from the top. Each notebook has a Settings or Setup cell where you choose the device and the number of shots, and it prints the device status and an estimated cost before submitting anything.

**Locally:**

```bash
git clone --recurse-submodules https://github.com/qBraid/qBraid-QUEST.git
cd qBraid-QUEST
pip install -r requirements/core.txt      # add requirements/chem.txt for the VQE notebook
```

Running on hardware from your own machine needs a qBraid API key.

## More information

- **[Notebook details](NOTEBOOK_DETAILS.md):** devices and prices, each notebook's qubits, gates, cost and results from our hardware tests, and advice on using the notebooks in a course.
- **[Resources](RESOURCES.md):** textbooks, courses and other external material, by topic.
- **[qBraid tutorial series](tutorials/):** longer tutorials on error mitigation, error correction, chemistry and more, included as submodules.

## Contributing

Corrections to physics, text, exercises or device settings are welcome as small pull requests. If you have course material to share with other instructors, please open an issue describing it first.

The QUEST notebooks are released for educational use. The tutorial series under `tutorials/` and `qbraid-lab-demo/` are separate repositories under their own licenses.
