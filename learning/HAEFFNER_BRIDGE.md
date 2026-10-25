# From trapped-ion geometric gates to finite-bus congestion

A harmonic mediator can connect many qubits. The question here is how much independently programmable entangling action that connection supplies at a fixed force budget: can a few modes perform an extensive layer of independent CZ gates quickly, and what does loss add to the resource requirement?

The selected educational anchor is **H. Häffner, C. F. Roos and R. Blatt, *Quantum computing with trapped ions*, Physics Reports 469, 155–203 (2008)**. All section and page pointers below refer to the **99-page arXiv:0809.4368v1 preprint, submitted 25 September 2008**: [version record](https://arxiv.org/abs/0809.4368v1), [open PDF](https://arxiv.org/pdf/0809.4368v1). The page numbers are the preprint/PDF pages, not the journal pagination.

This is the single foundations anchor. The [30-milestone map](MILESTONES.md) organizes the complete account. The [model](../science/model.md) defines the admissible controls, and the scientific pages supply the resource theorems and proofs.

## Targeted route through the anchor

These selections are sufficient for the physical connection; reading the entire review is unnecessary.

| Connection | Verified v1 pointer | Milestones |
|---|---|---|
| Oscillator and laser coupling | [§2.2, pp. 8–10, Eqs. (1)–(7)](https://arxiv.org/pdf/0809.4368v1#page=8) | M02–M03 |
| Fixed spin basis and local rotations | [§2.5, pp. 16–17; Eq. (10), p. 17](https://arxiv.org/pdf/0809.4368v1#page=17) | M01, M03 |
| Physical normal modes | [§2.6.1, pp. 22–23; Fig. 10, p. 23](https://arxiv.org/pdf/0809.4368v1#page=22) | M07 |
| A phase gate in the spin-$`x`$ basis | [§2.6.3, pp. 28–29; Eq. (15), p. 28](https://arxiv.org/pdf/0809.4368v1#page=28) | M01, M04 |
| Conditional force and return of motion | [§2.6.4, pp. 29–31; Fig. 15, p. 30](https://arxiv.org/pdf/0809.4368v1#page=29) | M04, M14 |
| Heating and motional dephasing | [§3.2, starting p. 45; heating on pp. 46–47](https://arxiv.org/pdf/0809.4368v1#page=45) | M05, M25 |

The review supplies the physical mechanism and its experimental context. Its historical device figures are not current hardware estimates. The matrix optimization, phase-lift converse, and robust Boolean argument below are supplied by this project and its attributed research ingredients.

## Notation and the effective model

| Anchor notation or object | Convention used here | Required distinction |
|---|---|---|
| $`a,a^\dagger`$ | $`a_\mu,a_\mu^\dagger`$, $`\mu=1,\ldots,b`$ | $`b`$ counts physical oscillator modes. |
| $`\sigma_x`$ or another fixed spin axis | $`Z_i`$ in a fixed rotated basis | A basis choice does not authorize changing the coupled axis during the gate. |
| $`\Omega,\eta`$ | Effective coefficients $`u_{\mu i}(t)`$ and bound $`g`$ | Laser strength and Lamb–Dicke factors need a device-specific conversion. |
| Motional occupation | $`\langle a_\mu^\dagger a_\mu\rangle`$ | Here $`n`$ counts qubits and $`m`$ counts disjoint CZ pairs. |

A fixed change of spin basis is straightforward: for the Hadamard operator $`H_{\rm Had}`$, $`H_{\rm Had}\sigma_xH_{\rm Had}=Z`$. Applying one fixed basis convention throughout preserves commutation of the spin-dependent forces. The theorem does not include interspersed rotations that change that axis.

The project takes the following effective interaction as its starting assumption, with $`\hbar=1`$:

**(B1)**

```math
H_{\rm bus}(t)=
i\sum_{\mu,i}Z_i
\left[u_{\mu i}(t)a_\mu^\dagger-u_{\mu i}(t)^*a_\mu\right].
```

Every complex coefficient is independently programmable. That control freedom is stronger than access to a single global laser envelope or a fixed set of mode participation factors. A device reduction must establish which coefficients can actually be controlled and how its laser constraints map to

**(B2)**

```math
\sum_\mu\vert u_{\mu i}(t)\vert ^2\leq g^2
\quad\text{for each qubit }i.
```

In particular, neither $`g=\Omega`$ nor $`g=\eta\Omega`$ is assumed. Detunings, normalization conventions, mode shapes, and shared control channels all matter. The [resource ledger](../science/architecture.md) also separates force, occupation, modulation, preparation, and memory costs.

## From a conditional loop to the phase matrix

This is the connection between M04, M08 and M15. Begin without loss and let

```math
\dot\alpha_{\mu i}(t)=u_{\mu i}(t),\qquad
\alpha_{\mu i}(0)=\alpha_{\mu i}(T)=0.
```

Collect the trajectories into a $`b\times n`$ matrix $`A(t)`$. For a computational string $`z\in\{+1,-1\}^n`$, the conditional coherent amplitude is $`A(t)z`$.

Displacements do not commute as scalar translations. With $`D(\alpha)=\exp(\alpha a^\dagger-\alpha^*a)`$, the phase accumulated around a closed branch path is

**(B3)**

```math
q(z)=\mathrm{Im}\int_0^T
[A(t)z]^\dagger\dot A(t)z\,dt=z^TKz,
\qquad
K=\mathrm{Im}\int_0^T A^\dagger\dot A\,dt.
```

Closure removes the final spin–bus displacement correlation; the accumulated phase remains. Integration by parts makes $`K`$ real symmetric. The resulting data gate is

**(B4)**

```math
U_K=\exp(i\mathbf{Z}^TK\mathbf{Z})
=e^{i\mathrm{tr}K}
\exp\left(2i\sum_{i\lt j}K_{ij}Z_iZ_j\right).
```

The coefficient of $`Z_iZ_j`$ is therefore $`2K_{ij}`$. The diagonal of $`K`$ changes only a global phase. These two facts will be essential when deciding whether a control bound applies to a physical gate or only to one matrix representing it.

The basic scalar resources are

**(B5)**

```math
E=\int_0^T\Vert \dot A(t)\Vert _F^2dt,\qquad
X=\int_0^T\Vert A(t)\Vert _F^2dt.
```

At zero loss, $`E`$ is the squared-force action. The exposure $`X`$ is the integrated bus occupation averaged over uniform computational strings. Neither quantity alone imposes a maximum occupation on every branch.

## A fully paid single-CZ loop

[M14](MILESTONES.md#m14-a-fully-paid-single-cz-loop) makes the normalization concrete. Take two qubits, one bus, vacuum initially, and

**(B6)**

```math
\alpha_1(t)=\alpha_2(t)=\frac14
\left(e^{2\pi it/T}-1\right).
```

Both columns close exactly. Their forces are

**(B7)**

```math
u_1(t)=u_2(t)=\frac{i\pi}{2T}e^{2\pi it/T},
\qquad
\max_t\vert u_i(t)\vert =\frac{\pi}{2T}.
```

The relevant integrals are

**(B8)**

```math
K=\frac{\pi}{8}
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
F:=\mathrm{Re}\int_0^T A^\dagger A\,dt
=\frac{T}{8}
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
```

For example, $`\int_0^T\vert e^{2\pi it/T}-1\vert ^2dt=2T`$ gives $`F`$, and
$`\mathrm{Im}\int_0^T(e^{-2\pi it/T}-1) (2\pi i/T)e^{2\pi it/T}dt=2\pi`$ gives $`K`$.
Thus

**(B9)**

```math
U_K=e^{i\pi/4}e^{i\pi Z_1Z_2/4},
\qquad
e^{-i\pi(Z_1+Z_2)/4}U_K=\mathrm{CZ}.
```

The final correction is a product of local $`Z`$ rotations, as permitted by the target convention. Its implementation or frame tracking belongs to the device account.

The complete force and displacement ledger for this loop is

**(B10)**

```math
E=\frac{\pi^2}{2T},\qquad
X=\frac T4,\qquad
\max_{z,t}\vert A(t)z\vert ^2=1.
```

Under the individual cap (B2), its shortest duration is $`T=\pi/(2g)`$. At that duration,

```math
gT=\frac\pi2,\qquad E/g=\pi,\qquad gX=\frac\pi8.
```

The force is nonzero at the interval endpoints. Vacuum preparation, local correction overhead, and finite switching bandwidth are not included in this gate interval; they have explicit places in the [architecture account](../science/architecture.md). This example is a normalized control construction, not a calibrated trapped-ion pulse prescription.

## Why a finite bus has a temporal cost

M17–M19 extend the loop to a matrix target. Every closed $`H^1`$ trajectory admits

```math
A(t)=\sum_{k\neq0}V_k
\left(e^{2\pi ikt/T}-1\right).
```

The phase and action become

**(B11)**

```math
K=2\pi\sum_{k\neq0}k\,\mathrm{Re}(V_k^\dagger V_k),
\qquad
E=\frac{4\pi^2}{T}\sum_{k\neq0}k^2\Vert V_k\Vert _F^2.
```

At a fixed signed harmonic, $`\mathrm{Re}(V_k^\dagger V_k)`$ has real rank at most $`2b`$: each complex bus coefficient has two real quadratures. More independent directions require higher temporal harmonics, which cost more action per unit phase.

Let $`\ell_j^+`$ and $`\ell_j^-`$ be the positive eigenvalues and negative-eigenvalue magnitudes of $`K`$, descending separately within each sign. The exact fixed-matrix optimum is

**(B12)**

```math
E_{\min}=\frac{2\pi}{T}
\sum_{\sigma\in\{+,-\}}\sum_j
\left\lceil\frac{j}{2b}\right\rceil\ell_j^\sigma.
```

The [spectral proof](../science/spectral_cost.md) supplies both the lower bound and attaining pulses. Its spectral allocation uses the established weighted bilinear-control framework of [Wong and Baillieul, Theorem 5.1 and Corollary 5.1](https://arxiv.org/pdf/1201.6527v2). The selected review supplies the physical foundations, not this optimization theorem.

For each disjoint CZ pair, either block

```math
\frac\pi8\begin{pmatrix}1&1\\1&1\end{pmatrix}
\quad\text{or}\quad
\frac\pi8\begin{pmatrix}-1&1\\1&-1\end{pmatrix}
```

has the desired off-diagonal entry. Its sole nonzero eigenvalue is respectively $`+\pi/4`$ or $`-\pi/4`$. Distributing pair blocks between signs therefore places up to $`4b`$ independent pairs into each absolute harmonic. The pointwise force calculation extends (B7) and gives the explicit upper bound

**(B13)**

```math
gT_{\rm construct}=\frac\pi2
\sqrt{\left\lceil\frac{m}{4b}\right\rceil}.
```

This is an achievable duration, with the cap summing all modes at each qubit. To prove it has the right scaling for the gate, every other phase representative must also be included.

## From a matrix representative to the quantum gate

M11 and M20 supply the missing step. A four-point mixed phase difference of $`z^TKz`$ is $`8K_{ij}`$. For a CZ graph with adjacency $`\mathsf{A}`$, agreement up to local $`Z`$ rotations requires

**(B14)**

```math
K_{ij}=\frac\pi8\mathsf{A}_{ij}+\frac\pi4N_{ij},
\qquad N_{ij}\in\mathbb{Z},\quad i\neq j.
```

The integers can be large. Minimizing only the unwrapped adjacency matrix would not give a gate-level converse.

Across the two sides of an $`m`$-pair matching, (B14) gives

**(B15)**

```math
K_{AB}=\frac\pi8(I_m+2B),\qquad B\in\mathbb{Z}^{m\times m}.
```

Its integer factor has odd, nonzero determinant. If $`\sigma_j`$ are its cross-block singular values, this implies

```math
\prod_{j=1}^m\sigma_j(K_{AB})\geq(\pi/8)^m.
```

This statement survives every phase lift and every diagonal completion. A weighted arithmetic–geometric mean estimate, combined with the sharp cross-block spectral bound, yields the converse matching the scaling of (B13):

**(B16)**

```math
T_{\min}=
\Theta\left(\frac{\sqrt{1+m/b}}{g}\right)
```

in the stated lossless model. [The matching theorem](../science/matching.md) contains the finite constants, construction, and exact quantifiers.

### Nearly correct gates still require consistent phase lifts

M23–M24 address approximation. A useful algebraic fact is that a quadratic Boolean phase cannot wrap independently at every input while remaining uniformly close to a valid phase function.

Suppose a degree-two polynomial on $`x\in\{0,1\}^n`$ satisfies

```math
q(x)=2\pi h(x)+e(x),\qquad
h(x)\in\mathbb{Z},\quad \vert e(x)\vert \leq\delta\lt \pi/4.
```

On every three-coordinate cube, the third mixed finite difference of $`q`$ vanishes. The corresponding difference of $`e`$ has magnitude at most $`8\delta\lt 2\pi`$, so the integer third difference of $`h`$ must be zero. Hence $`h`$ itself has Boolean degree at most two. Parseval then controls the matrix coefficients of the residual.

For the actual closed-bus noisy channel at global half-diamond error $`\epsilon\lt 1/(2\sqrt2)`$, testing two-state superpositions with one fixed reference string confines the relative coherence phases to an arc of half-width $`\delta=\arcsin(2\epsilon)`$. The argument then gives

**(B17)**

```math
K_{AB}=\frac\pi8(I_m+2B)+R,\qquad
\Vert R\Vert _F\leq\frac{\delta}{2}.
```

The reference-string argument also handles the extra environmental phase in the next section: at fixed reference string it is only linear in the other string. Thus (B17) does not assume that the geometric unitary alone approximates the target. Singular-value perturbation bounds then preserve the congestion converse at fixed sufficiently small global error. The [full proof](../science/matching.md) states a positive bound at every system size.

## What loss adds, and what motional heating does not mean here

M25–M28 introduce a specific open-system model:

**(B18)**

```math
\dot\rho=-i[H_{\rm bus},\rho]
+\kappa\sum_\mu\mathcal{D}[a_\mu](\rho),
\qquad
\mathcal{D}[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
```

This is vacuum Markov damping. Without a drive it obeys
$`d\langle a^\dagger a\rangle/dt=-\kappa\langle a^\dagger a\rangle`$.
A heating process can increase occupation from vacuum; it requires a different generator, for example an excitation term $`\mathcal{D}[a^\dagger]`$. An experimental motional heating rate therefore cannot simply be substituted for $`\kappa`$.

A prescribed path now requires

**(B19)**

```math
u=\dot A+\frac{\kappa}{2}A,\qquad
G:=\int_0^T\Vert u\Vert _F^2dt
=E+\frac{\kappa^2}{4}X.
```

For the single-CZ loop (B6), this is

**(B20)**

```math
u_i(t)=\frac14\left[
\left(\frac{2\pi i}{T}+\frac{\kappa}{2}\right)e^{2\pi it/T}
-\frac{\kappa}{2}\right],
\qquad
G=\frac{\pi^2}{2T}+\frac{\kappa^2T}{16}.
```

Keeping the original path does not keep the original peak force. In this example the exact individual peak is

```math
\frac14\left[
\sqrt{(2\pi/T)^2+\kappa^2/4}+\kappa/2\right].
```

The damped cap is met when
$`gT\geq\pi/[2\sqrt{1-\kappa/(4g)}]`$, provided $`\kappa\lt 4g`$ for this particular circular family. This restriction is not a universal impossibility statement for other paths.

Although the bus returns to vacuum, the output field retains a branch-dependent coherent record with amplitude $`\sqrt{\kappa}A(t)z`$. Write

```math
\int_0^T A^\dagger A\,dt=F+iJ,\qquad J^T=-J.
```

Relative to $`U_K`$, a data coherence $`\vert z\rangle\langle z'\vert `$ is multiplied exactly by

**(B21)**

```math
\exp\left[
-\frac{\kappa}{2}(z-z')^TF(z-z')
+i\kappa z'^TJz
\right].
```

The skew-Gram phase generally cannot be discarded. The coherent-overlap loss mechanism is established in [Louis et al.](https://arxiv.org/pdf/0804.3240) and [Müller, Luoma and Strunz](https://arxiv.org/html/1907.08033v2). Louis et al. also construct independent single-qubit dephasing by suitable sequences, so loss does not make correlated errors unavoidable.

An antipodal computational-basis superposition supplies the target-independent bound

**(B22)**

```math
\frac12\Vert \mathcal{E}-\mathcal{V}\Vert _\diamond
\geq\frac{1-e^{-2\kappa X}}2
```

for every unitary target $`\mathcal{V}`$. At fixed trajectories, the first-order entanglement infidelity relative to $`U_K`$ is $`\kappa X`$. Average gate infidelity has the additional factor $`d/(d+1)`$, $`d=2^n`$. These are whole-gate metrics.

The exact fixed-$`K`$ frontier prices $`X`$ together with the paid action $`G`$. If
$`r_j=\lceil j/(2b)\rceil`$ and $`a_j=(r_j\pi/T)^2+\kappa^2/4`$, its parameterization is

**(B23)**

```math
X(\mu)=\sum_{\sigma,j}\frac{\ell_j^\sigma}{\sqrt{a_j+\mu}},
\qquad
G(\mu)=\sum_{\sigma,j}
\frac{(2a_j+\mu)\ell_j^\sigma}{\sqrt{a_j+\mu}},
\qquad \mu\geq0.
```

Here $`\mu`$ is an exposure price, not a physical mode index. The [loss/frontier derivation](../science/loss_and_frontier.md) proves attainment and completeness using the compact area-operator spectrum. This resource frontier does not determine the optimal full channel error, because $`F`$ and $`J`$ contain information beyond their exposure trace.

## Connection to the complete scientific record

The [milestone map](MILESTONES.md) has 13 background milestones, M01–M13, followed by 17 narrative milestones, M14–M30. The bridge above supplies a connected route through their physical core.

| Question | Complete account |
|---|---|
| Which trajectories and resources are allowed? | [Model](../science/model.md), M12–M15 |
| Why do extra independent directions cost action? | [Spectral cost](../science/spectral_cost.md), M16–M19 |
| Why does the bound survive phase wrapping and approximation? | [Matching theorem](../science/matching.md), M20–M24 |
| What channel does vacuum loss produce, and what is optimized exactly? | [Loss and frontier](../science/loss_and_frontier.md), M25–M28 |
| What does the result require of an architecture? | [Paid resource comparison](../science/architecture.md), M29–M30 |
| Which ingredients are inherited, and what finite checks support the formulas? | [Related work](../references/related_work.md) and [verification guide](../verification/README.md) |

The selected review motivates conditional motion and geometric gates. Weighted control geometry, modular phase equivalence, and the exact resource converses have their own attributed proofs. The conclusions remain specific to independently driven, linear harmonic buses with a fixed commuting spin axis and exact conditional return. Additional modes, different control algebras, encoded mediators, measurement, and different environmental models change the resources or the problem being studied.
