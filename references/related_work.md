# Related work and scope of the contribution

Closed oscillator trajectories, geometric entangling phases, and spectral pulse optimization are established tools. The result developed in this repository concerns a more specific question: the force action and duration required for a layer of $`K`$ independent maximally entangling pairs through $`m`$ harmonic modes, when every physically equivalent phase representative is allowed and the whole layer may have a fixed worst-case error.

The [model](../science/model.md) assumes commuting linear conditional forces and exact bus closure. It allows final local $`Z`$ corrections and global phase; it does not optimize over arbitrary local basis changes during the interaction. For the closed-system unitary core and every fixed half-diamond layer error $`\epsilon<1/\sqrt2`$, the [gate-layer bounds](../science/gate_layer_bounds.md) establish the finite-mode converse. The [construction](../science/matching_construction.md) supplies the matching scaling order. The distinction between a lower bound in an independently controlled relaxation and implementability on a specific device is developed in [hardware resources](../science/hardware_resources.md). A separately specified [vacuum-loss extension](../science/loss_and_frontier.md) derives the emitted-field channel and optimizes paid drive against displacement exposure for a fixed full phase matrix.

Bibliographic entries, including publication metadata and versioned preprints, are collected in [references.bib](references.bib). Section and equation pointers below identify the actual primary version used; preprint and journal numbering can differ.

## 1. Geometric optimal control is an antecedent

**Wong and Baillieul (2012), Theorem 5.1 and Corollary 5.1, Eqs. (5.1)–(5.2).** The primary [arXiv:1201.6527v2 PDF](https://arxiv.org/pdf/1201.6527v2), printed p. 17, minimizes quadratic effort for prescribed outputs of a bounded bilinear map. For the closed Brockett–Heisenberg system, the corollary yields harmonic weights $`\lceil j/2\rceil`$. Its cost averages over independently selected control families. The [author-institution publication record](https://research.cuhk.edu.hk/en/publications/control-communication-complexity-of-distributed-actions-2/) confirms *IEEE Transactions on Automatic Control* 57(11), 2731–2745 (2012), DOI [10.1109/TAC.2012.2192357](https://doi.org/10.1109/TAC.2012.2192357). Key: `WongBaillieul2012`.

Fourier multiplicity and weighted singular-value allocation are direct antecedents. The project's signed real symmetric phase matrix, its $`2m`$ real directions per signed harmonic, and its summed per-qubit force normalization require the explicit translation in the [spectral proof](../science/spectral_cost.md). The spectral principle is inherited; the quantum phase-equivalence quotient is an additional problem.

**Brockett (1982), Theorem 2.** The chapter [“Control Theory and Singular Riemannian Geometry”](https://doi.org/10.1007/978-1-4612-5651-9_2), pp. 11–27, treats the corresponding step-two control geometry and a vertical-distance spectral formula. An [author-hosted reprint](https://hrl.harvard.edu/publications/brockett81control.pdf) is available. Its normalization must be checked rather than transferred by inspection. BibTeX key: `Brockett1982`.

**Rizzi and Serres (2017), Appendix A, Proposition 15, Eq. (48), with proof Eqs. (49)–(51).** [arXiv:1610.01596v2](https://arxiv.org/html/1610.01596v2) gives the vertical-distance formula for a skew-symmetric area matrix $`Y`$ with nonzero eigenvalue magnitudes $`0<\alpha_1\le\cdots\le\alpha_r`$:

```math
d((0,0),(0,Y))^2=4\pi\sum_{j=1}^r(r-j+1)\alpha_j.
```

The integer weights come from distinct closed-loop harmonics. This is a direct mathematical antecedent of weighted spectral area costs. The author's [research page](https://sites.google.com/view/rizziluca/research) links an [erratum](https://drive.google.com/file/d/1uSMry_CAEsKCGpL39tgO8ND7TX48HHLG/view): it corrects Proposition 4's codimension and restores missing $`J_2`$ blocks in Eq. (50), without changing Proposition 15 or Eq. (48). BibTeX keys: `RizziSerres2017`, `RizziSerresErrata`.

The repository's real symmetric phase matrix is a projection of the underlying skew-area data, with multiplicities set by the number of bus modes. The [spectral proof](../science/spectral_cost.md) establishes that projection and its normalization directly. The weighted-harmonic mechanism is not claimed as new geometry. Also, a theorem for a prescribed full matrix $`A`$ does not by itself solve the physical gate problem: diagonal entries of $`A`$ are unobservable, and many different off-diagonal logarithms can represent the same gate up to local phases.

## 2. Hardware-aware optimal pulses and parallel ion gates

### Blümel et al.: optimality for a selected pair

**“Power-optimal, stabilized entangling gate between trapped-ion qubits,” npj Quantum Information 7, 147 (2021).** [Primary preprint v2](https://arxiv.org/html/1905.09292v2): Section I, “Power-optimal two-qubit entangling gate”; supplement S5, “Analytical lower bound of required peak pulse power”; S6, “Power and execution time scaling”; S7, “Power optimality requires identical pulses”; S13, “Efficient arbitrary simultaneously entangling gates.” [Published DOI](https://doi.org/10.1038/s41534-021-00489-w). Key: `Bluemel2021`.

The closure nullspace and the phase quadratic form yield a power-optimal pulse for a selected pair; the supplement also studies power and time bounds and an EASE extension. This supplies a close spectral-control antecedent. Its selected-pair and hardware-specific optimization is a different statement from a universal matching-layer converse over arbitrary phase representatives and fixed whole-layer error.

### EASE: arbitrary simultaneous interactions are established

**Grzesiak et al., “Efficient arbitrary simultaneously entangling gates on a trapped-ion quantum computer,” Nature Communications 11, 2963 (2020).** The inspected [arXiv:1905.09294v1](https://arxiv.org/html/1905.09294v1) presents the single-pair conditions in Section I and the EASE protocol in Section II; Section III describes implementation. [Published DOI](https://doi.org/10.1038/s41467-020-16790-9). Key: `Grzesiak2020`.

EASE constructs independently specified simultaneous pair interactions, including overlapping pairs, using linear closure conditions and bilinear phase constraints. Its constructive and experimental results preclude presenting arbitrary simultaneous gate synthesis as a new capability here. The present question charges primitive force norms and finite bus dimension, rather than only pulse-design complexity or the existence of a simultaneous solution.

### Zhu et al.: additional mode families enable parallel gates

**“Pairwise-Parallel Entangling Gates on Orthogonal Modes in a Trapped-Ion Chain,” Advanced Quantum Technologies 6, 2300056 (2023).** [Primary preprint v1](https://arxiv.org/html/2302.09145v1): Section II, Eqs. (1)–(7). [Published DOI](https://doi.org/10.1002/qute.202300056). Key: `Zhu2023`.

The scheme implements two pair gates through orthogonal radial mode families. Their commuting Hamiltonians allow independently designed gate pulses to run simultaneously, including when the pairs share an ion. This establishes additional motional modes as a parallelism resource and supplies a direct experimental precedent. Each family contains several canonical oscillator modes; a family is not one mode in the present count. The result does not supply a finite-mode primitive-force converse over all phase representatives or a fixed whole-layer diamond-error bound.

### Peleg et al.: a prior spectral resource estimate

**“Fast Design and Scaling of Multiqubit Gates in Large-Scale Trapped-Ion Quantum Computers,” PRX Quantum 7, 033021 (2026).** [Primary preprint v2](https://arxiv.org/html/2307.09566v2): Section II, “Formulation of the gate design problem,” particularly Eqs. (3) and (5); Section III, “Scalability in large ion crystals,” Eqs. (7) and (8); Appendix A, model derivation. [Published DOI](https://doi.org/10.1103/r78y-3q89). Key: `Peleg2026`.

Equation (7) estimates pulse amplitudes using the nuclear norm of the desired phase matrix; Eq. (8) gives a timescale related to mode spacing. The nuclear-norm estimate is heuristic and calibrated in the analyzed ion setting, with limitations discussed in that section. The relation between spectrum and control resources is therefore prior work. The present weighted, finite-mode converse has different hypotheses and includes the optimization over physical gate equivalence.

### Diaz et al.: the square-root parallel construction has a precedent

**“Arbitrary parallel entangling gates with independent calibration on a trapped ion quantum computer,” arXiv:2604.25993v1 (2026).** [Primary text](https://arxiv.org/html/2604.25993v1): Sections II–III; Appendix A.1, “Sequencing protocol”; A.2, “Disjoint null-space protocol”; A.3, “Common null-space protocol”; B.1, “Power Scaling.” Key: `Diaz2026`.

Appendix A.1 gives orthogonal sign sequencing and its square-root speedup over serial execution; the other protocols exploit pulse-space orthogonality and shared nullspaces. Their multimode ion results also support many disjoint gates in a duration comparable to a single gate in the examined regime. Consequently, a square-root parallel upper construction is not the distinguishing claim here. The finite-mode lower bound and its fixed-error, all-phase-representative treatment are the relevant additional statements. When the number of useful modes grows with the register, constant-order matching duration is consistent with the present law.

### Orozco-Ruiz and Mintert: mode resolution is not a universal prerequisite

**“Multi-ion entangling gates mediated by spectrally unresolved modes,” Physical Review A 114, 012422 (2026).** [Primary preprint v1](https://arxiv.org/html/2602.11326v1): Section II, “Framework,” Eq. (1); its subsections on effective interactions, spin echo, and boundary conditions; Section III.2, “Rainbow interaction.” [Published DOI](https://doi.org/10.1103/357p-y5qf). Key: `OrozcoRuiz2026`.

A time-dependent gradient drives the axial mode family, and closure plus echo design produces selected simultaneous interactions without resolving modes individually. This rules out identifying every gate-speed limitation with spectral resolution. A single envelope in that Hamiltonian still addresses multiple canonical oscillators: its number of drive channels is not its bus dimension. The force-and-closure model must be applied to the actual participating modes and boundary conditions.

## 3. Few-mode electrical resonators provide a physical setting

**Kerman, “Quantum information processing using quasiclassical electromagnetic interactions between qubits and electrical resonators,” New Journal of Physics 15, 123011 (2013).** [Primary preprint v4](https://arxiv.org/html/1212.3300v4): Section II, “General qubit-resonator system”; Section III, “Controlled-phase gate with quasiclassical forces”; Appendix C, higher resonator modes; Appendix E, comparison with trapped-ion gates. [Published DOI](https://doi.org/10.1088/1367-2630/15/12/123011). Key: `Kerman2013`.

This work develops qubit-conditioned electrical resonator displacements and selected interactions among qubits coupled to a common resonator. It grounds the few-mode architecture and highlights additional physical corrections. The existence and state-insensitivity of the closed-loop gate mechanism are antecedents, not contributions of this repository.

**Royer et al., “Fast and high-fidelity entangling gate through parametrically modulated longitudinal coupling,” Quantum 1, 11 (2017).** [Primary preprint v3](https://arxiv.org/html/1603.04424v3): “Oscillator mediated qubit-qubit interaction,” Eqs. (1)–(3); “Oscillator-induced qubit dephasing,” Eq. (4). [Published DOI](https://doi.org/10.22331/q-2017-05-11-11). Key: `Royer2017`.

This work supplies an explicit longitudinal-coupling Hamiltonian and a two-qubit operating example. The [hardware account](../science/hardware_resources.md) distinguishes its real modulation amplitude from the slow rotating-wave force amplitude. Gate noise and engineered squeezed inputs are additional physical questions; the present closed-system bound does not supply a fidelity prediction for that proposal.

## 4. Effective Ising time and compiled gate count are different costs

**Baßler, Heinrich, and Kliesch, “Time-optimal multi-qubit gates: Complexity, efficient heuristic and gate-time bounds,” Quantum 8, 1279 (2024).** [Primary preprint v2](https://arxiv.org/html/2307.11160v2), Section 2, Eq. (1), starts with a fixed native Ising Hamiltonian and optimizes the durations of sign encodings; Section 5 gives special constant-time constructions. [Published DOI](https://doi.org/10.22331/q-2024-03-13-1279). Key: `Bassler2024`.

That effective Hamiltonian already provides pair interactions. Its Ising evolution time does not include synthesizing those interactions from a finite conditional-force bus while returning the bus. The results therefore address a distinct resource model.

**Bravyi, Maslov, and Nam, “Constant-cost implementations of Clifford operations and multiply controlled gates using global interactions,” Physical Review Letters 129, 230501 (2022).** [Primary preprint v2](https://arxiv.org/html/2207.08691v2), Section I, defines a global tunable gate with an independently chosen interaction parameter for every qubit pair. [Published DOI](https://doi.org/10.1103/PhysRevLett.129.230501). Key: `Bravyi2022`.

A matching layer is already one such instruction. Constant numbers of these instructions can coexist with a growing physical implementation cost per instruction. The present result concerns that underlying force cost in the stated bus model, not the optimal compiled gate count.

## 5. What the additional converse establishes

The distinction rests on physical gate equivalence. At zero error, every allowed representative has a matching cross block $`C=(\pi/8)(I+2M)`$ for an integer matrix $`M`$. Its determinant cannot vanish. The resulting constraint on all singular values, combined with the weighted spectral control cost, prevents reducing the resource scaling by choosing a more favorable wrapped logarithm or unobservable diagonal.

At fixed whole-layer error, the proof derives a controlled unwrapping from closeness of the actual unitary channels. It does not assume that the implemented real phase matrix is already close to the preferred target matrix. This gives

```math
T\mathcal E=\Omega_\epsilon(K+K^2/m)
```

for every fixed $`\epsilon<1/\sqrt2`$, with exact bus closure retained. Together with an explicit exact upper bound it yields the scaling law in the [model](../science/model.md).

The cited geometric results and parallel-gate constructions are essential antecedents. The inspected results above do not supply this combined all-representative, fixed-error matching-layer converse under the same primitive-force assumptions. This scoped comparison is not a claim that spectral optimal control, geometric oscillator gates, parallel gates, or square-root upper constructions originate here.

## 6. Vacuum loss: established mechanism and a paid frontier

**Louis et al., “Loss in hybrid qubit-bus couplings and gates,” Physical Review A 78, 022326 (2008).** The primary [arXiv:0804.3240v1](https://arxiv.org/html/0804.3240v1), §IV, Eqs. (23)–(24), expresses lost-probe effects through coherent-state overlaps. Eqs. (36)–(39) combine sequences to retain a conditional phase with independent single-qubit dephasing. Loss-induced decoherence and control of error correlations are established; correlated errors are not unavoidable for every pulse sequence. Key: `Louis2008`.

**Müller, Luoma, and Strunz, “Geometric phase gates in dissipative quantum dynamics,” Physical Review A 102, 032611 (2020).** The primary [arXiv:1907.08033v2](https://arxiv.org/html/1907.08033v2), §III.1, retains both coherence attenuation and an environment-induced phase. §III.2, Eqs. (27)–(28), explains how faster winding reduces the squared excursion integral at fixed geometric phase. The journal year is 2020; the inspected preprint revision is dated 14 April 2021. Their §VI distinguishes damping from the heating relevant to typical ion-gate conditions. Key: `Mueller2020`.

The [vacuum-loss account](../science/loss_and_frontier.md) keeps this distinction explicit. With trajectory matrix $`D(t)`$, exact closure and uniform amplitude decay $`\kappa/2`$ give

```math
\mathcal E=E_{\mathrm{path}}+\frac{\kappa^2}{4}X,
\qquad
E_{\mathrm{path}}=\int_0^T\lVert\dot D\rVert_F^2dt,
\qquad
X=\int_0^T\lVert D\rVert_F^2dt.
```

Its fixed-matrix frontier charges both the drive needed to follow the path and the exposure that loss can reveal. The exact reduced channel retains the real and imaginary parts of $`\int D^\dagger D\,dt`$. The established winding-versus-dephasing mechanism is therefore coupled to an explicit finite-force optimization; exposure does not by itself solve the full channel-error problem. The exact frontier is for a prescribed full $`A`$. Optimization over every phase-equivalent gate remains separate, and a lossless upper construction alone supplies no noisy-gate upper bound.

For fidelity conventions, [Nielsen (2002)](https://arxiv.org/html/quant-ph/0205035v2), Eqs. (2)–(3), gives a proof of the Horodecki relation $`F_{\mathrm{avg}}=(dF_e+1)/(d+1)`$ after composing with the inverse target unitary (`Nielsen2002`). These average quantities remain distinct from the whole-layer half-diamond error used by the converses.
