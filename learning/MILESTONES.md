# Project understanding map: 30 milestones

This map organizes Quantum Bus Congestion into exactly **30 milestones**. Its targets and order follow the scientific dependencies of the project and are common to every reader, including an LLM.

The allocation is **13 background/preliminaries milestones** and **17 narrative/innovation milestones**. The background begins with a qubit and an oscillator, develops a two-qubit gate and its environment, then introduces register-level matrix, temporal, Boolean, and resource tools. The narrative begins again with one completely specified CZ loop. It then joins the spectral control theorem, quantum phase equivalence, approximation robustness, exact loss model, and paid architecture consequences. Seventeen narrative milestones give these logically distinct arguments room before the final synthesis.

The single educational anchor is H. Häffner, C. F. Roos, and R. Blatt, *Quantum computing with trapped ions* (2008), specifically **[arXiv:0809.4368v1][HRB]**. The [Häffner bridge](HAEFFNER_BRIDGE.md) owns the detailed section mapping, notation translation, and source-to-model transition. The review supplies the physical route into the project. The matrix optimization, functional analysis, Boolean unwrapping, and diamond-distance arguments are supplied by the project pages; they are not attributed to the review. Other primary references remain sources of mathematical and physical attribution, not additional educational anchors.

Each milestone gives a central question, an understanding target, earlier dependencies and its role in the story, a conceptual connection, and anchor/project source pointers. The scientific pages remain authoritative for exact assumptions, constants, and complete proofs. The 2008 review is used for physical foundations and historical context, not as a current hardware performance forecast.

[HRB]: https://arxiv.org/pdf/0809.4368v1

## Route through the project

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | [M01](#m01-local-qubits-and-phase-conventions)–[M06](#m06-state-fidelity-process-error-and-operational-distance) | Local quantum phases, one oscillator, conditional gates, environmental records, and operational error |
| Background/preliminaries | [M07](#m07-normal-modes-addressability-and-physical-controls)–[M11](#m11-quadratic-boolean-phases-and-their-modular-ambiguity) | A register's physical controls and the matrix, temporal, and Boolean tools needed to analyze it |
| Background/preliminaries | [M12](#m12-a-complete-ledger-of-control-resources)–[M13](#m13-the-complete-architecture-question) | The full resource ledger, model boundaries, and quantifiers of an architecture claim |
| Narrative/innovation | [M14](#m14-a-fully-paid-single-cz-loop)–[M19](#m19-the-sharp-cost-of-a-cross-block) | A concrete gate develops into the exact spectral optimum and its sharp cross-block consequence |
| Narrative/innovation | [M20](#m20-quantum-phase-equivalence-and-the-odd-determinant)–[M24](#m24-a-positive-congestion-bound-at-every-size) | All quantum phase representatives, attaining matching controls, physical caps, and finite-accuracy robustness |
| Narrative/innovation | [M25](#m25-the-exact-lossy-channel-and-its-skew-phase)–[M28](#m28-the-complete-fixed-matrix-exposure-frontier) | The actual noisy channel, operational converses, and exact paid-action/exposure optimization |
| Narrative/innovation | [M29](#m29-a-paid-architecture-comparison-with-global-accuracy)–[M30](#m30-the-complete-scoped-architecture-story) | Explicit resource comparisons and the complete, attributed architecture conclusion |

## Phase I: background/preliminaries

### M01 Local qubits and phase conventions

**Central question.** Which phases change a quantum operation, and which can be removed by allowed local control?

**Understanding target.** Interpret a qubit state, Pauli $`Z`$, and a diagonal rotation in a fixed computational basis. Distinguish a scalar global phase from a relative phase, and a product of one-qubit phases from a two-qubit conditional phase. The sign labels $`z_i=\pm1`$ and bit labels $`x_i=(1-z_i)/2`$ describe the same basis with different polynomial coefficients.

**Earlier dependencies and story role.** None within the map. This fixes the local language used in every subsequent gate-equivalence statement.

**Conceptual connection.** A change of basis is a specified control operation. It does not make a time-dependent, noncommuting coupling axis part of a model that permits only fixed commuting $`Z_i`$ forces.

**Anchor and project sources.** [HRB] §2.5, especially the single-qubit rotation convention; [model, §§1–2](../science/model.md#1-dynamics-and-admissible-controls), including equation (M8).

### M02 One harmonic mode and coherent displacement

**Central question.** What does a point in oscillator phase space represent physically?

**Understanding target.** Relate $`a,a^\dagger`$, number states, vacuum, and a coherent amplitude $`\alpha`$ to a harmonic oscillator. Interpret $`D(\alpha)=e^{\alpha a^\dagger-\alpha^*a}`$ and $`\langle a^\dagger a\rangle=\vert \alpha\vert ^2`$ for a coherent state. The noncommuting composition of displacements produces a phase, while the coherent-state overlap carries both magnitude and phase information.

**Earlier dependencies and story role.** [M01](#m01-local-qubits-and-phase-conventions) supplies phase conventions. The oscillator now provides the smallest mediator in the story.

**Conceptual connection.** An oscillator mode has an unbounded harmonic ladder in this model. A finite-dimensional bus approximation and a fixed peak occupation are additional assumptions.

**Anchor and project sources.** [HRB] §§2.2 and 2.6.4, with Fig. 15 for the state-dependent-force picture; [conditional trajectories](../science/model.md#2-conditional-trajectories-closure-and-phase) and [coherent-state overlaps](../science/loss_and_frontier.md#coherent-state-dilation) supply the explicit phase-space conventions.

### M03 From ion-light coupling to a conditional force

**Central question.** How does a laboratory spin–motion interaction become the force used in the model?

**Understanding target.** Identify the roles of the rotating frame, carrier and sideband terms, Lamb–Dicke expansion, detuning, and optical phase. Relate a fixed-axis spin-dependent force to $`iZ(ua^\dagger-u^*a)`$, keeping the complex envelope and its two quadratures explicit. The resulting effective Hamiltonian is a controlled approximation to particular hardware interactions.

**Earlier dependencies and story role.** [M01](#m01-local-qubits-and-phase-conventions) and [M02](#m02-one-harmonic-mode-and-coherent-displacement) provide the spin and oscillator. This milestone identifies the physical entry point and its approximation boundary.

**Conceptual connection.** A fixed spin-axis convention can describe an appropriate gate interaction after a specified basis change. Independently programmable complex envelopes on every qubit–mode coupling remain a stronger assumption than many native drive arrangements.

**Anchor and project sources.** [HRB] §2.2, equations (1)–(7), and §§2.6.3–2.6.4; [admissible controls](../science/model.md#1-dynamics-and-admissible-controls); [Häffner bridge](HAEFFNER_BRIDGE.md).

### M04 A closed loop as an entangling primitive

**Central question.** How can motion return to its initial state while leaving a nontrivial spin gate?

**Understanding target.** Follow the conditional oscillator path for each spin-basis branch. Exact return removes the final spin–bus correlation, while the accumulated phase depends on the path's signed area. For two qubits, the branch phases can contain an entangling $`Z_1Z_2`$ term even when the bus returns to vacuum.

**Earlier dependencies and story role.** [M02](#m02-one-harmonic-mode-and-coherent-displacement) and [M03](#m03-from-ion-light-coupling-to-a-conditional-force) combine into the first mediated gate.

**Conceptual connection.** Bus return and zero gate action are different conditions. The useful output is the phase retained by the spins; the mediator can finish in its initial state.

**Anchor and project sources.** [HRB] §2.6.4 and Fig. 15; [closure and geometric phase](../science/model.md#2-conditional-trajectories-closure-and-phase). The project's vacuum assumption for loss is specified separately.

### M05 An open bus leaves an environmental record

**Central question.** What can the environment retain after the oscillator itself has returned?

**Understanding target.** Trace out an environment whose state depends on the spin branch. Its branch overlaps multiply spin coherences, so final bus closure does not imply a unitary reduced spin channel. In the project's vacuum Markov model, $`\kappa`$ is the number-decay rate and coherent amplitudes decay at $`\kappa/2`$.

**Earlier dependencies and story role.** [M02](#m02-one-harmonic-mode-and-coherent-displacement) and [M04](#m04-a-closed-loop-as-an-entangling-primitive) provide the paths whose histories can become distinguishable.

**Conceptual connection.** Motional heating, dephasing, and vacuum amplitude damping are different physical processes. The review's discussion of ion-motion imperfections motivates an open-system analysis without identifying every experimental mechanism with $`\kappa\mathcal{D}[a]`$.

**Anchor and project sources.** [HRB] §§3.2–3.3 for motional coherence and modeling; [vacuum Markov dynamics](../science/model.md#1-dynamics-and-admissible-controls) and [the output-field dilation](../science/loss_and_frontier.md#coherent-state-dilation) specify the project's narrower channel.

### M06 State fidelity, process error, and operational distance

**Central question.** What does it mean for an entire gate to be accurate?

**Understanding target.** Distinguish preparation of one desired state from approximation of a quantum channel on all inputs. Separate state fidelity, entanglement fidelity, average gate fidelity, and half-diamond distance $`\Vert \mathcal{E}-\mathcal{V}\Vert _\diamond/2`$. The last is a worst-case distinguishability criterion that permits an ancilla; a particular input supplies a lower bound.

**Earlier dependencies and story role.** [M01](#m01-local-qubits-and-phase-conventions), [M04](#m04-a-closed-loop-as-an-entangling-primitive), and [M05](#m05-an-open-bus-leaves-an-environmental-record) connect the ideal operation to its noisy output.

**Conceptual connection.** A Bell-state fidelity, an averaged error, and a global layer-error guarantee support different conclusions. None alone supplies a local stochastic noise model or fault-tolerance threshold.

**Anchor and project sources.** [HRB] §§4.4 and 4.7 motivate state/process characterization; [operational error and fidelities](../science/loss_and_frontier.md#2-operational-error-and-first-order-gate-metrics) and [matching conventions](../science/matching.md#1-conventions-and-precise-scope) supply the precise metrics used here.

### M07 Normal modes, addressability, and physical controls

**Central question.** Which independent resources are present when many qubits share motion?

**Understanding target.** Interpret collective normal modes, qubit participation in each mode, and individually specified control coefficients. Keep physical modes $`b`$, data qubits $`n`$, control channels, and temporal modulation harmonics distinct. The same oscillator can carry several time-dependent directions without becoming several physical buses.

**Earlier dependencies and story role.** [M03](#m03-from-ion-light-coupling-to-a-conditional-force) and [M04](#m04-a-closed-loop-as-an-entangling-primitive) extend from one pair to a register.

**Conceptual connection.** A converse for independent envelopes remains valid when hardware imposes further restrictions. An attaining waveform may cease to be available when couplings are tied or only one real quadrature is controlled.

**Anchor and project sources.** [HRB] §2.6.1, especially the normal-mode discussion and Fig. 10, plus §2.7; [control access](../science/model.md#1-dynamics-and-admissible-controls) and [physical-mode accounting](../science/architecture.md#5-bandwidth-occupation-preparation-and-memory).

### M08 A register of conditional paths and its phase matrix

**Central question.** How can one matrix describe all computational branches of a multiqubit gate?

**Understanding target.** Interpret the columns of $`A(t)\in\mathbb{C}^{b\times n}`$ as displacement coefficients and $`A(t)z`$ as a branch amplitude. A quadratic phase $`z^{\mathsf{T}}Kz`$ encodes all pair angles. For symmetric $`K`$, the physical coefficient is $`2K_{ij}`$ and its ordinary diagonal contributes only $`\mathrm{tr}K`$.

**Earlier dependencies and story role.** [M01](#m01-local-qubits-and-phase-conventions), [M04](#m04-a-closed-loop-as-an-entangling-primitive), and [M07](#m07-normal-modes-addressability-and-physical-controls) provide the branch and mode interpretation.

**Conceptual connection.** A collective rank-one phase and a matching of independent pairs are different tasks, even if both create entanglement. Fixing a full matrix $`K`$ is also a stronger requirement than fixing its physical quantum gate.

**Anchor and project sources.** [HRB] §§2.6.3–2.6.4 and §3.3 provide multiqubit context; [matrix trajectories and phase](../science/model.md#2-conditional-trajectories-closure-and-phase) supplies this notation.

### M09 Real Gram matrices and spectral matrix tools

**Central question.** Which matrix properties express independent phase directions and unavoidable cost?

**Understanding target.** Connect Gram positivity, real and complex ranks, positive and negative eigenvalue lists, singular values, and Frobenius/nuclear/operator norms. Understand the roles of eigenvalue monotonicity, low-rank approximation, and norm duality. A real Gram matrix obtained from complex vectors can have twice their complex rank.

**Earlier dependencies and story role.** [M02](#m02-one-harmonic-mode-and-coherent-displacement) and [M08](#m08-a-register-of-conditional-paths-and-its-phase-matrix) give the vectors and matrices being analyzed.

**Conceptual connection.** Real environmental-record rank, complex jump-operator rank, and the number of physical oscillators are not interchangeable. Matrix order and scalar trace inequalities also carry different information.

**Anchor and project sources.** [HRB] §§2.6.1 and 3.3 are physical context only; [environmental rank](../science/model.md#5-environmental-rank-is-not-physical-bus-count) and [spectral proofs, §§2–4](../science/spectral_cost.md#2-fixed-matrix-optimum) supply the additional matrix tools.

### M10 Closed trajectories, Fourier modes, and variational spectra

**Central question.** What mathematical structure makes a continuum of possible pulses analyzable?

**Understanding target.** Interpret $`L^2`$ controls, $`H_0^1`$ paths, endpoint traces, Fourier orthogonality, Parseval, and Dirichlet Poincaré. Understand why a quadratic area form can be represented relative to a positive control-cost inner product, and how a complete self-adjoint spectrum can replace a pulse-by-pulse search.

**Earlier dependencies and story role.** [M04](#m04-a-closed-loop-as-an-entangling-primitive), [M08](#m08-a-register-of-conditional-paths-and-its-phase-matrix), and [M09](#m09-real-gram-matrices-and-spectral-matrix-tools) connect closure, matrices, and quadratic costs.

**Conceptual connection.** Satisfying oscillator return imposes a boundary condition, not a hard bandwidth or zero-force switching condition. Completeness of a modal description requires an analytic argument beyond checking a few pulse shapes.

**Anchor and project sources.** [HRB] §§2.6.4 and 3.3 motivate the control problem; [Fourier regularity](../science/spectral_cost.md#21-fourier-representation-including-the-endpoint-issue) and [the area operator](../science/loss_and_frontier.md#3-spectrum-of-the-closed-loop-area-operator) supply the functional analysis.

### M11 Quadratic Boolean phases and their modular ambiguity

**Central question.** Which algebra keeps track of a phase specified only modulo $`2\pi`$?

**Understanding target.** Relate multilinear polynomials on the bit cube to Walsh characters on the sign cube. Mixed finite differences expose polynomial degree; integer-valued functions have integer multilinear coefficients when evaluated by differences at the origin. Walsh orthogonality and Parseval turn a uniform residual bound into a bound on its coefficient squares.

**Earlier dependencies and story role.** [M01](#m01-local-qubits-and-phase-conventions), [M06](#m06-state-fidelity-process-error-and-operational-distance), and [M08](#m08-a-register-of-conditional-paths-and-its-phase-matrix) identify the modular phase whose accuracy will matter.

**Conceptual connection.** Selecting a principal value separately at every basis state need not preserve a low polynomial degree. The later robustness proof must justify that passage before applying a matrix perturbation bound.

**Anchor and project sources.** [HRB] §2.6.4 supplies only the conditional-phase motivation. The finite-difference and Walsh/Parseval tools are project supplements in [matching, §5](../science/matching.md#5-uniform-phase-unwrapping-on-the-boolean-cube).

### M12 A complete ledger of control resources

**Central question.** What is paid when the same gate is delivered by different paths, modes, or durations?

**Understanding target.** Distinguish derivative action $`E=\int\Vert \dot A\Vert _F^2dt`$, exposure $`X=\int\Vert A\Vert _F^2dt`$, and physical drive action $`G=\int\Vert u\Vert _F^2dt`$. Under exact damped closure, $`G=E+\kappa^2X/4`$. A pointwise total cap gives $`G\leq PT`$, while a per-qubit cap sums over all modes coupled to that qubit.

**Earlier dependencies and story role.** [M05](#m05-an-open-bus-leaves-an-environmental-record), [M07](#m07-normal-modes-addressability-and-physical-controls), [M08](#m08-a-register-of-conditional-paths-and-its-phase-matrix), and [M10](#m10-closed-trajectories-fourier-modes-and-variational-spectra) establish the physical and analytic quantities being budgeted.

**Conceptual connection.** Squared-coupling action is not automatically laboratory energy in joules. Basis-averaged exposure does not bound maximum branch occupation, and an integrated action bound does not imply an instantaneous force cap.

**Anchor and project sources.** [HRB] §§2.7 and 6–8 motivate hardware accounting; [what is paid](../science/model.md#3-what-is-paid) and [architecture resources](../science/architecture.md#5-bandwidth-occupation-preparation-and-memory) define the project ledger.

### M13 The complete architecture question

**Central question.** Which operational task and which assumptions make a congestion theorem meaningful?

**Understanding target.** Assemble the task: a layer of $`m`$ independent CZ pairs on arbitrary input states, implemented through $`b`$ linear harmonic buses with commuting force axes, exact conditional return, and specified force and accuracy budgets. Separate a fixed-$`K`$ optimum, a gate-equivalent minimum, a constructive upper bound, and a noisy necessary condition.

**Earlier dependencies and story role.** [M06](#m06-state-fidelity-process-error-and-operational-distance), [M09](#m09-real-gram-matrices-and-spectral-matrix-tools), [M10](#m10-closed-trajectories-fourier-modes-and-variational-spectra), [M11](#m11-quadratic-boolean-phases-and-their-modular-ambiguity), and [M12](#m12-a-complete-ledger-of-control-resources) complete the preliminary framework.

**Conceptual connection.** Small demonstrations of simultaneous pair gates and collective entanglement are compatible with a scaling cost for an extensive matching. Connectivity alone does not specify simultaneous independent-gate capacity.

**Anchor and project sources.** [HRB] §§2.1, 5.5, and 8 provide task and architecture context; [matching scope](../science/matching.md#1-conventions-and-precise-scope), [architecture question](../science/architecture.md#1-independent-gates-and-collective-phases-have-different-costs), and [claim boundaries](../references/related_work.md#6-precise-boundary-of-the-claims).

## Phase II: narrative/innovation

### M14 A fully paid single-CZ loop

**Central question.** What does one exact entangling gate cost in the project's conventions?

**Understanding target.** Interpret the one-bus path $`\alpha_1=\alpha_2=(e^{2\pi it/T}-1)/4`$. Every entry of its two-by-two $`K`$ is $`\pi/8`$, so its physical pair angle is $`\pi/4`$ and local $`Z`$ corrections give CZ. The path closes, has $`E=\pi^2/(2T)`$ and $`X=T/4`$, and saturates the lossless individual cap when $`gT=\pi/2`$.

**Earlier dependencies and story role.** [M04](#m04-a-closed-loop-as-an-entangling-primitive), [M08](#m08-a-register-of-conditional-paths-and-its-phase-matrix), [M12](#m12-a-complete-ledger-of-control-resources), and [M13](#m13-the-complete-architecture-question) support this local restart of the project narrative.

**Conceptual connection.** The same explicit trajectory fixes phase, action, exposure, and peak force. Its simplicity does not license free damping compensation or a size-independent claim for many independent pairs.

**Anchor and project sources.** [HRB] §2.6.4 and Fig. 15; [Häffner bridge](HAEFFNER_BRIDGE.md); [matching construction, equations (M.10)–(M.13)](../science/matching.md#32-explicit-lossless-upper-construction).

### M15 From conditional loops to the admissible matrix model

**Central question.** How does the single-pair example become a controlled statement for a whole register?

**Understanding target.** Follow the branch evolution $`A(t)z`$, the equivalence of all-branch return and $`A(T)=0`$, and the area formula $`K=\mathrm{Im}\int A^\dagger\dot A`$. Integration by parts makes $`K`$ real symmetric. Independent complex controls realize any admitted $`H_0^1`$ path through $`u=\dot A+\kappa A/2`$.

**Earlier dependencies and story role.** [M07](#m07-normal-modes-addressability-and-physical-controls), [M10](#m10-closed-trajectories-fourier-modes-and-variational-spectra), [M13](#m13-the-complete-architecture-question), and [M14](#m14-a-fully-paid-single-cz-loop) establish the general model behind the example.

**Conceptual connection.** An interaction-picture description does not grant uncharged direct two-qubit gates, bus squeezing, or intermediate noncommuting spin controls. These would change the feasible set.

**Anchor and project sources.** [HRB] §§2.2, 2.6.4, and 3.3; [model, §§1–2](../science/model.md#1-dynamics-and-admissible-controls), equations (M1)–(M8).

### M16 The geometric phase-exposure bound and its limits

**Central question.** What control cost is unavoidable before the finite number of buses is considered?

**Understanding target.** Relate the real block Gram matrix to $`E_{\rm mat}\succeq KF^+K`$ and $`EX\geq\Vert K\Vert _*^2`$. A rotated-path Dirichlet argument strengthens the scalar bound to $`E\geq\Vert K\Vert _*^2/X+\pi^2X/T^2`$. The explicit two-column counterexample shows why the finite-time term cannot generally be added as a matrix-order inequality.

**Earlier dependencies and story role.** [M09](#m09-real-gram-matrices-and-spectral-matrix-tools), [M10](#m10-closed-trajectories-fourier-modes-and-variational-spectra), [M12](#m12-a-complete-ledger-of-control-resources), and [M15](#m15-from-conditional-loops-to-the-admissible-matrix-model) provide the first universal resource converse.

**Conceptual connection.** A nuclear-norm trace bound controls total geometric demand but does not yet charge the limited multiplicity of low-cost temporal directions.

**Anchor and project sources.** [HRB] §2.6.4 provides the area interpretation; the inequalities and counterexample are project derivations in [spectral cost, §4](../science/spectral_cost.md#4-phaseexposureenergy-inequalities), equations (SC.14)–(SC.16).

### M17 The temporal capacity of a finite bus

**Central question.** Why does using more temporal directions make a fixed number of buses more expensive?

**Understanding target.** Follow the closed Fourier expansion $`A(t)=\sum_{k\ne0}V_k(e^{2\pi ikt/T}-1)`$, including the convergence needed for endpoint values and area integrals. Each signed harmonic has a positive semidefinite real Gram matrix of rank at most $`2b`$; the sign of $`k`$ determines the sign of its area contribution. Its area magnitude scales with $`\vert k\vert `$, while derivative action scales with $`k^2`$.

**Earlier dependencies and story role.** [M09](#m09-real-gram-matrices-and-spectral-matrix-tools), [M10](#m10-closed-trajectories-fourier-modes-and-variational-spectra), and [M15](#m15-from-conditional-loops-to-the-admissible-matrix-model) expose the mechanism absent from the trace-only bound.

**Conceptual connection.** Two real quadratures per complex bus and separate positive/negative harmonics determine capacity. Adding a temporal tone spends control action without increasing the count of physical oscillators.

**Anchor and project sources.** [HRB] §2.6.1 supplies the physical-mode comparison; [Fourier reduction](../science/spectral_cost.md#21-fourier-representation-including-the-endpoint-issue), equations (SC.6)–(SC.8), supplies the temporal argument.

### M18 The exact fixed-matrix spectral optimum

**Central question.** How is a desired phase spectrum assigned to the cheapest available temporal directions?

**Understanding target.** Read the separately ordered positive and negative eigenvalue lists in $`\Phi_b(K)`$ and understand the exact formula $`E_{\min}T=2\pi\Phi_b(K)`$. Low-frequency rank limits force eigenvalue-tail costs; packing at most $`2b`$ real eigenvectors into each signed harmonic attains the lower bound.

**Earlier dependencies and story role.** [M09](#m09-real-gram-matrices-and-spectral-matrix-tools) and [M17](#m17-the-temporal-capacity-of-a-finite-bus) convert the temporal mechanism into a sharp fixed-$`K`$ theorem.

**Conceptual connection.** This is an application of inherited weighted spectral control geometry. It establishes an exact optimum for a specified full matrix, while a quantum gate still admits diagonal completions and different phase representatives.

**Anchor and project sources.** [HRB] §§2.6.1 and 2.6.4 provide physical context; [Theorem SC1 and attainment](../science/spectral_cost.md#2-fixed-matrix-optimum); [Wong–Baillieul, Brockett, and Rizzi–Serres attribution](../references/related_work.md#2-the-spectral-control-mathematics-is-inherited).

### M19 The sharp cost of a cross block

**Central question.** Which part of the spectral cost survives freedom in the rest of the phase matrix?

**Understanding target.** For $`C=K_{\mathcal{A}\mathcal{B}}`$, connect symmetric nuclear-norm duality and best low-rank approximation to $`\Phi_b(K)\geq2\sum_j\lceil j/(4b)\rceil\sigma_j(C)`$. The factor $`4b`$ combines the separate signed capacities. Understand the signed rank-one completion that attains equality when both diagonal blocks are free.

**Earlier dependencies and story role.** [M09](#m09-real-gram-matrices-and-spectral-matrix-tools) and [M18](#m18-the-exact-fixed-matrix-spectral-optimum) provide the bridge from a fixed matrix to a gate-level invariant.

**Conceptual connection.** A free diagonal block is not the same as freedom in ordinary diagonal entries. General completions can create same-side interactions; for $`C=cI`$, the attaining completion changes only ordinary diagonal entries and therefore only a global phase.

**Anchor and project sources.** [HRB] §2.6.4 supplies the phase-gate setting; [Theorem SC2 and sharp completion](../science/spectral_cost.md#3-sharp-cross-block-cost) supplies this project specialization.

### M20 Quantum phase equivalence and the odd determinant

**Central question.** Can a different equivalent phase representative remove the matching's required directions?

**Understanding target.** Follow the four-point phase difference that gives the complete lift class $`K_{ij}=\pi\Gamma_{ij}/8+\pi N_{ij}/4`$. For a matching, $`C=(\pi/8)(I+2B)`$ with integer $`B`$. Reduction modulo two makes its determinant odd, so $`\prod_j\sigma_j(C)\geq(\pi/8)^m`$ for every lift.

**Earlier dependencies and story role.** [M01](#m01-local-qubits-and-phase-conventions), [M11](#m11-quadratic-boolean-phases-and-their-modular-ambiguity), [M13](#m13-the-complete-architecture-question), and [M19](#m19-the-sharp-cost-of-a-cross-block) remove the arbitrary choice of phase branch from the converse.

**Conceptual connection.** The result constrains a physical diagonal gate up to the allowed local corrections. It does not assume small matrix entries or bound the number of phase wraps.

**Anchor and project sources.** [HRB] §§2.5 and 2.6.4 provide local/conditional phase context; [Lemma M1 and the determinant argument](../science/matching.md#2-every-exact-phase-lift); [quantum phase-equivalence attribution](../references/related_work.md#3-what-the-quantum-unitary-adds).

### M21 The exact matching sandwich and an attaining family

**Central question.** What remains after the all-lift converse and a physically allowed construction are combined?

**Understanding target.** With $`w_j=\lceil j/(4b)\rceil`$, connect the determinant and weighted arithmetic–geometric mean to the lower bound in Theorem M2, and the construction carrying $`4b`$ pairs per harmonic magnitude to its upper bound. Together they give $`E^*_{m,b}(T)=\Theta((m+m^2/b)/T)`$. For $`m\leq4b`$, both bounds equal $`\pi^2m/(2T)`$.

**Earlier dependencies and story role.** [M14](#m14-a-fully-paid-single-cz-loop), [M19](#m19-the-sharp-cost-of-a-cross-block), and [M20](#m20-quantum-phase-equivalence-and-the-odd-determinant) establish the exact-gate congestion law.

**Conceptual connection.** Exact target synthesis and an exact finite-size optimum are separate claims. The integer-lift optimum is not evaluated in closed form for larger matchings, although the scaling is attained.

**Anchor and project sources.** [HRB] §§2.6.4 and 5.5 provide pair-gate context; [Theorem M2 and explicit construction](../science/matching.md#3-exact-matching-cost-including-all-lifts), equations (M.6)–(M.16).

### M22 From integrated action to physical force caps

**Central question.** Which gate-duration law follows from a total cap, and which requires an individual-cap construction?

**Understanding target.** Combine the action converse with $`E\leq PT`$ at zero loss. The explicit matching controls have constant total power and individual powers $`\pi^2k_j/(4T^2)`$. Their separate peak analysis gives $`T_{\min}=\Theta(g^{-1}\sqrt{1+m/b})`$ when every qubit obeys $`\sum_\mu\vert u_{\mu i}\vert ^2\leq g^2`$.

**Earlier dependencies and story role.** [M12](#m12-a-complete-ledger-of-control-resources), [M13](#m13-the-complete-architecture-question), and [M21](#m21-the-exact-matching-sandwich-and-an-attaining-family) turn the control theorem into the first architecture conclusion.

**Conceptual connection.** Increasing available modes does not increase the allowed total drive per qubit. Collective low-rank entangling phases can have a different duration law from independent matchings.

**Anchor and project sources.** [HRB] §§2.7, 5.5, and 8 provide implementation context; [total and individual caps](../science/matching.md#4-scaling-and-the-two-power-conventions) and [collective-phase comparison](../science/architecture.md#1-independent-gates-and-collective-phases-have-different-costs).

### M23 Unwrapping a nearly correct quadratic gate

**Central question.** Does a small channel error justify comparing ordinary quadratic coefficients despite arbitrary phase wraps?

**Understanding target.** For two diagonal unitary channels, connect half-diamond error $`\epsilon`$ to a phase arc with radius $`\delta=\arcsin\epsilon`$. If $`q=2\pi h+e`$ and $`\vert e\vert \leq\delta\lt \pi/4`$, every third finite difference of the integer-valued $`h`$ vanishes because its magnitude is less than one. Thus $`h`$ is an integer quadratic polynomial, and Walsh/Parseval gives $`\Vert R_{\mathcal{A}\mathcal{B}}\Vert _F\leq\delta/2`$.

**Earlier dependencies and story role.** [M06](#m06-state-fidelity-process-error-and-operational-distance), [M11](#m11-quadratic-boolean-phases-and-their-modular-ambiguity), and [M20](#m20-quantum-phase-equivalence-and-the-odd-determinant) justify the passage from gate accuracy to matrix stability.

**Conceptual connection.** The integer unwrapping and the coefficient-norm bound are distinct steps. A pointwise choice of phase branch alone would not justify the second.

**Anchor and project sources.** [HRB] §§2.6.4 and 4.7 motivate phase gates and process accuracy; the phase arc, finite differences, and Walsh argument are project derivations in [Lemma M3 and matching §5](../science/matching.md#5-uniform-phase-unwrapping-on-the-boolean-cube).

### M24 A positive congestion bound at every size

**Central question.** How does the exact matching converse survive a bounded coefficient residual?

**Understanding target.** Apply singular-value stability to the unwrapped cross block. With $`\eta=4\delta/\pi\lt 1`$, distinguish the weighted determinant lower bound from the positive term $`m-\eta\sqrt m`$. Their combination yields the all-size bound $`E\geq\pi^2(1-\eta)(m+m^2/b)/(60T)`$ for every $`m,b\geq1`$.

**Earlier dependencies and story role.** [M09](#m09-real-gram-matrices-and-spectral-matrix-tools), [M21](#m21-the-exact-matching-sandwich-and-an-attaining-family), and [M23](#m23-unwrapping-a-nearly-correct-quadratic-gate) establish fixed-error congestion with explicit finite-size control.

**Conceptual connection.** An increasing weighted singular-value function is not assumed to be a norm. Stability uses the Frobenius perturbation inequality, and the number $`30`$ appearing inside one proof is not a restriction on the theorem's system size.

**Anchor and project sources.** [HRB] §4.7 gives accuracy context only; [Theorem M4](../science/matching.md#6-explicit-finite-error-lower-bounds-positive-for-every-m), including equations (M.28)–(M.35), supplies the bound and its unitary threshold $`\epsilon\lt 1/\sqrt2`$.

### M25 The exact lossy channel and its skew phase

**Central question.** Which spin channel is actually implemented by a closed damped bus?

**Understanding target.** Follow the coherent-output dilation with $`\beta_z=\sqrt\kappa\,Az`$. The overlap gives attenuation governed by $`F=\mathrm{Re}\int A^\dagger A`$ and a phase $`\kappa z'^{\mathsf{T}}Jz`$, with $`J=\mathrm{Im}\int A^\dagger A`$ antisymmetric. The resulting Schur multiplier is completely positive because it is an environment Gram matrix.

**Earlier dependencies and story role.** [M05](#m05-an-open-bus-leaves-an-environmental-record), [M06](#m06-state-fidelity-process-error-and-operational-distance), [M09](#m09-real-gram-matrices-and-spectral-matrix-tools), and [M15](#m15-from-conditional-loops-to-the-admissible-matrix-model) identify the actual operation needed for noisy claims.

**Conceptual connection.** The skew phase generally cannot be removed by one diagonal Hamiltonian correction. When $`J=0`$, Gaussian dephasing is available; diagonal $`F`$ permits independent dephasing. Correlated noise is therefore not asserted to be unavoidable.

**Anchor and project sources.** [HRB] §§3.2–3.3 motivate open motion; [exact channel, equations (L2)–(L4)](../science/loss_and_frontier.md#1-exact-channel-including-the-imaginary-trajectory-gram-matrix); [Louis and Müller–Luoma–Strunz attribution](../references/related_work.md#5-dissipation-known-mechanism-paid-resource-frontier).

### M26 What channel accuracy forces on phase and exposure

**Central question.** How can the actual noisy channel constrain both the geometric gate and its environmental record?

**Understanding target.** For a diagonally dressed matching target, fixing a reference string makes the skew bath phase linear in the other string. Two-branch input states then give a phase radius $`\delta=\arcsin(2\epsilon)`$, so the same unwrapping works for $`\epsilon\lt 1/(2\sqrt2)`$. Separately, an antipodal superposition gives the target-independent floor $`\epsilon\geq(1-e^{-2\kappa X})/2`$ relative to any unitary.

**Earlier dependencies and story role.** [M06](#m06-state-fidelity-process-error-and-operational-distance), [M23](#m23-unwrapping-a-nearly-correct-quadratic-gate), [M24](#m24-a-positive-congestion-bound-at-every-size), and [M25](#m25-the-exact-lossy-channel-and-its-skew-phase) extend the converse to implemented noisy gates.

**Conceptual connection.** The reference-dependent linear term is a proof device, not a correction that removes all bath phases. The antipodal argument constrains purity and remains valid even when the target's geometric phase differs from the realized $`K`$.

**Anchor and project sources.** [HRB] §§3.2 and 4.7 provide noise/process context; [Theorem M5](../science/matching.md#7-direct-robustness-for-the-implemented-lossy-channel) and [the operational loss floor, equations (L5)–(L6)](../science/loss_and_frontier.md#a-nonperturbative-floor-relative-to-any-unitary-target).

### M27 The damped area spectrum and paid action

**Central question.** What changes in the exact spectral optimum when maintaining a closed path itself costs force?

**Understanding target.** Follow the area operator relative to the cost $`E+\lambda X`$. Its Dirichlet eigenfunctions are $`e^{\pm i\omega_kt}\sin(k\pi t/T)`$, with $`\omega_k=\sqrt{(k\pi/T)^2+\lambda}`$ and signed real multiplicity $`2b`$. Rank allocation with these new weights gives the exact priced optimum. Setting $`\lambda=\kappa^2/4`$ gives the minimum paid action $`G`$.

**Earlier dependencies and story role.** [M10](#m10-closed-trajectories-fourier-modes-and-variational-spectra), [M12](#m12-a-complete-ledger-of-control-resources), [M18](#m18-the-exact-fixed-matrix-spectral-optimum), and [M25](#m25-the-exact-lossy-channel-and-its-skew-phase) extend the inherited spectral engine to compensated loss.

**Conceptual connection.** The complete spectrum and explicit attaining paths prove an integrated-action optimum. A separate peak-force constraint is not automatically satisfied at the value $`G/T`$.

**Anchor and project sources.** [HRB] §§2.6.4 and 3.3 motivate controlled damped trajectories; [area spectrum and priced optimum](../science/loss_and_frontier.md#3-spectrum-of-the-closed-loop-area-operator), equations (L11)–(L20); [mathematical attribution](../references/related_work.md#2-the-spectral-control-mathematics-is-inherited).

### M28 The complete fixed-matrix exposure frontier

**Central question.** Which action–exposure tradeoffs are optimal when the full phase matrix and time are fixed?

**Understanding target.** Introduce an exposure price $`\mu\geq0`$ through $`\lambda=\kappa^2/4+\mu`$. The supporting function gives $`X(\mu)=S'(\mu)`$ and $`G(\mu)=S(\mu)-\mu X(\mu)`$, with explicit attaining controls. Monotonicity and domination show that this parameterization covers every nondominated $`(G,X)`$ pair for fixed $`K,T,b,\kappa`$.

**Earlier dependencies and story role.** [M16](#m16-the-geometric-phase-exposure-bound-and-its-limits), [M25](#m25-the-exact-lossy-channel-and-its-skew-phase), and [M27](#m27-the-damped-area-spectrum-and-paid-action) complete the exact scalar resource optimization.

**Conceptual connection.** For nonzero $`K`$, as exposure tends to zero, action and phase-rotation rate diverge; asymptotically $`GX\to\Vert K\Vert _*^2`$. An exposure optimum is not a diamond-error optimum, and it does not minimize over gate-equivalent phase lifts.

**Anchor and project sources.** [HRB] §§3.2 and 8 motivate the coherence/control tradeoff; [complete fixed-$`K`$ frontier](../science/loss_and_frontier.md#5-paid-damping-and-the-complete-fixed-k-exposure-frontier), equations (L21)–(L23), and its scope discussion.

### M29 A paid architecture comparison with global accuracy

**Central question.** What do the proved resource laws imply when force, duration, and whole-layer accuracy are budgeted together?

**Understanding target.** For $`\kappa\gt 0`$, $`0\lt \epsilon\lt 1/(2\sqrt2)`$, and $`\delta=\arcsin(2\epsilon)`$, combine the robust bound $`\Vert K\Vert _*\geq\pi m/4-\delta\sqrt m`$, the exposure ceiling from M26, and $`G\leq PT`$ to obtain
$`T\geq2\kappa(\pi m/4-\delta\sqrt m)^2/[P(-\log(1-2\epsilon))]`$.
Interpret the peak-constrained damped example and the two figure panels with their distinct optimization domains.

**Earlier dependencies and story role.** [M22](#m22-from-integrated-action-to-physical-force-caps), [M24](#m24-a-positive-congestion-bound-at-every-size), [M26](#m26-what-channel-accuracy-forces-on-phase-and-exposure), and [M28](#m28-the-complete-fixed-matrix-exposure-frontier) join ideal congestion to a separately paid global noise requirement.

**Conceptual connection.** More modes can improve lossless parallelism without guaranteeing a chosen global accuracy. Modulation, growing branch occupation, initial preparation, and data-memory noise remain explicit resources. A lower error bound for a pulse family is not its exact error.

**Anchor and project sources.** [HRB] §§2.7, 3.2, and 6–8 provide architecture context; [global accuracy consequence](../science/architecture.md#2-a-global-accuracy-constraint-from-loss), [resource examples](../science/architecture.md#3-two-resource-comparisons), and [finite verification](../verification/README.md).

### M30 The complete scoped architecture story

**Central question.** What does finite-bus congestion establish about an architecture, and where do its conclusions stop?

**Understanding target.** Connect the conditional-area primitive to temporal multiplicity, the inherited spectral optimum to all quantum phase representatives, and phase unwrapping to fixed-error congestion. Join that lossless attainable law with the actual noisy-channel converse and the exact fixed-matrix exposure frontier. The resulting account identifies what is possible, what is necessary, and which assumptions support each statement.

**Earlier dependencies and story role.** [M13](#m13-the-complete-architecture-question), [M21](#m21-the-exact-matching-sandwich-and-an-attaining-family), [M24](#m24-a-positive-congestion-bound-at-every-size), [M28](#m28-the-complete-fixed-matrix-exposure-frontier), and [M29](#m29-a-paid-architecture-comparison-with-global-accuracy) supply the complete synthesis.

**Conceptual connection.** Fixed per-qubit coupling requires $`b=\Omega(m)`$ for constant-duration independent matching in the lossless model; global loss accuracy adds a mode-independent necessary cost. Neither statement covers unrestricted processors, nonlinear or encoded buses, intermediate noncommuting controls, approximate return, or fault tolerance without new analysis. Mathematical attribution, analytic proofs, finite numerical checks, and hardware evidence retain their separate roles.

**Anchor and project sources.** [HRB] §8 supplies the broader architecture perspective; [scientific reading map](../science/README.md), [complete model](../science/model.md), [architecture conclusions](../science/architecture.md#6-what-follows-for-architecture), [related work and claim boundaries](../references/related_work.md), and [verification limits](../verification/README.md).
