# Vacuum loss and the exact force–exposure frontier

For a fixed real symmetric geometric phase matrix $`A`$, a gate time $`T`$, and $`m`$ independently controlled displacement modes, this page derives an exact optimum for the paid quadratic force cost and its tradeoff with loss exposure. The optimum includes the force needed to close the trajectory in the presence of damping. It is an optimum in the two scalar resources $`(\mathcal E,X)`$; it is not an optimum in diamond error or a hardware-independent noise threshold.

The lossless Hamiltonian, phase matrix, and force-fluence convention are fixed in the [model](model.md). This page adds common-rate vacuum Markov loss. Let $`D(t)\in\mathbb C^{m\times n}`$ collect the actual conditional displacement coefficients, with $`D_{\ell j}=\alpha_{j\ell}`$. The phase matrix remains $`A`$, the number of modes remains $`m`$, and the physical paid force fluence remains $`\mathcal E`$. Here $`n`$ is any number of qubits; a matching has $`n=2K`$. The matrix $`u=[u_{j\ell}]_{\ell,j}`$ uses mode-first indices on this page. The damped dynamics and exact closure are

```math
\dot D=u-\frac{\kappa}{2}D,\qquad D(0)=D(T)=0,
\qquad
A=\mathrm{Im}\int_0^T D^\dagger\dot D\,dt,
```

**(L1)**

```math
\Gamma=\int_0^T D^\dagger D\,dt=F+iJ,\quad
J^T=-J,\quad
X=\mathrm{tr}F,\quad
E_{\rm path}=\int_0^T\Vert \dot D\Vert _F^2dt,\quad
\mathcal E=E_{\rm path}+\frac{\kappa^2}{4}X.
```

The paid-cost identity follows by expanding $`\lVert\dot D+\kappa D/2\rVert_F^2`$: its integrated cross term is $`(\kappa/2)[\lVert D(T)\rVert_F^2-\lVert D(0)\rVert_F^2]=0`$. Exact damped closure is equivalently $`\int_0^T e^{\kappa t/2}u(t)dt=0`$. Conversely every $`D\in H_0^1`$ is attainable with the compensated force. Zero one-sided endpoint force is an additional condition.

$`X`$ has time units and is the integrated conditional occupation averaged over uniform computational strings, because $`\mathbb E_z\lVert D(t)z\rVert^2=\lVert D(t)\rVert_F^2`$. Its product $`\kappa X`$ is the corresponding mean emitted photon number. Neither $`X`$ nor the coefficient-force norm is a maximum-branch bound. Both $`E_{\rm path}`$ and $`\mathcal E`$ have inverse-time units, and $`T\mathcal E`$ remains the dimensionless force action.

Here $`\kappa`$ is the number-decay rate in the Lindblad generator $`\kappa\mathcal{D}[a]`$. All modes and input fields start in vacuum. The joint data–bus state obeys $`\dot\rho=-i[H/\hbar,\rho]+\kappa\sum_{\ell=1}^m\mathcal D[a_\ell](\rho)`$, with $`\mathcal D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2`$. Hence coherent amplitude decays at rate $`\kappa/2`$. The geometric data unitary is $`U_A\vert z\rangle=e^{iz^TAz}\vert z\rangle`$, with $`z_i\in\{+1,-1\}`$.

## 1. Exact channel, including the imaginary trajectory Gram matrix

### Coherent-state dilation

Conditional on a computational string $`z`$, linear driving and passive attenuation preserve coherent states of the joint bus and output field. At closure the branch state is

**(L2)**

```math
\vert z\rangle\vert 0\rangle_{\rm bus}\vert 0\rangle_{\rm in}
\longmapsto
e^{iz^TAz}\vert z\rangle\vert 0\rangle_{\rm bus}\vert \beta_z\rangle_{\rm out},
\qquad
\beta_z(\mu,t)=\sqrt{\kappa}\,[D(t)z]_\mu .
```

One way to derive this is to alternate infinitesimal drive displacements and vacuum beam splitters. A displacement contributes phase $`\mathrm{Im}[(Dz)^\dagger uz]dt`$; a passive beam splitter maps product coherent states to product coherent states without an additional scalar phase. Equation (L1) then gives $`\mathrm{Im}[(Dz)^\dagger uz]=\mathrm{Im}[(Dz)^\dagger\dot Dz]`$. The output amplitude is $`\sqrt{\kappa}Dz`$ and the remaining bus amplitude is zero at $`T`$. Taking the continuum limit gives (L2).

For coherent states in the output space $`L^2([0,T];\mathbb{C}^m)`$,

```math
\langle\beta_{z'}\vert \beta_z\rangle
=\exp\left[
-\frac{\Vert \beta_z\Vert ^2+\Vert \beta_{z'}\Vert ^2}{2}
+\langle\beta_{z'},\beta_z\rangle
\right].
```

Since $`\langle\beta_{z'},\beta_z\rangle=\kappa z'^T\Gamma z`$, the exact reduced data channel is the Schur multiplier

**(L3)**

```math
\mathcal{N}_D(\vert z\rangle\langle z'\vert )
=e^{i(z^TAz-z'^TAz')}\,M_{zz'}\,\vert z\rangle\langle z'\vert ,
```

**(L4)**

```math
\boxed{
M_{zz'}=
\exp\left[
-\frac{\kappa}{2}(z-z')^TF(z-z')
+i\kappa z'^TJz
\right].
}
```

The matrix $`M`$ is a Gram matrix with unit diagonal, so (L3) is completely positive and trace preserving. No perturbation in $`\kappa`$ has been made.

The second term in (L4) is generally not of the form $`\vartheta(z)-\vartheta(z')`$. Such a representation would require its phases to satisfy a cycle identity on every triple of strings. An arbitrary antisymmetric $`J`$ does not satisfy that identity. Consequently it is incorrect to discard this term or to absorb it globally into an assumed diagonal Hamiltonian.

For an equivalent spin-only description, define $`L_{\mu,t}=\sqrt{\kappa}\sum_iD_{\mu i}(t)Z_i`$ for each bus. The relative channel $`\mathcal{U}_A^\dagger\circ\mathcal{N}_D`$ is the exponential of the integrated diagonal dissipators $`\sum_\mu\int_0^T\mathcal{D}[L_{\mu,t}]dt`$. Their action on $`\vert z\rangle\langle z'\vert `$ is exactly the exponent in (L4), and these superoperators commute. Complex diagonal jump amplitudes retain the $`J`$ term.

If $`J=0`$, (L4) is classical Gaussian phase noise: average $`e^{i\xi^T\mathbf{Z}}`$ over a real Gaussian vector with covariance $`\kappa F`$. If also $`F`$ is diagonal, this factors into independent one-qubit dephasing channels with

```math
p_i=\frac{1-e^{-2\kappa F_{ii}}}{2}
```

as the probability of $`Z_i`$. Correlated errors are therefore not unavoidable in this model. Explicit sequences producing independent single-qubit dephasing while retaining the desired conditional phase were already constructed by [Louis et al., Eqs. (35)–(40)](https://arxiv.org/pdf/0804.3240).

### Environmental rank and physical mode count

The real Gram matrix $`F`$ describes the real span of the output displacement records; $`\Gamma=F+iJ`$ describes their complex span. The [Gram inequality](spectral_cost.md#7-phase-exposure-and-trajectory-energy) implies $`\operatorname{rank}F\ge\operatorname{rank}A`$, while $`\operatorname{rank}F\le2\operatorname{rank}\Gamma`$. For one row $`D(t)=f(t)(1,1,i,i)`$ with a closed scalar path of nonzero area, $`\operatorname{rank}\Gamma=1`$ and $`\operatorname{rank}F=\operatorname{rank}A=2`$. Thus real record rank is not the count of complex jump operators or physical modes. One physical mode can emit many temporal directions; the area spectrum charges their cost.

### Relation to earlier dissipative geometric-gate analysis

The basic loss mechanism is inherited. [Müller, Luoma and Strunz, Sec. III.1](https://arxiv.org/html/1907.08033v2#S3.SS1) analyze a damped coherent branch pair and obtain both attenuation determined by path separation and an additional dissipative phase. Their Sec. III.2 gives damped closure conditions and discusses reducing dephasing by increasing angular motion at fixed area. Equation (L4) states those mechanisms for an arbitrary number of independently driven data coefficients in one matrix convention. Its normalization follows directly from (L2). Independent complex quadratures enable the arbitrary path-preserving compensation $`u=\dot D+\kappa D/2`$ used here; a real laboratory-force restriction must be imposed separately.

## 2. Operational error and first-order gate metrics

### A nonperturbative floor relative to any unitary target

Let $`\mathcal{V}`$ be any unitary channel on the data, and let

```math
\epsilon_V=\frac12\Vert \mathcal{N}_D-\mathcal{V}\Vert _\diamond .
```

For a sign vector $`s`$, apply the channel to

```math
\vert \psi_s\rangle=\frac{\vert s\rangle+\vert -s\rangle}{\sqrt2}.
```

The output remains in this two-dimensional span with equal populations. Its off-diagonal magnitude is $`a_s/2`$, where

```math
a_s=e^{-2\kappa s^TFs}.
```

Indeed, $`s^TAs=(-s)^TA(-s)`$ and $`s^TJs=0`$. Local diagonal corrections would change only the off-diagonal phase and not the following argument. The output eigenvalues are $`(1\pm a_s)/2`$. The target output $`\mathcal{V}(\vert \psi_s\rangle\langle\psi_s\vert )`$ is pure. Its trace distance from the actual output is at least $`1-\lambda_{\max}=(1-a_s)/2`$: measure the projector onto that target pure state and use its expectation value at most $`\lambda_{\max}`$.

The diamond norm dominates this particular input distinguishability. Averaging $`s^TFs`$ over independent uniform signs gives $`\mathrm{tr}F=X`$, so at least one sign vector has $`s^TFs\geq X`$. Hence

**(L5)**

```math
\boxed{
\epsilon_V\geq
\frac{1-e^{-2\kappa\max_s s^TFs}}{2}
\geq\frac{1-e^{-2\kappa X}}{2}.
}
```

The bound applies in particular to the intended diagonal gate, whether or not its phase matrix equals $`A`$. For $`\kappa\gt 0`$, achieving $`\epsilon_V\leq\epsilon\lt 1/2`$ requires

**(L6)**

```math
X\leq\frac{-\log(1-2\epsilon)}{2\kappa}.
```

This is a global gate criterion, not a local stochastic error parameter. The bound may be strict.

### Entanglement and average gate fidelity

For comparison specifically with $`\mathcal{U}_A`$, write $`d=2^n`$. The entanglement fidelity on a maximally entangled input is exactly

**(L7)**

```math
F_{\rm e}(\mathcal{N}_D,\mathcal{U}_A)
=\frac{1}{d^2}\sum_{z,z'}M_{zz'}.
```

The sum is real because terms for $`(z,z')`$ and $`(z',z)`$ are conjugate. With a fixed closed trajectory held in place by its compensated drive, expansion at $`\kappa=0`$ gives

```math
\mathbb{E}_{z,z'}[(z-z')^TF(z-z')]=2X,\qquad
\mathbb{E}_{z,z'}[z'^TJz]=0,
```

and therefore

**(L8)**

```math
1-F_{\rm e}=\kappa X+O(\kappa^2).
```

The usual exact identity $`F_{\rm av}=(dF_{\rm e}+1)/(d+1)`$ gives

**(L9)**

```math
1-F_{\rm av}
=\frac{d}{d+1}\kappa X+O(\kappa^2).
```

For the fidelity identity, see [Nielsen, Eq. (3)](https://arxiv.org/html/quant-ph/0205035v2). The expansion is at fixed finite $`n`$ and fixed trajectory; its remainder is not claimed uniform in system size or in a control family whose amplitudes diverge. A sufficient uniform small parameter for a particular finite family is the largest magnitude of the exponent in (L4), not just its mean.

Beyond first order, even entanglement fidelity depends on more than $`X`$. Diamond error also depends on the structure of $`F`$ and $`J`$. Minimizing $`X`$ is therefore not equivalent to minimizing the complete channel error.

### Finite control cost implies a positive loss floor

The [phase–exposure inequality](spectral_cost.md#7-phase-exposure-and-trajectory-energy) gives $`\mathcal E X\geq E_{\rm path}X\geq\Vert A\Vert _*^2`$. If $`\mathcal E\leq \mathcal E_{\max}`$ and $`A\neq0`$, then

**(L10)**

```math
X\geq\frac{\Vert A\Vert _*^2}{\mathcal E_{\max}},\qquad
\epsilon_V\geq
\frac{1-\exp[-2\kappa\Vert A\Vert _*^2/\mathcal E_{\max}]}{2}.
```

This is a necessary bound at the realized $`A`$. For a gate-level statement, its allowed phase representatives and diagonal completions must still be accounted for; the [direct noisy matching converse](gate_layer_bounds.md#10-direct-converse-for-the-vacuum-lossy-channel) supplies this step. The exact fixed-$`A`$ force–exposure tradeoff below can strengthen the scalar estimate. With unbounded control cost, no positive exposure floor is asserted.

## 3. Spectrum of the closed-loop area operator

Fix $`\lambda\geq0`$. On the complex Hilbert space $`\mathcal{H}=H^1_0(0,T;\mathbb{C})`$ define

**(L11)**

```math
q_\lambda(f,g)=\int_0^T
(\dot f^*\dot g+\lambda f^*g)\,dt,\qquad
\mathfrak{a}(f,g)=\int_0^T f^*(-i\dot g)\,dt.
```

Dirichlet Poincaré makes $`q_\lambda`$ coercive even when $`\lambda=0`$. Integration by parts makes $`\mathfrak{a}`$ Hermitian. Its real part is the real symmetric bilinear area form

```math
\mathrm{Re}\mathfrak{a}(f,g)
=\mathrm{Im}\int_0^T f^*\dot g\,dt.
```

There is a bounded $`q_\lambda`$-self-adjoint operator $`\mathsf{T}_\lambda`$ with $`q_\lambda(f,\mathsf{T}_\lambda g)=\mathfrak{a}(f,g)`$. In weak form,

```math
\mathsf{T}_\lambda=Q_\lambda^{-1}(-i\partial_t),
\qquad
Q_\lambda=-\partial_t^2+\lambda
```

with Dirichlet conditions. The derivative maps $`H^1_0`$ boundedly into $`L^2`$; the inverse $`Q_\lambda^{-1}`$ maps $`L^2`$ into $`H^2\cap H^1_0`$; and this space embeds compactly into $`H^1_0`$ on a finite interval. Thus $`\mathsf{T}_\lambda`$ is compact. Its kernel is trivial: $`\mathfrak{a}(f,g)=0`$ for every test function forces $`\dot g=0`$, and the endpoints then force $`g=0`$.

For a nonzero eigenvalue $`\rho`$, the eigenfunction obeys

**(L12)**

```math
-i\dot f=\rho(-\ddot f+\lambda f),\qquad f(0)=f(T)=0.
```

Set $`f(t)=e^{it/(2\rho)}y(t)`$. Then

```math
\ddot y+\left(\frac{1}{4\rho^2}-\lambda\right)y=0,
\qquad y(0)=y(T)=0.
```

A nonzero solution requires the coefficient to be $`(k\pi/T)^2`$ for an integer $`k\geq1`$. Therefore the complete nonzero spectrum is

**(L13)**

```math
\boxed{
\rho_{k,\pm}=\pm\frac{1}{2\omega_k},\qquad
\omega_k=\sqrt{(k\pi/T)^2+\lambda},
\qquad
f_{k,\pm}(t)=e^{\pm i\omega_k t}\sin(k\pi t/T).
}
```

The ODE excludes any other eigenvalues. The compact self-adjoint spectral theorem, together with the trivial kernel, gives a complete $`q_\lambda`$-orthogonal eigenbasis. For $`m`$ modes, each signed eigenvalue has complex multiplicity $`m`$ and real multiplicity $`2m`$. This real multiplicity is the source of the factor $`2m`$ below.

Useful normalizations are

**(L14)**

```math
\int_0^T\vert f_{k,\pm}\vert ^2dt=\frac T2,\qquad
q_\lambda(f_{k,\pm},f_{k,\pm})=T\omega_k^2,\qquad
\mathfrak{a}(f_{k,\pm},f_{k,\pm})=\pm\frac{T\omega_k}{2}.
```

When $`\lambda=0`$, these eigenfunctions are proportional to the closed Fourier loops $`e^{\pm 2\pi ikt/T}-1`$.

## 4. Exact minimum of a priced trajectory cost

Let

```math
\ell_1^+\geq\ell_2^+\geq\cdots\gt 0,\qquad
\ell_1^-\geq\ell_2^-\geq\cdots\gt 0
```

be the positive eigenvalues of $`A`$ and the magnitudes of its negative eigenvalues. The two lists are indexed separately. Set $`r_j=\lceil j/(2m)\rceil`$.

**Theorem.** For every real symmetric $`A`$, $`T\gt 0`$, $`m\geq1`$, and $`\lambda\geq0`$,

**(L15)**

```math
\boxed{
\min_{\substack{D\in H^1_0([0,T];\mathbb{C}^{m\times n})\\
 \mathrm{Im}\int D^\dagger\dot D=A}}
(E_{\rm path}+\lambda X)
 =
2\sum_{\sigma\in\{+,-\}}\sum_j
\sqrt{(r_j\pi/T)^2+\lambda}\,\ell_j^\sigma .
}
```

The minimum is attained by a finite sum of the modes (L13).

### Lower bound

Expand the trajectory columns in a real $`q_\lambda`$-orthonormal eigenbasis of the $`m`$-mode area operator. For each signed eigenvalue there are $`2m`$ real coefficients per column. Consequently

```math
A=\sum_{k\geq1}(X_k-Y_k),\qquad
X_k,Y_k\succeq0,\qquad
\mathrm{rank}X_k,\mathrm{rank}Y_k\leq2m,
```

**(L16)**

```math
E_{\rm path}+\lambda X=\sum_{k\geq1}s_k\mathrm{tr}(X_k+Y_k),
\qquad
s_k=2\sqrt{(k\pi/T)^2+\lambda}.
```

For example, if the real coefficient matrix at positive mode $`k`$ is $`B_k`$, then $`X_k=\rho_{k,+}B_k^TB_k`$, and its cost is $`\mathrm{tr}(B_k^TB_k)=s_k\mathrm{tr}X_k`$.

Write $`X_+=\sum_kX_k`$. The partial sum through $`k=l`$ is bounded above by $`X_+`$ and has rank at most $`2ml`$. The variational principle for eigenvalue sums yields

```math
\mathrm{tr}\left(X_+-\sum_{k\leq l}X_k\right)
\geq\sum_{j\gt 2ml}\lambda_j(X_+).
```

Because $`s_k`$ is increasing,

**(L17)**

```math
\begin{aligned}
\sum_{k\geq1}s_k\mathrm{tr}X_k
&=s_1\mathrm{tr}X_+
 +\sum_{l\geq1}(s_{l+1}-s_l)
   \mathrm{tr}\left(X_+-\sum_{k\leq l}X_k\right)\\
&\geq\sum_j s_{r_j}\lambda_j(X_+)
\geq\sum_j s_{r_j}\ell_j^+ .
\end{aligned}
```

The last step uses $`X_+\succeq A`$ and eigenvalue monotonicity; extra nonnegative terms can be dropped. Applying the same argument to $`X_-=\sum_kY_k\succeq-A`$ gives the negative list. Finite cost ensures convergence, and the nonnegative tail sums justify the infinite-dimensional passage.

### Explicit attaining trajectories

Choose real orthonormal eigenvectors $`q_j^\sigma`$ of $`A`$ with eigenvalues $`\sigma\ell_j^\sigma`$. Within each group having fixed $`(\sigma,r_j)`$, choose bus vectors $`v_j^\sigma\in\mathbb{C}^m`$ satisfying

```math
\mathrm{Re}\bigl[(v_i^\sigma)^\dagger v_j^\sigma\bigr]=\delta_{ij}.
```

There are at most $`2m`$ vectors in each group, so this is possible using the real and imaginary quadratures of the $`m`$ standard mode vectors. Vectors can be reused in different signed temporal modes. Then

**(L18)**

```math
\boxed{
D(t)=\sum_{\sigma,j}
\sqrt{\frac{2\ell_j^\sigma}{T\omega_{r_j}}}\,
v_j^\sigma(q_j^\sigma)^T
e^{\sigma i\omega_{r_j}t}
\sin(r_j\pi t/T)
}
```

has zero endpoints and exactly the prescribed $`A`$. Different temporal eigenmodes are area-orthogonal; within a degenerate mode, the real orthogonality of the $`v_j^\sigma`$ gives the required independent directions. Equations (L14) show that each term pays $`2\omega_{r_j}\ell_j^\sigma`$, attaining (L15).

This is a precise use of independent complex coupling control. It does not imply that a platform with a fixed global force pattern can implement (L18).

### Lossless specialization and mathematical inheritance

At $`\lambda=0`$,

**(L19)**

```math
E_{\rm path,min}(A,T,m)=\frac{2\pi}{T}\Phi_m(A),\qquad
\Phi_m(A)=\sum_{\sigma,j}
\left\lceil\frac{j}{2m}\right\rceil\ell_j^\sigma.
```

The weighted spectral optimization method has close prior art. [Wong and Baillieul, Theorem 5.1 and Corollary 5.1](https://arxiv.org/pdf/1201.6527v2) give exact weighted singular-value control costs for bilinear target maps, including closed Brockett–Heisenberg loops. Related rank-weighted area formulas appear in [Rizzi and Serres, Appendix A, Proposition 15](https://arxiv.org/html/1610.01596v2#A1). Equations (L13)–(L18) give the symmetric signed-area and exposure-priced specialization used here; they do not claim that weighted bilinear control cost or matrix isoperimetry originated in this project.

## 5. Paid damping and the complete fixed-$`A`$ exposure frontier

The physical drive cost is obtained by setting $`\lambda=\kappa^2/4`$ in (L15):

**(L20)**

```math
\boxed{
\mathcal E_{\min}(A,T,m,\kappa)=
\sum_{\sigma,j}
\sqrt{(2\pi r_j/T)^2+\kappa^2}\,\ell_j^\sigma .
}
```

To price exposure, minimize $`\mathcal E+\mu X`$ for $`\mu\geq0`$. This is (L15) with $`\lambda=\kappa^2/4+\mu`$. Define

**(L21)**

```math
a_j=(r_j\pi/T)^2+\frac{\kappa^2}{4},\qquad
S(\mu)=2\sum_{\sigma,j}\ell_j^\sigma\sqrt{a_j+\mu}.
```

The attaining pulse (L18), with $`\omega_{r_j}=\sqrt{a_j+\mu}`$ and physical force $`u=\dot D+\kappa D/2`$, has

**(L22)**

```math
\boxed{
X(\mu)=\sum_{\sigma,j}
\frac{\ell_j^\sigma}{\sqrt{a_j+\mu}},
\qquad
\mathcal E(\mu)=\sum_{\sigma,j}
\frac{(2a_j+\mu)\ell_j^\sigma}{\sqrt{a_j+\mu}} .
}
```

These expressions can be checked directly: the trace over data coordinates removes cross terms between the orthogonal $`q_j^\sigma`$; a mode carrying area magnitude $`\ell`$ has exposure $`\ell/\omega`$. Its derivative cost plus $`\kappa^2X/4`$ gives the second expression. Equivalently, $`S'(\mu)=X(\mu)`$ and $`\mathcal E(\mu)=S(\mu)-\mu X(\mu)`$.

### Why this is the whole nondominated $`(\mathcal E,X)`$ frontier

Assume $`A\neq0`$. The function $`X(\mu)`$ is continuous and strictly decreasing from $`X(0)\gt 0`$ to zero. Every exposure $`0\lt X\leq X(0)`$ therefore has a unique parameter $`\mu\geq0`$. For any competing admissible trajectory with exposure $`\widetilde X\leq X(\mu)`$, the supporting bound (L15) gives

```math
\widetilde{\mathcal E}+\mu\widetilde X\geq S(\mu)
=\mathcal E(\mu)+\mu X(\mu),
```

so $`\widetilde{\mathcal E}\geq \mathcal E(\mu)`$. At equal exposure, (L18) attains this lower bound. Any point with exposure larger than $`X(0)`$ has cost at least $`\mathcal E(0)`$ and is dominated by the $`\mu=0`$ solution. Thus (L22) describes all nondominated resource pairs.

Also $`\mathcal E'(\mu)=-\mu X'(\mu)\gt 0`$ for $`\mu\gt 0`$. Given a budget $`\mathcal E_{\max}\geq \mathcal E(0)`$, its exact minimum achievable exposure is found by the unique $`\mu`$ satisfying $`\mathcal E(\mu)=\mathcal E_{\max}`$, with $`\mu=0`$ at equality. A budget below $`\mathcal E(0)`$ cannot realize this full matrix $`A`$. If $`A=0`$, the zero trajectory dominates all others.

### Limits and interpretation

Let $`L=\Vert A\Vert _*=\sum_{\sigma,j}\ell_j^\sigma`$. At large exposure price,

**(L23)**

```math
X(\mu)\sim\frac{L}{\sqrt{\mu}},
\qquad
\mathcal E(\mu)\sim L\sqrt{\mu},
\qquad
\mathcal E(\mu)X(\mu)\longrightarrow L^2.
```

Arbitrarily small exposure is therefore possible only by sending the control cost to infinity in this unrestricted waveform model. The optimal pulses also acquire arbitrarily rapid phase rotation. A force, occupation, slew, or modulation constraint changes the feasible problem.

For finite $`\mathcal E_{\max}`$, inserting the exact minimum exposure from (L22) into (L5) gives a rigorous error lower bound. It does **not** establish a matching achievable diamond error: two attaining pulses with the same $`X`$ can have different full $`F`$ and $`J`$, and (L5) itself can be loose. The frontier concerns the specified $`A`$; optimizing over gate-equivalent diagonal completions or phase lifts is a further problem.

The spectral construction optimizes integrated force cost. Its damped pulses need not satisfy a separately specified instantaneous force cap at the same numerical value $`\mathcal E/T`$. A converse may use $`\mathcal E\leq PT`$ when such a cap is given, but attainment under that cap requires its own pulse analysis.

## 6. Attribution and remaining boundaries

The following distinctions are essential when using these formulas in an architectural claim.

- **Established dissipative physics.** [Louis et al.](https://arxiv.org/pdf/0804.3240) derive effective qubit operations from lossy bus overlaps in a sequential transfer model; their paired sequences remove correlated terms. [Müller, Luoma and Strunz](https://arxiv.org/html/1907.08033v2) treat Markovian damped geometric gates, including extra phases, loss of coherence, and adapted closure. Neither generic loss-induced dephasing nor compensation of endpoint closure is claimed as new.
- **Inherited mathematical method.** The spectral allocation and rank-tail strategy is closely related to the exact bilinear control optimization of [Wong and Baillieul](https://arxiv.org/pdf/1201.6527v2) and the geometric area formulas of [Rizzi and Serres](https://arxiv.org/html/1610.01596v2). The signed multiplicity and damped cost are derived explicitly here, with no priority claim for the underlying method.
- **Exact statements for this model.** The common normalization yields the paid force fluence (L20), the attaining exposure frontier (L22), and the target-independent loss lower bound (L5). These connect finite bus resources to quantum-gate requirements.
- **Additional physics.** The formulas assume vacuum input, a common Markovian loss rate, a harmonic bus, exact conditional closure, independent complex coupling controls, and a fixed commuting data axis. Non-vacuum preparation, monitored loss, nonlinear or encoded buses, free squeezing, interspersed noncommuting data control, and approximate residual bus return require separate analysis.
- **Gate error and fault tolerance.** Neither $`X`$ nor the global diamond lower bound is a local fault-tolerance noise model. No threshold, unavoidable correlated-error statement, or exact noisy-gate optimum follows from these scalar resources alone.
