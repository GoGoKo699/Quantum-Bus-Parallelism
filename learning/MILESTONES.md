# Thirty milestones for quantum bus parallelism

This map follows one scientific question: what force action and duration are required to implement many independent entangling pairs through a finite number of harmonic bus modes? It connects the physical gate mechanism to the spectral control cost, the converse for physically equivalent gates, the matching construction, and the interpretation for hardware, including the force and exposure paid under vacuum loss.

The single educational anchor is H. Häffner, C. F. Roos, and R. Blatt, *Quantum computing with trapped ions* (2008), using [arXiv:0809.4368v1](https://arxiv.org/abs/0809.4368v1). The [Häffner bridge](HAEFFNER_BRIDGE.md) translates its physical language into this project's notation and assumptions. The review supplies the trapped-ion and geometric-gate foundation. The project's canonical science pages supply the spectral optimization, phase-wrap, and channel-error arguments, with their own research references.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. Twelve establish the common language of conditional motion, phase matrices, force resources, and gate error. Eighteen connect the longer argument needed to make a control bound apply to an actual gate under phase equivalence and nonzero error, then connect it to an achievable construction and its physical limits. Each phase moves from individual objects and mechanisms to an integrated account; M12 and M30 are its synthesis milestones.

| Phase | Range | Local-to-global route |
|---|---|---|
| Background/preliminaries | M01–M12 | One spin and oscillator → collective modes and closed conditional paths → phase, resource, and error language → the complete architectural question. |
| Narrative/innovation | M13–M30 | One Fourier contribution → spectral and physical-gate converses → fixed-error robustness → parallel construction → architectural meaning and scope. |

## Shared notation and authoritative assumptions

There are $`K`$ disjoint target pairs on $`2K`$ qubits, $`m`$ canonical harmonic modes, and a pulse duration $`T`$. The effective complex forces are $`u_{j\ell}(t)`$, their paths are $`\alpha_{j\ell}(t)`$, and the closed-loop spin gate is $`U_A=\exp(iZ^{\mathsf T}AZ)`$. Force fluence is $`\mathcal E=\int\sum_{j,\ell}|u_{j\ell}|^2dt`$, and action is $`T\mathcal E`$. The force-limited problem uses a per-qubit bound $`\sum_\ell|u_{j\ell}|^2\le g^2`$. The layer error $`\epsilon`$ is half the diamond norm after optimizing final local $`Z`$ corrections.

The [model](../science/model.md#hamiltonian-and-exact-closure), [gate-equivalence definition](../science/model.md#target-and-physical-gate-equivalence), and [resource definitions](../science/model.md#charged-resources-and-optimization-problems) are authoritative throughout. In particular, the force axes commute during the evolution and every conditional path closes exactly. The fixed-error result changes the allowed spin-gate error while retaining exact bus closure. Source pointers below identify the relevant proof sections rather than reproduce their derivations.

The converse-and-construction route through M26 concerns the lossless unitary model. M27–M30 also follow the [vacuum-loss continuation](../science/model.md#vacuum-loss-extension-and-exposure), which assumes vacuum initial modes and input fields, common Markov damping, and exactly closed actual damped paths. There the mode-first trajectory matrix is $`D_{\ell j}=\alpha_{j\ell}`$, exposure is $`X=\int_0^T\lVert D\rVert_F^2dt`$, and the paid force fluence includes damping compensation. The noisy-channel converse and fixed-matrix resource frontier have their own scope; neither supplies a noisy analogue of the lossless matching upper bound.

## Phase I — Background and preliminaries

### M01 — A qubit, a basis state, and a phase

**Central question:** How can an operation change a quantum state while leaving its computational-basis label unchanged?

**Understanding target:** Explain the two-level qubit, the signs $`z_j=\pm1`$ of a Pauli-$`Z`$ eigenstate, and the distinction between a relative phase of a superposition and an overall phase. Relate this language to a gate diagonal in the computational basis.

**Dependencies and story role:** No earlier milestone is required. This is the local spin description on which the conditional-force model is built.

**Conceptual connection:** The review's internal ionic states become the project's spin labels; their phases, rather than changes of population, will encode the entangling operation.

**Source pointers:** Anchor [§2.2, “The basic Hamiltonian”][hrb22] and [§2.6.4, “Geometric phase gate”][hrb264]; project [model, target and physical gate equivalence](../science/model.md#target-and-physical-gate-equivalence); [notation bridge](HAEFFNER_BRIDGE.md).

### M02 — One harmonic mode and its displacement

**Central question:** What does a complex displacement describe about a harmonic oscillator?

**Understanding target:** Connect the oscillator operators $`a,a^\dagger`$, motional occupation, and the two real quadratures of a complex displacement $`\alpha`$. Interpret an effective force $`u(t)`$ as the rate of change of that displacement in the chosen interaction picture.

**Dependencies and story role:** Builds on M01 by adding the local physical mediator. It supplies the objects whose trajectories will generate spin phases.

**Conceptual connection:** Quantized ion motion provides the physical example; complex paths provide the mathematical description shared by motional and resonator buses.

**Source pointers:** Anchor [§2.2][hrb22]; project [spectral cost §1, control class and normalization](../science/spectral_cost.md#1-control-class-and-normalization) and [hardware resources §1, force quadratures](../science/hardware_resources.md#1-converting-a-laboratory-coupling-to-the-force-norm); [bridge](HAEFFNER_BRIDGE.md).

### M03 — Normal modes and the number of mediators

**Central question:** What is being counted when a device has $`m`$ bus modes?

**Understanding target:** Distinguish an individual ion's motion from a collective normal mode, and a canonical oscillator degree of freedom from a control channel or modulation tone. Explain why a single waveform can interact with several modes.

**Dependencies and story role:** Uses M02 and enlarges the physical setting from one oscillator to a shared multimode mediator.

**Conceptual connection:** The normal-mode description fixes the meaning of the architectural variable $`m`$ before any resource comparison is made.

**Source pointers:** Anchor [§2.6.1, “Motion of ion strings”][hrb261]; project [hardware resources §2, which modes and controls count](../science/hardware_resources.md#2-which-modes-and-controls-count) and [model, Hamiltonian](../science/model.md#hamiltonian-and-exact-closure).

### M04 — From a physical drive to a commuting conditional force

**Central question:** Which physical couplings are represented by the project's force Hamiltonian?

**Understanding target:** Explain how an effective drive can exert different forces for different spin states, why an interaction picture is useful, and what it means to keep each spin's coupling axis fixed. Recognize that a rotating-wave or Lamb–Dicke approximation is part of a physical model's justification.

**Dependencies and story role:** Combines the spin, oscillator, and mode descriptions of M01–M03 into the local interaction mechanism.

**Conceptual connection:** The Mølmer–Sørensen and geometric-gate discussions motivate the effective description; the project grants independent complex forces as a specified control class.

**Source pointers:** Anchor [§2.2][hrb22], [§2.6.3, “Mølmer-Sørensen gate”][hrb263], and [§2.6.4][hrb264]; project [model, Hamiltonian and closure](../science/model.md#hamiltonian-and-exact-closure) and [hardware resources §1](../science/hardware_resources.md#1-converting-a-laboratory-coupling-to-the-force-norm); [bridge](HAEFFNER_BRIDGE.md).

### M05 — A closed path leaves a spin phase

**Central question:** How can an oscillator return to its starting displacement while mediating an entangling operation?

**Understanding target:** Relate a closed conditional path to its oriented phase-space area and the accumulated phase. Explain how the force depends on a joint spin configuration and how the resulting phase can contain a two-spin term.

**Dependencies and story role:** Uses M02 and M04. It identifies the local geometric mechanism before considering how many independent interactions it can support.

**Conceptual connection:** Motional mediation becomes a spin gate through path-dependent phase accumulation; the project's area integral makes that mechanism quantitative.

**Source pointers:** Anchor [§2.6.4][hrb264]; project [model, Eq. (4)](../science/model.md#hamiltonian-and-exact-closure) and [spectral cost §1, Eqs. (3)–(4)](../science/spectral_cost.md#1-control-class-and-normalization).

### M06 — Exact closure and its physical limits

**Central question:** What does it mean to return the bus for every possible spin input?

**Understanding target:** Explain why each qubit–mode path must close, so every spin-conditioned sum of paths closes. Separate the ideal gate's independence of the initial oscillator state from heating, loss, nonlinear motion, and the validity range of a harmonic approximation.

**Dependencies and story role:** Uses M03–M05 and turns a one-path picture into a condition on the entire spin–bus evolution.

**Conceptual connection:** Closure removes final spin–bus entanglement in the model; motional coherence remains a distinct physical requirement during the trajectory.

**Source pointers:** Anchor [§2.6.4][hrb264] and [§3.2, “Motional coherence”][hrb32]; project [model, exact closure](../science/model.md#hamiltonian-and-exact-closure) and [hardware resources §4](../science/hardware_resources.md#4-oscillator-excursion-and-noise-exposure).

### M07 — The phase matrix and a target pair

**Central question:** How does a real symmetric matrix specify the spin gate produced by closed paths?

**Understanding target:** Read $`Z^{\mathsf T}AZ`$ as a quadratic phase: an off-diagonal entry contributes $`2A_{ij}Z_iZ_j`$, while the diagonal contributes only a global phase. Identify $`A_{A_jB_j}=\pi/8`$ as the preferred representative of one target $`ZZ(\pi/4)`$ gate.

**Dependencies and story role:** Uses M01, M05, and M06. It collects many geometric phases into the matrix that carries the rest of the argument.

**Conceptual connection:** The factor of two and the diagonal freedom connect a control calculation to the actual quantum operation.

**Source pointers:** Anchor [§2.6.3, conditional-phase interpretation][hrb263] and [§2.6.4][hrb264]; project [spectral cost §1](../science/spectral_cost.md#1-control-class-and-normalization) and [model, target gate](../science/model.md#target-and-physical-gate-equivalence).

### M08 — Independent directions in a phase matrix

**Central question:** What do eigenvalues, singular values, and rank reveal about a collection of interactions?

**Understanding target:** Interpret a real symmetric matrix as a sum of signed orthogonal rank-one contributions. Distinguish the sign of an eigenvalue from its magnitude, and recognize singular values as the nonnegative magnitudes used for the generally nonsymmetric matching cross block.

**Dependencies and story role:** Uses M07. It supplies the matrix language for counting and charging independent phase directions.

**Conceptual connection:** A collective spin phase and a collection of independently specified pair phases can have different spectral requirements even when both involve many qubits.

**Source pointers:** Project [spectral cost §2, spectral notation](../science/spectral_cost.md#2-exact-minimum-for-a-prescribed-full-matrix), [§3, singular values](../science/spectral_cost.md#3-a-bound-in-terms-of-singular-values), and [model, physical interpretation](../science/model.md#physical-interpretation-and-scope). These matrix prerequisites are supplied by the project rather than attributed to the review.

### M09 — Waveforms, force fluence, and time rescaling

**Central question:** Which resource stays fixed when a closed-loop pulse is stretched in time?

**Understanding target:** Distinguish force amplitude, integrated squared force $`\mathcal E`$, action $`T\mathcal E`$, and oscillator occupation. Explain how inverse amplitude scaling preserves the phase and action under a time stretch, and how a Fourier harmonic labels temporal structure within a pulse.

**Dependencies and story role:** Uses M02, M05, and M07. It establishes the resource and waveform language needed for a duration law.

**Conceptual connection:** A gate phase is geometric, whereas the conversion from action to duration depends on the allowed force norm. Fourier tones organize controls without changing the number of physical modes.

**Source pointers:** Project [model, charged resources](../science/model.md#charged-resources-and-optimization-problems), [spectral cost §2.1](../science/spectral_cost.md#21-fourier-representation-for-the-entire-control-class), and [hardware resources, resource table](../science/hardware_resources.md).

### M10 — A physical gate has many phase representatives

**Central question:** Why can different real phase matrices implement the same allowed gate?

**Understanding target:** Distinguish global phases, free final local $`Z`$ rotations, and genuinely different entangling phases. Understand the diagonal freedom and the elementary identity that makes an off-diagonal shift by $`\pi/4`$ a local correction up to global phase.

**Dependencies and story role:** Uses M01 and M07. It identifies the optimization domain before the project tries to bound its cost.

**Conceptual connection:** A resource bound for one chosen logarithm of a unitary must be extended to all physically equivalent representatives.

**Source pointers:** Anchor [§2.6.3, basis and phase conventions][hrb263]; project [spectral cost §4, phase matrix versus physical gate](../science/spectral_cost.md#4-a-phase-matrix-and-a-physical-gate-have-different-optimization-domains) and [model, local corrections](../science/model.md#target-and-physical-gate-equivalence).

### M11 — Error for the entire coherent gate layer

**Central question:** What does a fixed error tolerance for a layer of gates actually constrain?

**Understanding target:** Interpret half-diamond distance as worst-case channel distinguishability, including a reference system. Distinguish a bound on the full layer from separate per-pair errors or average fidelity, and retain exact bus closure as a separate hypothesis.

**Dependencies and story role:** Uses M06, M07, and M10. It completes the accuracy specification required for a robust architectural statement.

**Conceptual connection:** The relevant approximation is closeness of physical quantum channels; it does not initially require closeness of any chosen real phase matrices.

**Source pointers:** Project [model, Eq. (7) and error discussion](../science/model.md#target-and-physical-gate-equivalence) and [gate-layer bounds §3, channel-error convention](../science/gate_layer_bounds.md#3-half-diamond-error-gives-a-uniform-phase-lift). The channel metric and its research references are supplied there, not in the selected review.

### M12 — Background synthesis: the finite-bus architectural question

**Central question:** What is the complete problem once the mechanism, resources, and success criterion are specified?

**Understanding target:** Connect $`K`$ disjoint maximally entangling pairs, $`m`$ canonical modes, commuting independently controlled forces, exact closure, allowed local phases, and whole-layer error into one optimization problem. Explain why the existence of parallel gates leaves a further question about their force action and duration.

**Dependencies and story role:** Integrates M01–M11 and closes the background phase. The next phase can now ask which cost is unavoidable and which controls achieve the same order.

**Conceptual connection:** The review's simultaneous-pair example supplies a concrete physical precedent; the project asks a quantified resource question across varying pair and mode counts.

**Source pointers:** Anchor [§5.5, “Entanglement purification,” simultaneous pair operations][hrb55]; project [model, architectural question](../science/model.md#the-architectural-question), [optimization definitions](../science/model.md#charged-resources-and-optimization-problems), and [Häffner bridge](HAEFFNER_BRIDGE.md).

## Phase II — Narrative and innovation

### M13 — The phase directions supplied by one Fourier harmonic

**Central question:** How many independent real phase directions can one signed harmonic contribute?

**Understanding target:** Explain why a complex coefficient $`v=x+iy`$ contributes $`\mathrm{Re}(vv^\dagger)=xx^{\mathsf T}+yy^{\mathsf T}`$, so each mode supplies two real directions. Track the independent positive and negative harmonics and the resulting $`2m`$ directions per sign.

**Dependencies and story role:** Uses M08, M09, and M12. It begins the project argument with the local contribution of one waveform component.

**Conceptual connection:** Force quadratures become spectral capacity, with the harmonic sign fixing the sign of the area contribution.

**Source pointers:** Project [spectral cost §2.1, Eqs. (11)–(12)](../science/spectral_cost.md#21-fourier-representation-for-the-entire-control-class) and [§2.3, signed contributions](../science/spectral_cost.md#23-signed-contributions-and-the-lower-bound).

### M14 — Why higher spectral directions carry higher cost

**Central question:** Why does finite capacity at each harmonic produce staircase weights in the action?

**Understanding target:** Explain the positive-decomposition lemma: the first few harmonics can cover only a limited-dimensional subspace, leaving spectral weight in later tails. Understand why summing these tails yields weights $`\lceil r/(2m)\rceil`$ without assuming a special decomposition.

**Dependencies and story role:** Uses M08 and M13. It turns the local harmonic capacity into a lower bound covering arbitrary positive spectral decompositions.

**Conceptual connection:** Limited dimensional capacity becomes a quantitative cost on eigenvalue magnitudes, rather than just a count of nonzero directions.

**Source pointers:** Project [spectral cost §2.2, Lemma 2 and its proof](../science/spectral_cost.md#22-a-weighted-positive-decomposition-lemma); [§5, connection to classical spectral area costs](../science/spectral_cost.md#5-relation-to-the-classical-spectral-area-problem).

### M15 — Exact cost for a prescribed full matrix

**Central question:** How do the positive and negative contributions combine into an exact control theorem?

**Understanding target:** Connect the separate weighted spectra to $`\mathcal E_{\min}=2\pi\Phi_m(A)/T`$. Explain why arbitrary sign cancellation cannot beat the lower bound, why finite harmonic controls attain it, and why the theorem covers the whole square-integrable control class.

**Dependencies and story role:** Combines M13 and M14 into the first global control result. M10 identifies the additional optimization still needed for a physical gate.

**Conceptual connection:** A complete variational statement supplies both a universal lower bound and an explicit realization for each fixed matrix.

**Source pointers:** Project [spectral cost §2, Theorem 1](../science/spectral_cost.md#2-exact-minimum-for-a-prescribed-full-matrix), [§2.3](../science/spectral_cost.md#23-signed-contributions-and-the-lower-bound), and [§2.4, attainment](../science/spectral_cost.md#24-attainment-with-finitely-many-harmonics).

### M16 — Matching gates impose an integer-parity constraint

**Central question:** What constraint survives every allowed phase representative of the target layer?

**Understanding target:** Explain why Boolean mixed differences remove local phases and force the matching cross block to have the form $`C=(\pi/8)(I+2M)`$ with integer $`M`$. Interpret reduction modulo two as a constraint shared by all exact representatives.

**Dependencies and story role:** Uses M07, M10, and M15. It transfers the discussion from a prescribed matrix to the entire physical-gate equivalence class.

**Conceptual connection:** An unobservable choice of logarithm becomes controlled by an arithmetic invariant of the cross block.

**Source pointers:** Project [gate-layer bounds §2, exact phase wraps](../science/gate_layer_bounds.md#2-exact-gates-force-an-odd-determinant-cross-block) and [spectral cost §4, equivalence class](../science/spectral_cost.md#4-a-phase-matrix-and-a-physical-gate-have-different-optimization-domains).

### M17 — From an odd determinant to the exact gate converse

**Central question:** How does the parity constraint force a minimum action even for badly conditioned representatives?

**Understanding target:** Connect the nonzero odd determinant of $`I+2M`$ to a lower bound on the product of singular values of $`C`$. Combine singular-value compression and weighted arithmetic–geometric mean to understand $`\mathcal ET\ge(\pi^2/4)KG_{K,m}`$, where $`G_{K,m}`$ is the geometric mean of $`w_r=\lceil r/(4m)\rceil`$.

**Dependencies and story role:** Combines M08, M15, and M16 into the exact physical-gate lower bound.

**Conceptual connection:** The invariant controls the collective spectral cost without requiring every singular value to be individually large.

**Source pointers:** Project [spectral cost §3, merged singular-value bound](../science/spectral_cost.md#3-a-bound-in-terms-of-singular-values) and [gate-layer bounds §§1–2](../science/gate_layer_bounds.md#1-statement-and-spectral-input).

### M18 — Small channel error gives one short phase arc

**Central question:** How can an error bound on unitary channels constrain every relative eigenphase at once?

**Understanding target:** Explain the convex-hull description of unitary-channel distance and the role of a global phase in centering the relative spectrum. Understand the conversion from half-diamond error $`\epsilon`$ to a uniform phase radius $`\delta=\arcsin\epsilon`$.

**Dependencies and story role:** Uses M10, M11, and M17. It begins the fixed-error extension at the physically meaningful channel level.

**Conceptual connection:** Worst-case coherent error becomes a simultaneous bound on a real residual phase over the entire Boolean cube.

**Source pointers:** Project [gate-layer bounds §3, spectral-arc lemma](../science/gate_layer_bounds.md#3-half-diamond-error-gives-a-uniform-phase-lift) and its primary channel-metric reference; [model, error definition](../science/model.md#target-and-physical-gate-equivalence).

### M19 — Uniformly small error constrains the integer wrap

**Central question:** Why can a nearby physical gate not hide an arbitrary high-degree pattern of phase wraps?

**Understanding target:** Understand the decomposition $`q=2\pi k+r`$ with quadratic $`q`$, integer-valued $`k`$, and bounded $`r`$. Explain how a third Boolean difference and the strict inequality $`8\delta<2\pi`$ force $`k`$ itself to be quadratic.

**Dependencies and story role:** Uses M16 and M18. It restores the arithmetic structure required for the converse at nonzero channel error.

**Conceptual connection:** Discreteness of the integer wraps and uniformity of the residual jointly control a possible discontinuity of the logarithm.

**Source pointers:** Project [gate-layer bounds §4, quadratic integer unwrapping](../science/gate_layer_bounds.md#4-small-uniform-error-forces-quadratic-integer-wraps); [verification guide, strict-threshold example](../verification/README.md#what-is-checked).

### M20 — A global phase bound controls a whole residual matrix

**Central question:** How can a bound on phase values avoid an error penalty growing with the number of matrix entries?

**Understanding target:** Explain how the four-sign difference isolates the cross residual $`R`$ in $`C=(\pi/8)(I+2M)+R`$. Connect the uniform bilinear bound, averaging over independent signs, and $`\lVert R\rVert_F\le\delta/2`$.

**Dependencies and story role:** Uses M08, M18, and M19. It supplies the matrix perturbation control needed for a dimension-sensitive lower bound.

**Conceptual connection:** Whole-layer accuracy controls all cross coefficients together through their squared sum; treating their errors separately would discard that information.

**Source pointers:** Project [gate-layer bounds §4, Eqs. (14)–(17)](../science/gate_layer_bounds.md#4-small-uniform-error-forces-quadratic-integer-wraps) and [verification guide, Boolean gate cases](../verification/README.md#what-is-checked).

### M21 — The robust converse for every pair and mode count

**Central question:** How does the exact determinant argument survive perturbation without assuming well-conditioned phase wraps?

**Understanding target:** Connect Mirsky's singular-value inequality, the Frobenius residual bound, and the weighted error penalty $`\pi\delta\lVert w\rVert_2`$. Explain how $`\lVert w\rVert_2\le KG_{K,m}`$ produces a positive factor $`1-4\arcsin(\epsilon)/\pi`$ for every $`K,m\ge1`$ and fixed $`\epsilon<1/\sqrt2`$.

**Dependencies and story role:** Integrates M17–M20 into the fixed-error physical-gate converse, including its explicit range and constants.

**Conceptual connection:** Magnitude-sensitive spectral control preserves the resource law even when individual singular values become small.

**Source pointers:** Project [gate-layer bounds §5, weighted perturbation](../science/gate_layer_bounds.md#5-a-weighted-singular-value-perturbation-bound), [§6, uniform constants](../science/gate_layer_bounds.md#6-uniform-constants-for-every-k-and-m), and [§1, theorem](../science/gate_layer_bounds.md#1-statement-and-spectral-input).

### M22 — One pair needs only one signed spectral direction

**Central question:** How can diagonal phase freedom reduce the spectral resources of a target pair?

**Understanding target:** Explain why equal forces at a positive harmonic and opposite forces at a negative harmonic each realize the desired cross entry $`\pi/8`$ with a rank-one pair block. Recognize the different diagonal entries as global phase choices.

**Dependencies and story role:** Uses M07, M10, M13, and M15. It starts the constructive side with one physically equivalent pair representative.

**Conceptual connection:** The same equivalence freedom protected against in the converse becomes useful when designing an efficient control.

**Source pointers:** Project [matching construction §1, Eqs. (2)–(6)](../science/matching_construction.md#1-four-real-slots-per-mode-and-harmonic) and [spectral cost §4](../science/spectral_cost.md#4-a-phase-matrix-and-a-physical-gate-have-different-optimization-domains).

### M23 — Packing independent pairs without unwanted couplings

**Central question:** How do the local pair controls combine into an exact parallel layer?

**Understanding target:** Explain cancellation between real and imaginary quadrature slots, independence across modes and signed harmonics, and the allocation of $`4m`$ pairs per harmonic magnitude. Connect this packing to exact closure and action $`(\pi^2/2)\sum_{r=1}^K\lceil r/(4m)\rceil`$.

**Dependencies and story role:** Uses M13 and M22, with M21 supplying the lower-bound comparison. It turns the one-pair mechanism into the matching-order upper construction.

**Conceptual connection:** Orthogonality in control space creates independent interactions even though the pairs share a mediator.

**Source pointers:** Project [matching construction §1](../science/matching_construction.md#1-four-real-slots-per-mode-and-harmonic), [§2, exact action](../science/matching_construction.md#2-exact-action-and-force-limited-duration), and [verification guide, construction and integration checks](../verification/README.md#what-is-checked).

### M24 — Converting the action law into a clock law

**Central question:** What duration follows when each qubit has a fixed total force budget?

**Understanding target:** Explain the lower-bound conversion $`\mathcal E\le2Kg^2T`$ and the constant-magnitude tones of the upper construction. Connect the resulting $`\Theta_\epsilon(\sqrt{1+K/m}/g)`$ duration to the distinct regimes of bounded $`m`$ and $`m`$ proportional to $`K`$.

**Dependencies and story role:** Combines M09, M21, and M23 into the central architectural scaling statement.

**Conceptual connection:** The action theorem becomes a throughput constraint only after the force resource is specified consistently across all modes.

**Source pointers:** Project [gate-layer bounds §7, force-limited clock](../science/gate_layer_bounds.md#7-consequence-for-a-force-limited-clock), [matching construction §2](../science/matching_construction.md#2-exact-action-and-force-limited-duration), and [model, physical interpretation](../science/model.md#physical-interpretation-and-scope).

### M25 — The exact construction's harmonic resources

**Central question:** What additional restrictions follow when only finitely many Fourier harmonics are allowed?

**Understanding target:** Connect the construction's largest harmonic $`L`$ to its highest envelope frequency $`2\pi L/T`$, and understand the exact-gate capacity $`K\le4mL`$. Distinguish finite Fourier support on the pulse interval from a complete physical bandwidth or switching specification.

**Dependencies and story role:** Uses M13, M16, M23, and M24. It exposes a resource assumption behind the matching upper duration.

**Conceptual connection:** The spectral slot count gives an exact capacity statement, while actual waveform-generation limits require a separate physical interpretation.

**Source pointers:** Project [matching construction §3, bandwidth](../science/matching_construction.md#3-bandwidth-of-the-construction), [§5, exact harmonic capacity](../science/matching_construction.md#5-exact-capacity-with-finitely-many-fourier-harmonics), and [hardware resources §3](../science/hardware_resources.md#3-bandwidth-of-the-explicit-upper-construction).

### M26 — Why harmonic capacity is not an approximate rank bound

**Central question:** How can very few spectral directions approximate many pairs without defeating the action converse?

**Understanding target:** Explain how large integer phase wraps can have tiny singular values and a few very large ones. Connect the rank-one approximation to $`(I-2tN)^{-1}`$ with a rank-two full phase matrix, first-harmonic synthesis, small error at fixed $`K`$, and divergent action.

**Dependencies and story role:** Uses M16–M21 and M25. It resolves the apparent tension between exact harmonic capacity and fixed-error synthesis.

**Conceptual connection:** Rank is unstable under approximation; the charged magnitudes of surviving singular values preserve the robust lower bound.

**Source pointers:** Project [gate-layer bounds §8, two-pair shear example](../science/gate_layer_bounds.md#8-why-approximate-rank-is-insufficient) and [matching construction §6, finite-harmonic boundary proposition](../science/matching_construction.md#6-a-boundary-of-the-exact-harmonic-capacity-law).

### M27 — Intermediate excursion and exposure to noise

**Central question:** What happens to the oscillator during an exact parallel gate, before its path closes?

**Understanding target:** Distinguish a single-qubit path from the summed displacement conditioned on an entire spin string. Compare the construction's worst-case excursion bound with its uniform-basis mean occupation, and explain why final closure does not reverse loss of information to an environment.

For the vacuum-loss continuation, interpret $`X`$ as integrated mean occupation and distinguish it from maximum branch occupation. Explain why preserving the same closed path requires $`u=\dot D+\kappa D/2`$ and changes paid fluence to $`\mathcal E=E_{\rm path}+\kappa^2X/4`$. Recognize that the exact reduced channel retains both the real and imaginary parts of $`\int D^\dagger D\,dt`$, so exposure alone does not specify gate error.

**Dependencies and story role:** Uses M02, M06, and M23–M25. It connects the ideal closed-loop construction to the physical demands of its intermediate motion.

**Conceptual connection:** Geometric phase accumulation and endpoint disentanglement coexist with finite excitation and noise exposure during the gate.

**Source pointers:** Anchor [§3.2, motional coherence][hrb32]; project [matching construction §4, displacement bounds](../science/matching_construction.md#4-displacement-and-oscillator-excursion), [§7, compensated damping](../science/matching_construction.md#7-exposure-total-force-and-compensated-damping), [hardware resources §4](../science/hardware_resources.md#4-oscillator-excursion-and-noise-exposure), [exact vacuum-loss channel](../science/loss_and_frontier.md#1-exact-channel-including-the-imaginary-trajectory-gram-matrix), [operational error and exposure](../science/loss_and_frontier.md#2-operational-error-and-first-order-gate-metrics), and [bridge §7, one-pair damping example](HAEFFNER_BRIDGE.md#7-a-closed-loop-with-vacuum-loss).

### M28 — Applying the law to a specified device

**Central question:** What must be identified before the ideal force bound becomes a meaningful hardware statement?

**Understanding target:** Connect physical actuator amplitudes, participation factors, rotating-frame conventions, and the total per-qubit force norm. Explain why a lower bound survives further actuator restrictions, while attaining the ideal upper bound requires the stated quadratures, bandwidth, and mode access; identify when growing normal-mode count changes the scaling regime.

Under the specified vacuum-loss model, distinguish a necessary global loss-duration constraint from an achievable pulse with a checked peak-force cap. Identify preparation, occupation, and data-memory costs that require additional device assumptions.

**Dependencies and story role:** Combines M03, M04, M09, and M24–M27 into a consistent device-level interpretation.

**Conceptual connection:** A permissive control model supports a general converse; hardware calibration determines the variables and the attainability of its upper construction.

**Source pointers:** Anchor [§2.2][hrb22] and [§2.6.1][hrb261]; project [hardware resources §§1–2](../science/hardware_resources.md#1-converting-a-laboratory-coupling-to-the-force-norm), [§5, parameterized resonator example](../science/hardware_resources.md#5-a-parameterized-single-resonator-example), [§6, changes of frame](../science/hardware_resources.md#6-changes-of-frame-and-resources-outside-the-model), [§8, global loss-duration constraint](../science/hardware_resources.md#8-a-global-accuracy-constraint-from-vacuum-loss), [§10, damped pulse with a peak-force cap](../science/hardware_resources.md#10-a-damped-matching-with-an-actual-peak-force-cap), and [§11, preparation and memory](../science/hardware_resources.md#11-preparation-occupation-and-data-memory); [bridge](HAEFFNER_BRIDGE.md).

### M29 — The contribution and the evidence supporting it

**Central question:** Which conclusion follows from each kind of scientific evidence in the repository?

**Understanding target:** Distinguish established geometric gates, prior parallel constructions, and classical spectral-area optimization from the combined all-representative, fixed-error converse. Explain how finite calculations check normalization, waveform cancellation, and examples while the universal statements depend on the analytical proofs.

Apply the same distinction to the established loss mechanism and the project's exact fixed-matrix force–exposure frontier. Separate checks of the full damped channel and frontier formulas from proof of a universal noisy-channel converse or optimization of gate error.

**Dependencies and story role:** Uses M12 and M15–M28. It places the complete result in its mathematical and physical context before the final synthesis.

**Conceptual connection:** Attribution and reproducibility clarify the content and limits of the architectural claim, including why an existing parallel-gate demonstration is compatible with the new converse.

**Source pointers:** Anchor [§5.5, simultaneous-pair precedent][hrb55]; project [related work §§1–2](../references/related_work.md#1-geometric-optimal-control-is-an-antecedent), [§5, scope of the additional converse](../references/related_work.md#5-what-the-additional-converse-establishes), [§6, loss antecedents and paid frontier](../references/related_work.md#6-vacuum-loss-established-mechanism-and-a-paid-frontier), [spectral cost §5](../science/spectral_cost.md#5-relation-to-the-classical-spectral-area-problem), [loss/frontier §6, attribution and boundaries](../science/loss_and_frontier.md#6-attribution-and-remaining-boundaries), and [verification guide](../verification/README.md).

### M30 — Final synthesis: connectivity and independent-pair throughput

**Central question:** What does the complete result establish about an architecture that shares harmonic mediators?

**Understanding target:** Give a connected account from conditional geometric phases through spectral capacity, physical gate equivalence, and fixed-error robustness to the laws $`\mathcal A_\epsilon=\Theta_\epsilon(K+K^2/m)`$ and $`T_\epsilon=\Theta_\epsilon(\sqrt{1+K/m}/g)`$ for fixed $`0\le\epsilon<1/\sqrt2`$. Explain their assumptions, why collective connectivity alone does not determine independent-pair throughput, and how bandwidth, excitation, and device controls qualify the achievable construction.

Keep these lossless scaling laws distinct from necessary bounds for the actual vacuum-loss channel, whose phase-extraction theorem uses $`\epsilon<1/(2\sqrt2)`$ and $`\delta=\arcsin(2\epsilon)`$. Connect the exact paid force–exposure frontier at fixed full $`A,T,m,\kappa`$ to the physical cost of reducing exposure, while explaining why it neither optimizes over all phase-equivalent gates nor gives an exact diamond-error frontier or a matching noisy upper bound.

**Dependencies and story role:** Integrates both phases, especially M12, M21, M24, and M26–M29. It closes the map with the scientific meaning of the whole argument and its stated domain.

**Conceptual connection:** A familiar bus-mediated gate mechanism becomes a quantitative architecture comparison once physical equivalence, accuracy, and charged resources are treated together.

**Source pointers:** [Häffner bridge](HAEFFNER_BRIDGE.md); project [model, exact statements and proof route](../science/model.md#exact-statements-and-proof-route), [gate-layer theorem](../science/gate_layer_bounds.md#1-statement-and-spectral-input), [matching construction](../science/matching_construction.md), [hardware scope](../science/hardware_resources.md#6-changes-of-frame-and-resources-outside-the-model), [direct vacuum-loss converse](../science/gate_layer_bounds.md#10-direct-converse-for-the-vacuum-lossy-channel), [exact fixed-matrix frontier](../science/loss_and_frontier.md#5-paid-damping-and-the-complete-fixed-a-exposure-frontier), and [hardware duration/frontier comparison](../science/hardware_resources.md#9-duration-brackets-and-the-exposure-frontier).

[hrb22]: https://arxiv.org/pdf/0809.4368v1#page=8
[hrb261]: https://arxiv.org/pdf/0809.4368v1#page=22
[hrb263]: https://arxiv.org/pdf/0809.4368v1#page=28
[hrb264]: https://arxiv.org/pdf/0809.4368v1#page=29
[hrb32]: https://arxiv.org/pdf/0809.4368v1#page=45
[hrb55]: https://arxiv.org/pdf/0809.4368v1#page=73
