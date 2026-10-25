# Architecture consequences and paid resources

[Science map](README.md) · [Matching theorem](matching.md) · [Loss and exposure frontier](loss_and_frontier.md)

A common harmonic mediator supplies connectivity, but a single closed trajectory has limited capacity to encode many independent pair phases cheaply. The [matching theorem](matching.md) makes that statement operational: it applies to the implemented CZ layer, including phase representatives that differ by full turns and local Z rotations. This page translates the theorem into design constraints and an explicitly parameterized example.

The comparison concerns the [linear, commuting, exactly closed force model](model.md). Here $`m`$ denotes the number of disjoint pairs, there are $`2m`$ data qubits and $`b`$ accessible harmonic modes. A bus mode means a physical independent oscillator mode. A temporal harmonic is a control frequency on an existing mode; increasing the latter does not increase $`b`$.

## 1. Independent gates and collective phases have different costs

Write $`P`$ for the instantaneous bound on the sum of squared coupling amplitudes. In the absence of loss,

```math
\inf PT^2=\Theta\!\left(m+\frac{m^2}{b}\right)
```

for exact matching synthesis. The constants are universal and the lower bound includes every phase lift and diagonal completion. The upper bound is supplied by explicit closed loops. Under the individual constraints

```math
\sum_{\mu=1}^b \vert u_{\mu i}(t)\vert ^2\leq g^2
\quad\text{for every qubit }i,
```

the corresponding minimum duration has scaling

```math
T_{\min}=\Theta\!\left(\frac{\sqrt{1+m/b}}{g}\right).
```

Thus sustaining a constant duration in units of $`1/g`$ as $`m`$ grows requires $`b=\Omega(m)`$. This conclusion remains a necessary condition at a fixed sufficiently small nonzero global gate error, with the exact accuracy domain and finite constants stated in [matching.md](matching.md). The total drive allowed to each qubit is held fixed as modes are added.

This is a statement about independent phase directions. For contrast, take a collective rank-one matrix $`K=\chi vv^T`$ with $`v_i=\pm1`$. Its nonzero eigenvalue has magnitude $`\vert \chi\vert n`$, so a single bus attains $`ET=2\pi \vert \chi\vert n`$. Each qubit can have the same fixed force bound while the duration is independent of $`n`$ for fixed $`\chi`$. Such a gate generally couples all pairs. It is not a matching, and its usefulness depends on the task. The distinction explains why fast collective entanglement and a congestion bound for many independent pairs are compatible.

There is a direct hardware motivation for comparing these tasks. [Mai et al.](https://arxiv.org/html/2506.19535v1) use structured light to isolate sparse axial modes and demonstrate individually addressed pair gates in chains up to six ions. Isolating few modes can simplify control. The present result identifies a separate price when that choice must also support an extensive matching under bounded individual coupling. It does not assess that experiment's performance or replace its device model. Existing many-mode parallel gates, such as [Diaz et al.](https://arxiv.org/html/2604.25993v1), operate in a different mode-count regime. See the [related-work comparison](../references/related_work.md).

## 2. A global accuracy constraint from loss

Let the buses have common vacuum Markov loss rate $`\kappa\gt 0`$. Suppose the actual reduced spin channel, including any allowed local Z corrections, is within half-diamond distance $`\epsilon`$ of the desired matching, with

```math
0\lt \epsilon\lt \frac{1}{2\sqrt2},\qquad
\delta=\arcsin(2\epsilon),\qquad
L_\epsilon=-\log(1-2\epsilon).
```

The [robust phase-lift argument](matching.md) gives

```math
K_{AB}=\frac{\pi}{8}(I+2B)+R,
\qquad B\in\mathbb{Z}^{m\times m},
\qquad \lVert R\rVert_F\leq\frac\delta2.
```

The odd determinant of $`I+2B`$, the arithmetic-geometric mean inequality and the nuclear-norm perturbation bound imply

```math
\lVert K\rVert_*
\geq2\lVert K_{AB}\rVert_*
\geq\frac{\pi m}{4}-\delta\sqrt m
=:r_{m,\epsilon}\gt 0.
```

For completeness, the last perturbation step is
$`\lVert R\rVert_*\leq\sqrt m\lVert R\rVert_F`$; the unperturbed cross block has nuclear norm at least $`\pi m/8`$. Positivity follows from $`\delta\lt \pi/4`$ and $`m\geq1`$.

The [exposure bound](loss_and_frontier.md) holds relative to any unitary target:

```math
\epsilon\geq\frac{1-e^{-2\kappa X}}2.
```

One way to see its target independence is to use an antipodal computational-basis superposition. The actual output has largest eigenvalue $`(1+e^{-2\kappa s^TFs})/2`$, whereas a unitary maps the input to a pure state. Its trace distance from that pure state is at least one minus this largest eigenvalue. Averaging $`s^TFs`$ over signs supplies a choice with $`s^TFs\geq X`$.

Consequently $`X\leq L_\epsilon/(2\kappa)`$. The geometric inequality $`EX\geq\lVert K\rVert_*^2`$, together with the paid action $`G\geq E`$ and $`G\leq PT`$, yields the necessary bound

```math
\boxed{\quad
T\geq\frac{2\kappa\,r_{m,\epsilon}^2}{P L_\epsilon}.
\quad}
```

Under the individual coupling cap, $`P\leq2mg^2`$, so

```math
\boxed{\quad
gT\geq\frac{\kappa}{g}
\frac{(\pi m/4-\delta\sqrt m)^2}{mL_\epsilon}.
\quad}
```

At fixed small accuracy this grows linearly in $`m`$, independently of $`b`$. For small $`\epsilon`$, $`L_\epsilon\sim2\epsilon`$; the leading large-$`m`$ expression is $`gT\gtrsim (\pi^2/32)(\kappa/g)m/\epsilon`$. It must be combined with the finite-bus congestion lower bound, not substituted for it. This is a converse, not a claim that the bound is attainable for the full noisy channel.

The physical reason is distinct from temporal-mode congestion: the environment receives a distinguishable record of the spin-conditioned displacement. More modes can reduce the ideal time cost but do not by themselves remove the record. This is a constraint on a whole-layer worst-case error metric. It is not a per-qubit error probability, a local-stochastic error statement, or a fault-tolerance threshold.

## 3. Two resource comparisons

![Lossless duration brackets and exact fixed-phase action/exposure frontiers](figures/resource_frontiers.svg)

**Panel A.** The shaded intervals bracket the lossless optimal duration under the individual cap. With $`w_j=\lceil j/(4b)\rceil`$, the plotted necessary lower bound and achievable upper bound are

```math
\frac\pi2\left(\prod_{j=1}^m w_j\right)^{1/(2m)}
\leq gT_{\min}
\leq\frac\pi2\sqrt{\left\lceil\frac{m}{4b}\right\rceil}.
```

The lower bound relaxes the individual constraints to their total budget and holds uniformly over all phase lifts; the upper bound uses one explicit matching construction. The gap is a constant-factor gap in the converse, not a measured hardware uncertainty. For $`m\leq4b`$, both expressions equal $`\pi/2`$.

**Panel B.** This is the exact $`(G,X)`$ Pareto frontier at fixed $`T`$ and fixed full phase matrix $`K`$, without a pointwise force cap. The same $`m=64`$ matching completion is used for all three curves: 32 positive and 32 negative rank-one pair blocks, with nonzero eigenvalues of magnitude $`\pi/4`$. Here $`\kappa T=0.1`$. Each point is attainable in the independent-envelope model. Increasing the exposure price reduces $`X`$ while increasing $`G`$. Larger $`b`$ lowers the least-action endpoint; its exposure need not decrease. Full gate error also depends on the structure of the environmental Gram matrix, so this exact exposure frontier is not an exact diamond-error frontier.

The figure and its numbers are reproduced by [resource_examples.py](../verification/resource_examples.py). They use analytical formulas, not fitted data.

## 4. A damped matching example with an actual peak-force cap

Consider $`m=256`$ independent pairs and the illustrative dimensionless rate $`\kappa/g=10^{-3}`$. This is a model parameter, not an estimate for a particular device. Assign pair $`j`$ to the circular temporal harmonic

```math
k_j=\left\lceil\frac{j}{4b}\right\rceil.
```

The [matching construction](matching.md) gives each of its two qubits a displacement coefficient of magnitude $`1/(4\sqrt{k_j})`$ multiplying $`e^{\pm2\pi i k_j t/T}-1`$. Keeping this path under damping requires the compensated physical force $`u=\dot\alpha+\kappa\alpha/2`$. Its exact maximum magnitude is

```math
\max_t \vert u_i(t)\vert 
=\frac{\sqrt{(2\pi k_j/T)^2+\kappa^2/4}+\kappa/2}{4\sqrt{k_j}}.
```

For the displayed parameters, choosing

```math
gT=\max_j
\frac{\pi\sqrt{k_j}}{2\sqrt{1-\kappa/(4g\sqrt{k_j})}}
```

therefore respects every individual cap, with the limiting harmonic saturating it. The denominator condition is necessary for this particular path; it is satisfied here. Its exposure is

```math
gX=\frac{gT}{4}\sum_{j=1}^m\frac1{k_j}.
```

| Bus modes $`b`$ | Highest harmonic | Duration $`gT`$ | Exposure $`gX`$ | Highest in-interval angular frequency divided by $`g`$ | Rigorous half-diamond error floor |
|---:|---:|---:|---:|---:|---:|
| 1 | 64 | 12.5666 | 59.6144 | 31.9995 | 0.05620 |
| 4 | 16 | 6.2834 | 84.9696 | 15.9995 | 0.07814 |
| 16 | 4 | 3.1418 | 104.7263 | 7.9995 | 0.09449 |
| 64 | 1 | 1.5710 | 100.5435 | 3.9995 | 0.09108 |

The last column is $`(1-e^{-2\kappa X})/2`$, a lower bound for these explicit controls. It is not a calculation of their exact diamond distance. All four fast constructions fail a 1% global half-diamond error target. The architecture-wide noisy converse above gives $`gT\geq7.7916`$ for that target, for every $`b`$. In particular, the short durations in the last two rows cannot meet the target through a different closed waveform at the same individual cap. The first row being slower than this necessary bound does not certify its accuracy; its explicit exposure already rules it out.

This example identifies what adding modes does and what it leaves unresolved. It improves ideal parallelism, but a low-error design must also pay for smaller displacement exposure. The exact fixed-$`K`$ frontier gives that action price; imposing a pointwise cap and optimizing the full channel simultaneously is a further control problem.

## 5. Bandwidth, occupation, preparation and memory

The following resources delimit the interpretation of every upper bound.

| Resource | Accounting in this work | Consequence for a device |
|---|---|---|
| Physical modes | $`b`$ independent harmonic modes, counted explicitly | A temporal tone does not create another physical mediator. |
| Coupling | $`G=\int\sum_{\mu i}\vert u_{\mu i}\vert ^2dt`$; individual caps sum over all modes | Adding modes does not grant each qubit proportionally more total drive. Conversion to optical or microwave power is device dependent. |
| Addressing | Independent complex envelope for each usable qubit-mode coupling | Lower bounds survive additional control restrictions; exact attaining controls may not be native to a device with tied couplings. |
| Modulation and slew | Circular pulses use in-interval angular frequencies through $`2\pi\lceil m/(4b)\rceil/T`$ | Forces are nonzero at the interval endpoints. Hard switching has spectral tails; no strict bandwidth or slew-limited optimality is claimed. |
| Bus occupation | Conditional occupation is $`N_z(t)=\lVert A(t)z\rVert^2`$ | The harmonic model has no fixed occupation ceiling. Finite oscillator range, anharmonicity and Lamb-Dicke limits require a separate constraint. |
| Bus preparation and return | Vacuum initial state; every conditional path returns exactly to vacuum | Preparation time is outside $`T`$. Ideal closed layers do not leave a residual oscillator state to reset, but the emitted bath record remains. |
| Data storage | Data remain present for the entire gate interval | Hardware memory errors must be added in an application estimate. |
| Local corrections | Product Z rotations and global phases are allowed | A device must implement or track these corrections; their timing and errors are not part of the force action. |

Transient occupation can be bounded explicitly for the circular construction. When $`m=4bq`$, each bus carries four pair directions at each harmonic $`k\leq q`$. One pair contributes at most $`1/\sqrt{k}`$ to its conditional displacement magnitude. The triangle inequality therefore gives the conservative bound

```math
\max_{z,t}\sum_\mu \vert (A(t)z)_\mu\vert ^2
\leq16b\left(\sum_{k=1}^q k^{-1/2}\right)^2
\leq16m.
```

This is an allowed growing resource, not a constant-occupation construction. The per-mode bound is the same expression without the factor $`b`$. Neither the Frobenius coupling budget nor the exposure trace by itself bounds the largest branch force by a constant.

A simple additional memory model illustrates the time cost. If each of the $`2m`$ data qubits has independent Poisson Z errors at rate $`\gamma`$, the idle-only entanglement infidelity over time $`T`$ is exactly

```math
1-F_e^{\rm idle}
=1-\left(\frac{1+e^{-2\gamma T}}2\right)^{2m}
=2m\gamma T+O((m\gamma T)^2).
```

At fixed finite system size and weak noise, independent bus loss adds the first-order coefficient $`\kappa X`$, so the leading infidelity is $`\kappa X+2m\gamma T`$. This is a specified noise model and a perturbative metric; it does not replace the global diamond bounds above.

For example, multiplying every circular harmonic by an integer $`r\geq1`$, while saturating the lossless individual force cap, changes $`T`$ to $`T_1\sqrt r`$ and $`X`$ to $`X_1/\sqrt r`$. The leading noise expression becomes

```math
\frac{\kappa X_1}{\sqrt r}+2m\gamma T_1\sqrt r.
```

For $`\gamma\gt 0`$, its continuous optimum is $`r=\kappa X_1/(2m\gamma T_1)`$, clipped to $`r\geq1`$ before comparing neighboring integers. If $`\gamma=0`$ and $`\kappa\gt 0`$, this unrestricted family has no finite minimizing winding. This is an optimization of the first-order expression within this pulse family, not of the full noisy channel. Damping compensation, bandwidth and occupation must still be checked. The underlying small-excursion/more-winding idea is already present in [Müller, Luoma and Strunz](https://arxiv.org/html/1907.08033v2); the present formulas keep its force and duration price explicit.

## 6. What follows for architecture

The theorem gives a criterion for a specific primitive: few-mode linear harmonic connectivity cannot supply arbitrarily many independent CZ gates at constant duration and bounded per-qubit coupling. Existing weighted control geometry supplies the spectral machinery; [phase equivalence and approximation robustness](matching.md) make its consequence a statement about a quantum gate rather than an arbitrarily selected phase matrix. Loss adds a separately paid requirement on coherent displacement exposure.

Squeezing, nonlinear or encoded buses, additional coherent ancillas, intermediate measurements, noncommuting spin operations during the force interval, approximate bus return and different noise models can change the problem. They are resources or changed assumptions to analyze explicitly. No application-level speedup or error-correction threshold is inferred from this primitive-level result.

Continue with [the exact loss/frontier derivation](loss_and_frontier.md), the [source comparison](../references/related_work.md), or the [reproduction guide](../verification/README.md).
