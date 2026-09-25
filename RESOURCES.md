# Curated resources

Openly available material from across the field, organised by topic. Everything here is free
to access unless marked otherwise. The QUEST notebooks themselves are described in the
[README](README.md).

Each entry says what it is good for. The aim is a short list you can assign from. Where two
resources cover the same ground, we picked one and said why.

Levels: **Intro** (no prior quantum) · **Intermediate** (has seen circuits and linear
algebra) · **Advanced** (graduate) · **Reference** · **Tool**

---

## Start anywhere

Material that does not belong to one area, useful whatever you are teaching.

**Interactive courses**

- **[IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/)**: *Intro to Advanced.*
  The free course library that replaced the Qiskit Textbook when it was retired at the end
  of 2023. Start here rather than at the archived textbook pages, which still surface in
  search results. See the [full course catalog](https://quantum.cloud.ibm.com/learning/en/courses).
- **[PennyLane Codebook](https://pennylane.ai/codebook)**: *Intro to Intermediate.*
  Exercise-driven, runs entirely in the browser with nothing to install. The best option
  when students have no working Python environment and you do not want to spend a lab
  session creating one.
- **[Microsoft Quantum Katas](https://github.com/microsoft/QuantumKatas)**: *Intro to
  Intermediate.* Programming exercises with an automated test harness, so students get
  immediate feedback without you grading. Now integrated into
  [the QDK in VS Code](https://learn.microsoft.com/en-us/azure/quantum/katas-qdk-learning).
- **[IQM Academy](https://www.iqmacademy.com/)**: *Intro.* Free, interactive, and pitched
  deliberately low. Good for a first week, a non-majors course, or outreach.
- **[Q-CTRL Black Opal](https://q-ctrl.com/black-opal)**: *Intro.* Visual and gamified,
  built around building intuition before formalism. Strong for students who bounce off
  bra-ket notation on first contact. Free tier; institutional licensing for full access.

**Books and lecture notes**

- **[Wong, *Introduction to Classical and Quantum Computing*](https://www.thomaswong.net/introduction-to-classical-and-quantum-computing.pdf)**: *Intro.* Free PDF, and the most accessible rigorous option available: it assumes only
  trigonometry and builds the linear algebra it needs. Written for an actual undergraduate
  course taught since 2018.
- **[de Wolf, *Quantum Computing: Lecture Notes*](https://arxiv.org/abs/1907.09415)**: *Intermediate to Advanced.* The best free text for a theory-leaning course. Circuit model,
  the main algorithms, complexity, distributed settings and error correction, in roughly a
  semester.
- **[Preskill, Ph219/CS219 lecture notes](https://www.preskill.caltech.edu/ph219/)**: *Advanced.* The standard graduate reference for quantum information theory. Chapter 7 is
  still one of the best treatments of error correction anywhere.

**Frameworks worth showing beside Qiskit**

Concepts transfer between frameworks and syntax does not, so seeing a second one is worth a
lab session on its own.

- **[PennyLane](https://pennylane.ai/learn)**: differentiable programming as the organising
  idea. A genuinely different way to think about variational algorithms.
- **[Cirq](https://quantumai.google/cirq)**: Google's framework;
  [Introduction to Cirq](https://quantumai.google/cirq/start/intro) is the entry point.
- **[pytket](https://docs.quantinuum.com/tket/user-guide/)**: Quantinuum's compiler-first
  toolkit. Useful specifically because its compilation model differs from Qiskit's.
- **[Classiq](https://www.classiq.io/docs)**: synthesis from high-level functional models
  rather than hand-built gates. [Academic program](https://www.classiq.io/academia).
- **[NVIDIA CUDA-Q Academic](https://github.com/NVIDIA/cuda-q-academic)**: self-paced
  modules built for university courses, with
  [learning pathways](https://nvidia.github.io/cuda-q-academic/learningpath.html) mapped to
  course levels.

---

## 1. Foundations and Algorithms

**Courses**

- **[IBM · Basics of quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information)**: *Intro.* States, measurement, circuits, entanglement. The cleanest free treatment of the
  formalism, written by IBM's own team.
- **[IBM · Fundamentals of quantum algorithms](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms)**: *Intermediate.* Where quantum algorithms beat classical ones, including factoring and
  search. The natural companion to the [Grover notebook](algorithms/intermediate_01_grover_on_real_devices.ipynb) and the [phase estimation notebook](algorithms/intermediate_02_phase_estimation_precision_vs_noise.ipynb).
- **[PennyLane Codebook · Introduction to Quantum Computing](https://pennylane.ai/codebook/introduction-to-quantum-computing)**: *Intro.* Codercises rather than reading. See also the
  [Foundations learning path](https://pennylane.ai/codebook/learning-paths/foundations-of-quantum-computing).
- **[Qiskit Global Summer School lectures](https://www.youtube.com/playlist?list=PLOFEBzvs-Vvo5o97bYt8o1l8Ra1poMASQ)**: *Intermediate.* Recorded lecture series, free, by working researchers. Useful as
  supplementary lectures when you want a second voice on a hard topic.
- **[IonQ · Introduction to Quantum Programming](https://ionq.com/resources/anthology/lecture-series-introduction-to-quantum-programming)**: *Intro.* Four-part lecture series from IonQ scientists. Their
  [resource center](https://ionq.com/resources) also carries a hardware-focused series on
  how trapped ions actually compute.

**Beyond the standard algorithms**

- **[PennyLane · Intro to QSVT](https://pennylane.ai/demos/tutorial_intro_qsvt)**: *Intermediate to Advanced.* Quantum singular value transformation: the construction that
  puts Grover, amplitude amplification, Hamiltonian simulation and matrix inversion under a
  single framework. Increasingly the way modern algorithms are presented, and the natural
  step beyond the [Grover notebook](algorithms/intermediate_01_grover_on_real_devices.ipynb) and the [phase estimation notebook](algorithms/intermediate_02_phase_estimation_precision_vs_noise.ipynb). See also
  [how to implement QSVT on hardware](https://pennylane.ai/qml/demos/tutorial_qsvt_hardware).

**Reference**

- **[de Wolf, *Lecture Notes*](https://arxiv.org/abs/1907.09415)**: *Intermediate.* Chapters
  on Deutsch-Jozsa, Simon, Grover and Shor are assignable as-is.
- **[Preskill Ph219](https://www.preskill.caltech.edu/ph219/)**: *Advanced.*
- Nielsen & Chuang, *Quantum Computation and Quantum Information*: *Advanced.* Still the
  standard graduate text. Not free, but present in most university libraries.

---

## 2. Chemistry and Physics

**Tutorials**

- **[PennyLane · quantum chemistry demos](https://pennylane.ai/search/?contentType=DEMO&categories=quantum%20chemistry)**: *Intermediate.* The deepest free collection of quantum chemistry tutorials anywhere, and
  the differentiable approach contrasts usefully with the explicit-gradient treatment in the [VQE notebook](chemistry_and_physics/advanced_01_vqe_h2_ground_state.ipynb).
- **[QuTiP tutorials](https://qutip.org/qutip-tutorials/)**: *Intermediate to Advanced.*
  Open quantum systems, master equations and dynamics. Covers the dissipative side that the [Ising quench notebook](chemistry_and_physics/advanced_02_ising_quench_dynamics.ipynb)
  deliberately leaves out, and is the right tool when the question is physics rather than
  circuits.

- **[PennyLane · Intro to QSVT](https://pennylane.ai/demos/tutorial_intro_qsvt)**: *Advanced.* The modern route to Hamiltonian simulation and the successor to the
  Trotterisation the [Ising quench notebook](chemistry_and_physics/advanced_02_ising_quench_dynamics.ipynb) uses. Listed here for that application, but the framework is more
  fundamental than any one use of it, so it is cross-listed under Foundations as well.

**Papers worth assigning**

- **[McArdle et al., *Quantum computational chemistry*](https://arxiv.org/abs/1808.10402)**: *Advanced.* Rev. Mod. Phys. 92, 015003 (2020). The best single review bridging the two
  fields; assign sections rather than the whole thing.
- **[Cao et al., *Quantum Chemistry in the Age of Quantum Computing*](https://arxiv.org/abs/1812.09976)**: *Advanced.* Chem. Rev. 119, 10856 (2019). 194 pages and 404 references, so treat it as a
  reference work rather than a reading assignment.

**Tools**

- **[PySCF](https://pyscf.org/)**: *Tool.* The classical quantum chemistry package the [VQE notebook](chemistry_and_physics/advanced_01_vqe_h2_ground_state.ipynb) uses
  for its integrals. Worth an hour on its own, since students often meet the chemistry side
  for the first time here.
- **[OpenFermion](https://quantumai.google/openfermion)**: *Tool.* Fermion-to-qubit mappings
  and Hamiltonian manipulation.

---

## 3. Quantum Machine Learning

**Tutorials**

- **[PennyLane · Quantum Machine Learning](https://pennylane.ai/quantum-machine-learning)**: *Intermediate.* The reference collection for this area, and the
  [QML demo index](https://pennylane.ai/search/?contentType=DEMO&categories=quantum%20machine%20learning)
  covers far more ground than any course does.
- **[NVIDIA CUDA-Q Academic · QAOA for Max-Cut](https://github.com/NVIDIA/cuda-q-academic/tree/main/qaoa-for-max-cut)**: *Intermediate.* A complete pathway on exactly the problem the [QAOA notebook](machine_learning_and_optimization/advanced_01_qaoa_maxcut.ipynb) treats, from a different
  angle and in a different framework. The natural next step after the [QAOA notebook](machine_learning_and_optimization/advanced_01_qaoa_maxcut.ipynb).
- **[PennyLane · barren plateaus demo](https://pennylane.ai/demos/tutorial_barren_plateaus/)**: *Intermediate.* Hands-on version of the diagnostic the [variational classifier notebook](machine_learning_and_optimization/intermediate_01_variational_classifier_iris.ipynb) runs.

**Papers worth assigning**

- **[Cerezo et al., *Variational Quantum Algorithms*](https://arxiv.org/abs/2012.09265)**: *Intermediate to Advanced.* Nat. Rev. Phys. 3, 625 (2021). The orienting review for
  everything variational, covering the [VQE notebook](chemistry_and_physics/advanced_01_vqe_h2_ground_state.ipynb), the [variational classifier notebook](machine_learning_and_optimization/intermediate_01_variational_classifier_iris.ipynb) and the [QAOA notebook](machine_learning_and_optimization/advanced_01_qaoa_maxcut.ipynb) at once.
- **[McClean et al., *Barren plateaus in quantum neural network training landscapes*](https://arxiv.org/abs/1803.11173)**: *Intermediate.* Nat. Commun. 9, 4812 (2018). Short, and it reframes QML from "does it
  work" to "can it be trained at all". Pairs directly with the diagnostic in the [variational classifier notebook](machine_learning_and_optimization/intermediate_01_variational_classifier_iris.ipynb).
- **[Havlíček et al., *Supervised learning with quantum enhanced feature spaces*](https://arxiv.org/abs/1804.11326)**: *Intermediate.* Nature 567, 209 (2019). The origin of the variational classifier and
  quantum kernel methods the [variational classifier notebook](machine_learning_and_optimization/intermediate_01_variational_classifier_iris.ipynb) builds on.

---

## 4. Cryptography and Security

**Standards and timelines: the primary sources**

- **[NIST · Post-Quantum Cryptography](https://www.nist.gov/pqc)**: *Reference.* The
  authoritative starting point. FIPS 203 (ML-KEM), 204 (ML-DSA) and 205 (SLH-DSA) were
  published 13 August 2024;
  [HQC was selected as a backup KEM in March 2025](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption);
  FN-DSA is in draft as FIPS 206. See also the
  [standardization process history](https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization).
- **[NIST IR 8547 · Transition to Post-Quantum Cryptography Standards](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf)**: *Reference.* The actual migration timetable: RSA-2048 and ECC P-256 deprecated by 2030,
  disallowed after 2035. Assign this to any student who assumes the deadline is decades out.

**Resource estimates: why the deadline moves**

- **[Gidney & Ekerå (2019)](https://arxiv.org/abs/1905.09749)**: *Advanced.* 20 million
  noisy qubits and 8 hours for RSA-2048.
- **[Gidney (2025)](https://arxiv.org/abs/2505.15917)**: *Advanced.* Under 1 million qubits
  for the same problem, under identical hardware assumptions. Read as a pair, these two are
  the clearest available lesson in how algorithmic progress alone moves a security deadline.

**On reading factoring claims critically**

- **[Smolin, Smith & Vargo, *Oversimplifying quantum factoring*](https://arxiv.org/abs/1301.7007)**: *Intermediate.* Nature 499, 163 (2013). Two coherent qubits suffice to "factor" any
  product of two distinct odd primes if you already know the period. The [Shor notebook](cryptography_and_security/intermediate_02_shor_factoring_15.ipynb)
  reconstructs this argument in code.

**Tools**

- **[Open Quantum Safe / liboqs](https://openquantumsafe.org/)**: *Tool.* Working
  implementations of the standardised algorithms, plus prototype integrations into OpenSSL.
  Lets students run ML-KEM and measure it, rather than only reading the standard.
  [Source](https://github.com/open-quantum-safe/liboqs).

---

## 5. Systems, Hardware and Engineering

**Primary sources behind the [benchmarking notebook](noise_and_hardware/advanced_01_device_benchmarking.ipynb) and the [compiler notebook](noise_and_hardware/advanced_02_improving_the_compiler.ipynb)**

- **[Proctor et al., *Measuring the capabilities of quantum computers*](https://arxiv.org/abs/2008.11294)**: *Advanced.* Nat. Phys. 18, 75 (2022). The mirror-circuit method the [benchmarking notebook](noise_and_hardware/advanced_01_device_benchmarking.ipynb) implements, applied
  to twelve publicly available processors.
- **[Proctor et al., *Scalable randomized benchmarking using mirror circuits*](https://arxiv.org/abs/2112.09853)**: *Advanced.* Phys. Rev. Lett. 129, 150502 (2022). The follow-up that makes the method a
  benchmark rather than a demonstration.

**Compilation**

- **[Qiskit transpiler guide](https://quantum.cloud.ibm.com/docs/en/guides/transpile)**: *Reference.* Stage-by-stage documentation of the pipeline the [compiler notebook](noise_and_hardware/advanced_02_improving_the_compiler.ipynb) takes apart.
- **[pytket user guide](https://docs.quantinuum.com/tket/user-guide/)**: *Intermediate.* A
  second compiler with a different optimisation model. Compiling the same circuit through
  both is a good assignment: the differences are the lesson.

**Error mitigation**

- **[Mitiq](https://mitiq.readthedocs.io)**: *Tool.* Framework-agnostic reference
  implementation of zero-noise extrapolation, probabilistic error cancellation and readout
  mitigation. Pairs with the included Error Mitigation series.

**Hardware itself**

- **[IonQ documentation](https://docs.ionq.com/)** and their
  [technology overview](https://www.ionq.com/resources/overview-of-quantum-computing-technologies): *Intro to Intermediate.* Trapped-ion architecture from the people building it. Useful
  context for why all-to-all connectivity changes compilation.
- **[IBM · Quantum computing in practice](https://quantum.cloud.ibm.com/learning/en/courses/quantum-computing-in-practice)**: *Intermediate.* Working with 100+ qubit devices, which is the regime where the concerns
  in the [benchmarking notebook](noise_and_hardware/advanced_01_device_benchmarking.ipynb) and the [compiler notebook](noise_and_hardware/advanced_02_improving_the_compiler.ipynb) stop being optional.

---

## 6. Error Correction and Fault Tolerance

**Introductions**

- **[Roffe, *Quantum Error Correction: An Introductory Guide*](https://arxiv.org/abs/1907.11157)**: *Intermediate.* Contemp. Phys. 60, 226 (2019). The best modern entry point: stabilizer
  formalism from scratch, worked examples, and short enough to assign whole.
- **[Devitt, Munro & Nemoto, *Quantum Error Correction for Beginners*](https://arxiv.org/abs/0905.2794)**: *Intermediate.* Rep. Prog. Phys. 76, 076001 (2013). Older but still one of the clearest
  treatments of fault tolerance as distinct from correction.
- **[Preskill Ph219, Chapter 7](https://www.preskill.caltech.edu/ph219/)**: *Advanced.*
  The threshold theorem done properly.

**Where the field is now**

- **[Google Quantum AI, *Quantum error correction below the surface code threshold*](https://arxiv.org/abs/2408.13687)**: *Advanced.* Nature 638, 920 (2024). The first convincing demonstration that adding
  qubits makes a logical qubit better rather than worse: a distance-7 code suppressing error
  by Λ = 2.14 per two units of distance. This is the result that changed the field's
  timeline, and it is worth assigning even to students who cannot follow every detail.

**Reference**

- **[The Error Correction Zoo](https://errorcorrectionzoo.org)**: *Reference.* A searchable,
  cross-linked taxonomy of classical and quantum codes. The right answer to "what other
  codes are there", and a good source of student project topics.

**Tools**

- **[Stim](https://github.com/quantumlib/Stim)**: *Tool.* The standard fast stabilizer
  circuit simulator; makes distance-7 surface code experiments tractable on a laptop.
  Introduced in [arXiv:2103.02202](https://arxiv.org/abs/2103.02202).
- **[PyMatching](https://github.com/oscarhiggott/PyMatching)**: *Tool.* Minimum-weight
  perfect matching decoder, 100-1000x faster in version 2. Stim plus PyMatching is the
  standard pairing for a QEC course project.
- **[Sinter](https://github.com/quantumlib/Stim/tree/main/glue/sample)**: *Tool.* Parallel
  Monte Carlo sampling of QEC circuits built on Stim, with the plotting needed to produce
  threshold plots.

---

## Contributing to this list

Suggestions are welcome, especially from instructors who have taught with something and
found it worked. Open an issue with the link, the area, the level, and one sentence on what
it is good for. The one-sentence justification is the part that makes this list useful, so
entries without it are unlikely to be added.
