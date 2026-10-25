# Scientific reading map

The question is how a finite number of harmonic modes can supply many independent entangling gates at bounded force. The account distinguishes exact control cost, physical gate equivalence, whole-layer error, and the additional resources paid under loss.

Throughout, $`K`$ is the number of disjoint pairs, $`m`$ the number of physical oscillator modes, and $`A`$ the real symmetric geometric phase matrix. The actual trajectory coefficients are $`D_{\ell j}(t)=\alpha_{j\ell}(t)`$. The physical paid force fluence is $`\mathcal E`$, its dimensionless action is $`T\mathcal E`$, the derivative fluence is $`E_{\rm path}`$, and exposure is $`X`$. At zero loss, $`E_{\rm path}=\mathcal E`$; with common vacuum loss, $`\mathcal E=E_{\rm path}+\kappa^2X/4`$.

## Connected route

1. [Model and conventions](model.md) fixes the commuting linear Hamiltonian, exact conditional closure, gate-equivalence convention, per-qubit force cap, and the two optimization problems. The physical pair angle is $`2A_{ij}`$; the ordinary diagonal of $`A`$ is global phase.
2. [Spectral control cost](spectral_cost.md) proves the exact fixed-matrix minimum, signed real multiplicity $`2m`$, the sharp cross-block bound, and phase–exposure inequalities. Its weighted spectral method has established mathematical antecedents.
3. [Gate-layer bounds](gate_layer_bounds.md) handles every integer phase representative through an odd determinant, then proves robustness using Boolean unwrapping and a Frobenius singular-value estimate. Section 10 applies the converse directly to the actual vacuum lossy channel.
4. [Matching construction](matching_construction.md) implements the target exactly, accounts for action, peak force, temporal frequencies and displacement, and establishes exact finite-harmonic capacity. Its low-rank approximation example explains why approximate capacity needs a charged resource. Section 7 accounts for compensated damping.
5. [Loss and the force–exposure frontier](loss_and_frontier.md) derives the full emitted-field channel, including the imaginary environmental Gram phase, then solves the exposure-priced fixed-matrix problem through a complete area spectrum. The exact scalar frontier is distinct from a full gate-error optimum.
6. [Hardware resources](hardware_resources.md) translates force units and counts physical modes, controls, bandwidth and occupation. Its loss-duration bound, reproducible examples and memory model state additional paid resources.

## Claims and proof homes

| Claim | Scope | Authoritative home |
|---|---|---|
| $`\min T\mathcal E=2\pi\Phi_m(A)`$ | Specified full phase matrix; closed $`H^1`$ paths; independent complex controls; zero loss | [Spectral cost, Theorem 1](spectral_cost.md#2-exact-minimum-for-a-prescribed-full-matrix) |
| $`T\mathcal E\ge4\pi\sum_rw_rs_r(A_{AB})`$ | Every symmetric completion; sharp when free blocks are allowed | [Spectral cost, Theorem 3](spectral_cost.md#6-sharp-cost-when-only-a-cross-block-is-prescribed) |
| $`\mathcal A_\epsilon(K,m)=\Theta_\epsilon(K+K^2/m)`$ | Entire lossless layer, all wraps, $`0\le\epsilon<1/\sqrt2`$ | [Gate-layer bounds](gate_layer_bounds.md), [attaining construction](matching_construction.md) |
| $`T_\epsilon=\Theta_\epsilon(g^{-1}\sqrt{1+K/m})`$ | Per-qubit total force held fixed across modes; same lossless error range | [Gate-layer bounds, Section 7](gate_layer_bounds.md#7-consequence-for-a-force-limited-clock), [construction, Section 2](matching_construction.md#2-exact-action-and-force-limited-duration) |
| Exact optimum $`T\mathcal E=\pi^2K/2`$, $`T=\pi/(2g)`$ when $`K\le4m`$ | Zero loss, exact target, every phase representative | [Gate-layer bounds, Section 9](gate_layer_bounds.md#9-additional-finite-size-and-total-force-consequences) |
| Direct noisy congestion converse | Vacuum Markov loss, exact damped closure, $`\epsilon<1/(2\sqrt2)`$ | [Gate-layer bounds, Section 10](gate_layer_bounds.md#10-direct-converse-for-the-vacuum-lossy-channel) |
| Exact paid force–exposure frontier | Fixed full $`A,T,m,\kappa`$; no pointwise force cap | [Loss/frontier, L13–L22](loss_and_frontier.md#3-spectrum-of-the-closed-loop-area-operator) |
| Mode-independent global loss-duration constraint | Actual matching channel, exposure floor, bounded physical force | [Hardware resources, Section 8](hardware_resources.md#8-a-global-accuracy-constraint-from-vacuum-loss) |

Here $`w_r=\lceil r/(4m)\rceil`$. Exact matching optimality for $`K>4m`$ is bounded by finite lower and upper estimates, not solved in closed form. The noisy results are necessary conditions; the scalar frontier does not supply a matching diamond-error upper bound. The unitary and actual noisy-channel accuracy thresholds have different proofs and must remain separate.

The [one-pair learning bridge](../learning/HAEFFNER_BRIDGE.md) provides an entry from oscillator mechanics. The [related-work account](../references/related_work.md) distinguishes inherited control geometry and dissipative physics from the gate-level claims. The [verification guide](../verification/README.md) maps finite calculations to proof claims; computations check formulas and implementations, while the universal results rest on the analytical proofs.
