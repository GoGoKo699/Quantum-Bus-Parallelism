# Independent gates through a shared harmonic bus

## The architectural question

A harmonic oscillator can mediate interactions between many qubits. Closed conditional displacements accumulate a geometric phase while removing the final spin–oscillator entanglement. This mechanism supports collective interactions and selected two-qubit gates. Its ability to connect every pair leaves a separate resource question: how long does it take to implement a layer of many **disjoint** entangling gates through a fixed number of oscillators?

This project answers that question for commuting linear conditional forces. The model gives every qubit independent control of its force on every mode, subject only to explicitly stated force constraints. It is a relaxation of many hardware control models. A lower bound in this permissive model therefore remains valid for a device whose available controls form a subset, after converting its drives to the same effective-force units. Attaining the bound on a particular device requires a separate control and bandwidth check.

The central result is

```math
\mathcal A_\epsilon(K,m)=\Theta_\epsilon(K+K^2/m),
\qquad
T_\epsilon(K,m,g)=\Theta_\epsilon\!\left(\frac{\sqrt{1+K/m}}{g}\right),
\qquad\text{(1)}
```

for every fixed $`0\le\epsilon<1/\sqrt2`$. Here $`K`$ is the number of disjoint target pairs, $`m`$ is the number of bus modes, $`g`$ is a per-qubit force bound, $`\mathcal A_\epsilon`$ is the minimum force fluence multiplied by duration, and $`\epsilon`$ is a worst-case error for the **entire gate layer**. The constants can depend on $`\epsilon`$, but not on $`K`$, $`m`$, or $`g`$.

The exact upper construction also implements the target with zero error. Its growing bandwidth requirement in the few-mode regime is part of the [resource interpretation](hardware_resources.md).

## Hamiltonian and exact closure

There are $`N=2K`$ qubits, labeled $`A_1,\ldots,A_K,B_1,\ldots,B_K`$, and $`m\ge1`$ dynamical canonical harmonic modes. The number $`m`$ counts oscillator degrees of freedom, not control channels or modulation tones. Write $`Z_j`$ for Pauli $`Z`$ on qubit $`j`$ and $`a_\ell`$ for the annihilation operator of mode $`\ell`$. In an interaction picture,

```math
\frac{H(t)}{\hbar}
=i\sum_{j=1}^{N}\sum_{\ell=1}^{m}
Z_j\bigl[u_{j\ell}(t)a_\ell^\dagger-u_{j\ell}(t)^*a_\ell\bigr].
\qquad\text{(2)}
```

Each $`u_{j\ell}\in L^2([0,T];\mathbb C)`$ is an independently programmable effective force with units of inverse time. The qubit axes commute at all times. Define the absolutely continuous displacement paths

```math
\alpha_{j\ell}(t)=\int_0^t u_{j\ell}(s)\,ds,
\qquad \alpha_{j\ell}(0)=\alpha_{j\ell}(T)=0.
\qquad\text{(3)}
```

Exact closure is required separately for every qubit and mode. It implies exact spin–bus disentanglement for every initial oscillator state. In the physical picture the bus can still undergo its known free evolution; equality to its initial density operator requires compensating that evolution or choosing an invariant initial state. Neither finite oscillator temperature nor an initial coherent displacement changes the closed-loop spin gate in this ideal harmonic model.

The exact propagator at closure is

```math
U_A=\exp(iZ^{\mathsf T}AZ),
\qquad
A_{ij}=\mathrm{Im}\sum_{\ell=1}^{m}
\int_0^T\alpha_{i\ell}(t)^*\dot\alpha_{j\ell}(t)\,dt.
\qquad\text{(4)}
```

Integration by parts and closure make $`A`$ real symmetric. Thus the coefficient of $`Z_iZ_j`$ for $`i<j`$ is **$`2A_{ij}`$**. Diagonal entries contribute the global phase $`\mathrm{tr}A`$. This factor of two is used throughout the proofs and the verification code.

Equation (4) follows either from the Weyl displacement composition law or the terminating Magnus expansion: the commutator of two Hamiltonians is a quadratic polynomial in the mutually commuting $`Z_j`$, and all higher nested commutators vanish. The [spectral account](spectral_cost.md) treats the $`L^2`$ control class and the associated convergent Fourier expansions explicitly.

## Target and physical gate equivalence

The target layer is

```math
V_K=\prod_{j=1}^K\exp\!\left(\frac{i\pi}{4}Z_{A_j}Z_{B_j}\right).
\qquad\text{(5)}
```

Each factor is a maximally entangling two-qubit gate up to single-qubit phases. The pairing is fixed before the control is chosen. Relabeling the qubits gives any disjoint matching. No claim about an arbitrary dense interaction graph is needed for the lower bound.

Allow free final local $`Z`$ corrections

```math
L(\theta)=\exp\!\left(i\sum_{j=1}^{N}\theta_jZ_j\right).
\qquad\text{(6)}
```

For a unitary $`W`$, let $`\mathcal W(\rho)=W\rho W^\dagger`$. Define the layer error

```math
\epsilon(A)=\inf_{\theta\in\mathbb R^N}
\frac12\left\|\mathcal U_A-\mathcal L(\theta)\circ\mathcal V_K\right\|_\diamond.
\qquad\text{(7)}
```

Global phase is already invisible to a unitary channel. The infimum over local phases is attained because their channel action is periodic and continuous. Equation (7) permits all physical phase wraps of the target. It does not select one convenient real logarithm of the gate.

The diamond norm measures worst-case distinguishability, including an entangled reference. A constant error bound on the whole layer is stronger than a constant error bound for each pair separately. Average gate fidelity is a different criterion. The fixed-error theorem still requires exact closure (3); it does not replace that hypothesis by a bound on residual bus displacement.

## Charged resources and optimization problems

The force fluence and action are

```math
\mathcal E=\int_0^T\sum_{j,\ell}|u_{j\ell}(t)|^2\,dt,
\qquad \mathcal A=T\mathcal E.
\qquad\text{(8)}
```

$`\mathcal E`$ has units of inverse time and $`\mathcal A`$ is dimensionless. They are effective Hamiltonian control costs, not device-independent energies in joules. The action is unchanged when a waveform is stretched in time and its amplitude is reduced inversely.

For integers $`K,m\ge1`$, let $`\mathcal A_\epsilon(K,m)`$ be the infimum of $`T\mathcal E`$ over all $`T>0`$ and controls satisfying (2), (3), and $`\epsilon(A)\le\epsilon`$. For the duration problem impose, for each qubit and almost every time,

```math
\sum_{\ell=1}^{m}|u_{j\ell}(t)|^2\le g^2,
\qquad g>0.
\qquad\text{(9)}
```

Let $`T_\epsilon(K,m,g)`$ be the infimum duration under this additional constraint. The norm in (9) charges a qubit's simultaneous drives on different modes together. A bound on each mode separately would supply a larger total force as $`m`$ grows and would define a different resource comparison. Equation (9) gives $`\mathcal E\le2Kg^2T`$.

These optimizations impose no independent bandwidth, oscillator-occupation, pulse-segmentation, or hardware participation constraint. The [construction](matching_construction.md) states its bandwidth and displacement costs, and the [hardware account](hardware_resources.md) explains when extra constraints matter.

## Exact statements and proof route

Put

```math
c=\frac\pi8,\qquad
w_r=\left\lceil\frac r{4m}\right\rceil,\qquad
G_{K,m}=\left(\prod_{r=1}^K w_r\right)^{1/K},\qquad
\delta=\arcsin\epsilon.
\qquad\text{(10)}
```

The connected lossless argument has five parts.

| Result | Statement and scope | Authoritative proof |
|---|---|---|
| Spectral control cost | For a **prescribed full real symmetric** $`A`$, the optimal action is $`2\pi\sum_r\lceil r/(2m)\rceil[\lambda_r^+(A)+\lambda_r^-(A)]`$. | [Spectral cost](spectral_cost.md) |
| Sharp cross-block cost | Every completion of $`C=A_{AB}`$ obeys $`\mathcal ET\ge4\pi\sum_rw_rs_r(C)`$; the completion is attainable when its free blocks do not impose unwanted gate interactions. | [Spectral cost, Section 6](spectral_cost.md#6-sharp-cost-when-only-a-cross-block-is-prescribed) |
| Exact physical-gate converse | Every exact implementation of (5), up to (6), has a cross block $`C=c(I+2M)`$ with integer $`M`$; therefore $`\mathcal ET\ge(\pi^2/2)KG_{K,m}`$. | [Gate-layer bounds](gate_layer_bounds.md) |
| Fixed-error converse | If (7) is at most $`\epsilon<1/\sqrt2`$, then $`\mathcal ET\ge(\pi^2/2)KG_{K,m}-2\pi\delta\lVert w\rVert_2\ge(\pi^2/2)(1-4\delta/\pi)KG_{K,m}`$. | [Gate-layer bounds](gate_layer_bounds.md) |
| Exact attaining order | An explicit closed-loop construction has $`\mathcal ET=(\pi^2/2)\sum_{r=1}^K w_r`$ and $`T=(\pi/2g)\sqrt{\lceil K/(4m)\rceil}`$. | [Matching construction](matching_construction.md) |

Here $`\lambda_r^+`$ are the positive eigenvalues in descending order and $`\lambda_r^-`$ are the descending magnitudes of negative eigenvalues, with zeros appended. The last row attains the **scaling order** of the gate-level converse; the finite-size lower and upper constants need not coincide.

Since $`G_{K,m}\ge\max\{1,K/(4em)\}`$, the lower bounds and the explicit construction imply (1). In particular,

```math
T_\epsilon(K,m,g)
\ge\frac\pi{2g}\sqrt{(1-4\arcsin(\epsilon)/\pi)G_{K,m}},
\qquad\text{(11)}
```

whereas the upper duration in the table is achievable with zero spin-gate error. The fixed-error range is a proved sufficient range. The boundary $`1/\sqrt2`$ is not asserted to be an optimal threshold for a stronger theorem.

## Physical interpretation and scope

At fixed $`g`$ and fixed error tolerance, a bounded number of modes forces the matching-layer duration to grow as $`\sqrt K`$. Keeping duration bounded as $`K`$ grows requires $`m=\Omega(K)`$ in this model, and $`m=\Theta(K)`$ suffices in the independently controlled model. A collective phase proportional to $`(\sum_jZ_j)^2`$ can instead use one real spectral direction. Thus pairwise connectivity and independent-pair throughput are different resources.

The assumptions permit sign reversals and time-dependent envelopes that preserve the commuting qubit axes. Spin-independent, number-preserving quadratic oscillator evolution can be absorbed into a passive mode frame without changing the Euclidean force norm; its known net bus unitary remains in the physical picture. A time-dependent frame need not preserve the bandwidth of the original actuator signal. Intermediate noncommuting spin controls, additional direct qubit interactions, measurements, nonlinear oscillator couplings, and freely supplied active squeezing are different models. Any use of those mechanisms must account for its own resources before comparing it with (1).

Closed-loop geometric gates, spectral area inequalities, and parallel constructions have substantial antecedents. The contribution developed here is the gate-equivalence-invariant, fixed-error finite-mode converse and the resulting resource scaling. The [related-work account](../references/related_work.md) separates those ingredients and states the scope of the literature comparison.

## Vacuum-loss extension and exposure

The ideal closed-loop theorem above remains valid for every initial bus state. The [loss extension](loss_and_frontier.md) adds a more specific physical model: vacuum initial modes and input fields, unmonitored Markovian damping at a common number-decay rate $`\kappa`$, and exactly closed **actual damped** paths. Writing their coefficients as $`D_{\ell j}(t)=\alpha_{j\ell}(t)`$ gives

```math
\dot D=u-\kappa D/2,\qquad D(0)=D(T)=0,\qquad
A=\mathrm{Im}\int D^\dagger\dot D\,dt,
```

```math
X=\int\lVert D\rVert_F^2dt,\qquad
E_{\rm path}=\int\lVert\dot D\rVert_F^2dt,\qquad
\mathcal E=E_{\rm path}+\kappa^2X/4.
```

Here $`u=[u_{j\ell}]_{\ell,j}`$ uses mode-first matrix indices. The paid force fluence remains $`\mathcal E`$ and its dimensionless action remains $`T\mathcal E`$. At zero loss, $`E_{\rm path}=\mathcal E`$; otherwise the derivative cost alone omits damping compensation. $`X`$ has time units and equals integrated bus occupation averaged over uniform computational strings. It is not a maximum-branch occupation or a complete channel-error measure.

The emitted field retains which-branch information even when the bus closes. Its exact channel contains both the real and imaginary parts of $`\int D^\dagger D`$. The [direct noisy converse](gate_layer_bounds.md#10-direct-converse-for-the-vacuum-lossy-channel) proves the same congestion scaling as a necessary condition on the actual channel for $`\epsilon<1/(2\sqrt2)`$, with $`\delta=\arcsin(2\epsilon)`$. The [force–exposure frontier](loss_and_frontier.md#5-paid-damping-and-the-complete-fixed-a-exposure-frontier) is exact for a specified full phase matrix; it does not optimize diamond error or the physical gate's entire phase-equivalence class. A [separate loss-duration lower bound](hardware_resources.md#8-a-global-accuracy-constraint-from-vacuum-loss) charges the exposure required by a whole matching layer.

## Reading route

Read [spectral cost](spectral_cost.md) for the geometric control theorem, then [gate-layer bounds](gate_layer_bounds.md) for phase wrapping and robustness. The [explicit construction](matching_construction.md) supplies the upper bound and its implementation costs. The [loss and exposure account](loss_and_frontier.md) derives the noisy channel and the exact scalar resource frontier. [Hardware resources](hardware_resources.md) then translates the ideal law and its loss extension into device-level questions. The [verification guide](../verification/README.md) records finite checks of the formulas and constructions; the universal statements rest on the proofs.
