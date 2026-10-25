# Related work and scope of the contribution

Literature and bibliographic status checked on **24 October 2026**. Citation keys refer to [references.bib](references.bib). Links below point to primary papers, publisher records, or author manuscripts. Preprints are identified as such.

## 1. Problem and resource convention

The model, proofs, and architectural implications are developed in [model.md](../science/model.md), [spectral_cost.md](../science/spectral_cost.md), [loss_and_frontier.md](../science/loss_and_frontier.md), and [architecture.md](../science/architecture.md).

The object of study is a layer of commuting entangling gates mediated by $`b`$ harmonic oscillators. Independently programmable forces couple each qubit's fixed Pauli operator to oscillator displacement. Every computational branch returns every oscillator to its initial displacement at time $`T`$. With the trajectory matrix $`A(t)\in\mathbb{C}^{b\times n}`$, this means $`A(0)=A(T)=0`$. The geometric phase convention is

```math
K=\mathrm{Im}\int_0^T A^\dagger\dot A\,dt,
\qquad U_K=\exp(iZ^TKZ).
```

Thus the physical coefficient of $`Z_iZ_j`$, for $`i\lt j`$, is $`2K_{ij}`$. Diagonal entries of $`K`$ contribute only a global phase. Closed displacement gates and their phase-space interpretation are standard; see the reviews of [Häffner, Roos, and Blatt](https://arxiv.org/abs/0809.4368), especially §2.6, and [Leibfried et al.](https://doi.org/10.1103/RevModPhys.75.281) (`Haeffner2008`, `Leibfried2003`).

The charged control resource is the integrated squared spin–oscillator coupling, $`G=\int_0^T\sum_{\mu i}\vert u_{\mu i}(t)\vert ^2dt`$. This is an action in coupling units; its identification with electrical or optical energy requires a device-specific calibration. In the absence of damping, $`u=\dot A`$ and $`G=E:=\int\Vert \dot A\Vert _F^2dt`$. For uniform vacuum loss with Lindblad rate $`\kappa`$ (amplitude decay rate $`\kappa/2`$), $`u=\dot A+\kappa A/2`$ and exact closure gives

```math
G=E+\frac{\kappa^2}{4}X,
\qquad X:=\int_0^T\Vert A(t)\Vert _F^2dt.
```

Neither an uncharged infinite drive nor an uncharged increase in oscillator number is allowed. The lower bounds optimize over all waveforms in this model, without imposing a bandwidth cutoff. This enlarges the allowed control set and makes a converse stronger; attaining the associated upper bounds can require increasing bandwidth.

## 2. The spectral control mathematics is inherited

The closest mathematical predecessor is **Wong and Baillieul, “Control Communication Complexity of Distributed Actions”** (`WongBaillieul2012`, [paper](https://arxiv.org/abs/1201.6527), [DOI](https://doi.org/10.1109/TAC.2012.2192357)). Their Theorem 5.1 minimizes a quadratic control cost for a prescribed matrix of outputs of a bounded bilinear map. In their average-over-control-choices normalization,

```math
\widehat C_F(H)=\frac{2}{\sqrt{mn}}
\sum_k\frac{\sigma_k(H)}{\sigma_k(F)}.
```

For the closed-loop Brockett–Heisenberg system, Corollary 5.1 gives harmonic weights $`\lceil k/2\rceil`$. Its Fourier multiplicity, weighted singular-value minimization, and optimal allocation of matrix components to control harmonics are direct antecedents of the present analysis. A weighted spectral cost should therefore not be presented as a newly discovered control principle. The signed symmetric phase problem and its bus multiplicity need explicit translation, but that translation uses this established machinery.

There is also an older geometric lineage. [Brockett's chapter](https://doi.org/10.1007/978-1-4612-5651-9_2) (`Brockett1982`) connects quadratic control effort to constrained area and singular Riemannian geometry. [Rizzi and Serres](https://arxiv.org/abs/1610.01596) (`RizziSerres2017`), Appendix A, give an explicit spectral distance formula for vertical points of free step-two Carnot groups and discuss an earlier normalization issue. These are antecedents for matrix-valued area costs. The present derivation is self-contained and does not import a normalization from that formula.

For a **fixed full real symmetric $`K`$**, the present form of the result is

```math
E_{\min}(K,T,b)=\frac{2\pi}{T}\Phi_b(K),
\qquad
\Phi_b(K)=\sum_j\Big\lceil\frac{j}{2b}\Big\rceil\lambda_j^+(K)
+\sum_j\Big\lceil\frac{j}{2b}\Big\rceil\vert \lambda_j^-(K)\vert ,
```

where each sign's eigenvalues are ordered by decreasing magnitude. A signed Fourier harmonic supplies at most $`2b`$ real directions. This exact formula is best understood as the symmetric quantum-gate specialization of spectral bilinear control, with the normalization and physical resource interpretation made explicit.

## 3. What the quantum unitary adds

Prescribing one real phase matrix is stronger than prescribing its quantum gate. Global phases, local $`Z`$ rotations, and large integer phase windings can change the matrix representative while leaving the desired nonlocal operation unchanged. A lower bound evaluated only on a convenient representative does not exclude a cheaper equivalent gate.

The additional argument addresses that quotient. For a matching of $`m`$ controlled-$`Z`$ gates across the two halves of a bipartition, every exact representative, after allowing local $`Z`$ phases, has cross block

```math
K_{AB}=\frac{\pi}{8}(I+2B),\qquad B\in\mathbb{Z}^{m\times m}.
```

The integer matrix $`I+2B`$ has an odd, hence nonzero, determinant. Combined with the cross-block spectral action bound and weighted arithmetic–geometric mean inequality, this prevents arbitrary phase wraps from removing the action scaling

```math
ET=\Omega(m+m^2/b).
```

Explicit closed trajectories attain the same order in the lossless model. At a total instantaneous squared-coupling budget $`P`$, the optimal lossless time is consequently

```math
T=\Theta\!\left(\sqrt{\frac{m+m^2/b}{P}}\right).
```

If each qubit has total squared coupling at most $`g^2`$, the large-matching regime gives $`T=\Theta(\sqrt{m/b}/g)`$. Dense low-rank collective interactions and independent pairs can therefore have very different costs even when the hardware connectivity is all-to-all.

The fixed-error extension is a second essential step. Uniformly small error in a diagonal quadratic phase forces its nearest integer-valued phase lift to remain quadratic: third Boolean mixed differences vanish once the phase tolerance is below $`\pi/4`$. Parseval bounds the residual cross-matrix Frobenius norm; singular-value perturbation bounds then preserve the asymptotic matching cost. For the actual closed-bus vacuum-loss channel, half-diamond error $`\epsilon\lt 1/(2\sqrt2)`$ implies the needed phase tolerance $`\delta=\arcsin(2\epsilon)\lt \pi/4`$. This makes the converse a statement about a gate at fixed nonzero accuracy, including the noisy channel, rather than merely about exact synthesis of one real matrix.

The reviewed controls papers do not state this quantum phase-lattice argument or this fixed-error matching result. This is a bounded literature finding, not a proof that no related result exists elsewhere.

## 4. Comparison with gate synthesis and architecture literature

| Work | Established result or model | Relation to this project |
|---|---|---|
| [Grzesiak et al. (2020)](https://www.nature.com/articles/s41467-020-16790-9), `Grzesiak2020` | EASE constructs arbitrary simultaneous pairwise couplings, including overlapping pairs, with closure of the ion-chain motion and efficient classical pulse synthesis. | Establishes programmability and practical simultaneous control. It does not provide the universal action converse with finite $`b`$ and all equivalent phases included. |
| [Peleg et al. (2026)](https://doi.org/10.1103/r78y-3q89), `Peleg2026` | Efficient large-crystal multiqubit-gate design; investigates gate-time, power, and noise scaling. | The nearest trapped-ion resource comparison; the detailed distinction is given below. |
| [Diaz et al. (2026), preprint](https://arxiv.org/abs/2604.25993), `Diaz2026` | Parallel gates with independent calibration; disjoint pairs in the tested chains run in a time comparable to a single-pair gate. | Does not contradict a bound when the number of available motional modes grows with the system. Its power and mode-resolution assumptions must be retained. |
| [Baßler et al. (2023)](https://quantum-journal.org/papers/q-2023-04-20-984/), `Bassler2023` | Time-optimal synthesis from a fixed Ising interaction, selective participation, and local sign changes, using linear programming. | Optimizes time after the effective Ising interaction is supplied. It does not charge microscopic oscillator force, excursion, or exact bus return. |
| [Devulapalli et al. (2026)](https://doi.org/10.1103/7b1x-hjcy), `Devulapalli2026` | Routing and entanglement-generation bounds through finite bottlenecks under specified Hamiltonian norm and temporal-control assumptions. | Already establishes that high connectivity can conceal severe parallelism limits. The distinction here is the unbounded harmonic mediator, the charged force model, and the gate-specific phase quotient. |

In **Peleg et al.**, §III, Eq. (7) is explicitly a heuristic drive estimate involving the nuclear norm of an entrywise-absolute target-coupling matrix. Their numerical results associate dense all-crystal gates with mode-resolution times that grow with ion number. This is materially close motivation. Their Appendix C assigns distinct tones to different pairs, while §V and Fig. 7 analyze unwanted cross-entanglement and its cancellation when pairs share modes. The resource and cancellation intuition deserves credit. Their estimate is not the exact signed, harmonic-rank-weighted action in §2: it does not optimize over the quantum phase lattice, prove the matching bound for every waveform, or give the fixed-error converse. These comparisons were checked in the [final published paper](https://journals.aps.org/prxquantum/pdf/10.1103/r78y-3q89), as well as the [arXiv v2 manuscript](https://arxiv.org/html/2307.09566v2).

In **Diaz et al.**, Appendix B.1 explicitly studies pulse-power growth: at a fixed 300-microsecond duration, the reported scaling changes when the motional spectrum becomes too crowded. Their finite-chain demonstrations and proposed use of multiple medium-length chains are compatible with the distinction between connectivity and independently usable mediators. The present asymptotic statement concerns fixed or sublinear $`b`$, under a stated coupling normalization. It does not assert that existing parallel-gate demonstrations violate a speed limit. [Primary manuscript, v1](https://arxiv.org/html/2604.25993v1).

In **Devulapalli et al.**, nearly square-root bottleneck behavior already appears for entanglement generation through a small qubit region. That exponent, or the phrase “bottleneck,” cannot carry the novelty claim here. Their bounded qubit-interaction assumptions do not directly encompass linear bosonic force operators with unrestricted occupation; their free-particle routing result also concerns a different, number-conserving dynamics. Translating a physical drive budget into either model is necessary before comparing scalings. [Published paper](https://journals.aps.org/prxquantum/pdf/10.1103/7b1x-hjcy).

Two concrete architectural choices clarify the motivation. [Li et al. (2013)](https://arxiv.org/abs/1208.2863), `Li2013`, propose Rydberg mode shaping to create independently addressable vibrational sub-crystals. This increases the supply of independent mediating motion. [Mai et al. (2026)](https://doi.org/10.1126/sciadv.aec0392), `Mai2026`, use structured-light addressing to isolate a single or few sparse axial modes while retaining qubit addressability. Their two-qubit demonstrations motivate the complementary question studied here: what parallelism cost remains when control is deliberately concentrated into few mediators? The tradeoff is our inference from their architecture, not a lower bound proved in their paper. [Open primary manuscript](https://arxiv.org/html/2506.19535v1).

## 5. Dissipation: known mechanism, paid resource frontier

**Louis et al. (2008)** already derive effective operations for lossy qubit–bus gates from the distinguishability of conditional bus states. Their iteration construction converts the resulting noise to independent single-qubit dephasing while retaining the conditional gate. Conditional-environment overlaps, correlated dephasing, and the possibility of modifying correlations by pulse design are therefore established prior results (`Louis2008`, [paper](https://arxiv.org/abs/0804.3240)).

**Müller, Luoma, and Strunz**, published in **2020** after a 2019 preprint, analyze geometric gates with oscillator dissipation, including a complex environment-induced phase. Their §III.2, Eqs. (27)–(28), compares geometric phase with the time integral of the squared excursion and explicitly explains that increased winding can reduce dephasing at fixed enclosed phase. They also discuss compensating forces and extension to more spin branches. The winding-versus-loss mechanism is thus not new here. Their analysis does not impose and solve the present finite-force, finite-bus spectral optimization (`Mueller2020`, [v2](https://arxiv.org/html/1907.08033v2)).

The present exact statement charges that mitigation. For a fixed full phase matrix $`K`$, uniform damping $`\kappa`$, and exposure price $`\mu\ge0`$, define

```math
s_k(\mu)=2\sqrt{(k\pi/T)^2+\kappa^2/4+\mu}.
```

The supported drive–exposure frontier is

```math
\min_{A:\,K(A)=K}\{G(A)+\mu X(A)\}
=\sum_j s_{\lceil j/(2b)\rceil}(\mu)\lambda_j^+(K)
+\sum_j s_{\lceil j/(2b)\rceil}(\mu)\vert \lambda_j^-(K)\vert .
```

It applies the inherited spectral method to the damped, closed-displacement control problem. It is exact for fixed $`K`$; optimization over all phase-equivalent $`K`$ is a separate quantum problem. For the full gate quotient, the matching converse supplies a robust lower bound rather than a claim that the global frontier is solved for every target gate.

The exact reduced channel retains both attenuation from the real part of the trajectory Gram matrix and a phase from its imaginary part. Dropping the latter is generally incorrect. Exposure also supplies the channel bound

```math
\tfrac12\Vert \mathcal{E}-\mathcal{U}_K\Vert _\diamond
\ge\frac{1-e^{-2\kappa X}}{2}.
```

This links the paid control frontier to an operational error measure. An exact lossless construction is not automatically an achievable noisy-gate upper bound.

The reservoir assumption matters. Müller et al. distinguish damping from the heating common in ion motion. [Grossman et al. (2026), preprint](https://arxiv.org/abs/2605.28536), `Grossman2026`, treats phonon heating, motional dephasing, and photon scattering in multiqubit ion gates and connects them to surface-code simulations. The vacuum-loss result here is not a replacement for that microscopic ion-noise model, nor does it establish a fault-tolerance threshold.

## 6. Precise boundary of the claims

The combined contribution is a resource theorem for **closed, commuting displacement gates**: a correctly normalized spectral specialization; a lower bound that survives all local phase choices and integer phase wraps; stability at fixed channel error; and an exactly solved, paid drive–exposure optimization for a fixed phase matrix. The primitive gate mechanism, spectral bilinear optimization, loss-induced dephasing, and general architectural bottleneck intuition are inherited from the work above.

The result does not cover unrestricted noncommuting spin control, squeezing, nonlinear or encoded bosonic buses, auxiliary coherent processors, measurement and feedback, or approximate bus return. Nor does it by itself quantify an entire processor's throughput, optical wattage, achievable bandwidth, or ion heating. A concrete hardware comparison must count all active mediator modes, map its control amplitudes into $`u_{\mu i}`$, and check that the proposed protocol remains inside this model.

## 7. Version and metadata notes

- **Wong–Baillieul:** final journal record is *IEEE Transactions on Automatic Control* **57**(11), 2731–2745 (2012); the theorem numbering above was checked in arXiv:1201.6527v2.
- **Peleg et al.:** journal publication is *PRX Quantum* **7**, 033021, **31 July 2026**; Eq. (7), §V, and Appendix C were checked in the final publication and compared with arXiv:2307.09566v2.
- **Devulapalli et al.:** *PRX Quantum* **7**, 010310, **15 January 2026**; the published paper was inspected.
- **Müller et al.:** *Physical Review A* **102**, 032611 (2020), not a 2019 journal article; arXiv:1907.08033v2 is dated 14 April 2021.
- **Diaz et al.** and **Grossman et al.:** arXiv v1 preprints were current in the retrieved records; no journal publication is asserted.
- **Grzesiak et al.:** the bibliography follows the published author list, including Ming Li, rather than the shorter initial preprint list.
- **Mai et al.:** *Science Advances* **12**(14), eaec0392 (2026), online 1 April, issue date 3 April; publication metadata was cross-checked against the [indexed journal record](https://pubmed.ncbi.nlm.nih.gov/41920994/) and the primary arXiv manuscript.
