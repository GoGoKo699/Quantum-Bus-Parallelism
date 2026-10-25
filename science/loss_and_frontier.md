# Vacuum loss and the exact force–exposure frontier

For a fixed real symmetric geometric phase matrix $`K`$, a gate time $`T`$, and $`b`$ independently controlled displacement buses, this page derives an exact optimum for the paid quadratic force cost and its tradeoff with loss exposure. The optimum includes the force needed to close the trajectory in the presence of damping. It is an optimum in the two scalar resources $`(G,X)`$; it is not an optimum in diamond error or a hardware-independent noise threshold.

The dynamics, closure condition, and normalization are specified in [model.md](model.md). In particular,

```math
\dot A=u-\frac{\kappa}{2}A,\qquad A(0)=A(T)=0,
\qquad
K=\mathrm{Im}\int_0^T A^\dagger\dot A\,dt,
```

**(L1)**

```math
C=\int_0^T A^\dagger A\,dt=F+iJ,\quad
J^T=-J,\quad
X=\mathrm{tr}F,\quad
E=\int_0^T\Vert \dot A\Vert _F^2dt,\quad
G=E+\frac{\kappa^2}{4}X.
```

Here $`\kappa`$ is the number-decay rate in the Lindblad generator $`\kappa\mathcal{D}[a]`$. All buses and input fields start in vacuum. The geometric data unitary is $`U_K\vert z\rangle=e^{iz^TKz}\vert z\rangle`$, with $`z_i\in\{+1,-1\}`$.

## 1. Exact channel, including the imaginary trajectory Gram matrix

### Coherent-state dilation

Conditional on a computational string $`z`$, linear driving and passive attenuation preserve coherent states of the joint bus and output field. At closure the branch state is

**(L2)**

```math
\vert z\rangle\vert 0\rangle_{\rm bus}\vert 0\rangle_{\rm in}
\longmapsto
e^{iz^TKz}\vert z\rangle\vert 0\rangle_{\rm bus}\vert \beta_z\rangle_{\rm out},
\qquad
\beta_z(\mu,t)=\sqrt{\kappa}\,[A(t)z]_\mu .
```

One way to derive this is to alternate infinitesimal drive displacements and vacuum beam splitters. A displacement contributes phase $`\mathrm{Im}[(Az)^\dagger uz]dt`$; a passive beam splitter maps product coherent states to product coherent states without an additional scalar phase. Equation (L1) then gives $`\mathrm{Im}[(Az)^\dagger uz]=\mathrm{Im}[(Az)^\dagger\dot Az]`$. The output amplitude is $`\sqrt{\kappa}Az`$ and the remaining bus amplitude is zero at $`T`$. Taking the continuum limit gives (L2).

For coherent states in the output space $`L^2([0,T];\mathbb{C}^b)`$,

```math
\langle\beta_{z'}\vert \beta_z\rangle
=\exp\left[
-\frac{\Vert \beta_z\Vert ^2+\Vert \beta_{z'}\Vert ^2}{2}
+\langle\beta_{z'},\beta_z\rangle
\right].
```

Since $`\langle\beta_{z'},\beta_z\rangle=\kappa z'^TCz`$, the exact reduced data channel is the Schur multiplier

**(L3)**

```math
\mathcal{E}_A(\vert z\rangle\langle z'\vert )
=e^{i(z^TKz-z'^TKz')}\,M_{zz'}\,\vert z\rangle\langle z'\vert ,
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

For an equivalent spin-only description, define $`L_{\mu,t}=\sqrt{\kappa}\sum_i\alpha_{\mu i}(t)Z_i`$ for each bus. The relative channel $`\mathcal{U}_K^\dagger\circ\mathcal{E}_A`$ is the exponential of the integrated diagonal dissipators $`\sum_\mu\int_0^T\mathcal{D}[L_{\mu,t}]dt`$. Their action on $`\vert z\rangle\langle z'\vert `$ is exactly the exponent in (L4), and these superoperators commute. Complex diagonal jump amplitudes retain the $`J`$ term.

If $`J=0`$, (L4) is classical Gaussian phase noise: average $`e^{i\xi^T\mathbf{Z}}`$ over a real Gaussian vector with covariance $`\kappa F`$. If also $`F`$ is diagonal, this factors into independent one-qubit dephasing channels with

```math
p_i=\frac{1-e^{-2\kappa F_{ii}}}{2}
```

as the probability of $`Z_i`$. Correlated errors are therefore not unavoidable in this model. Explicit sequences producing independent single-qubit dephasing while retaining the desired conditional phase were already constructed by [Louis et al., Eqs. (35)–(40)](https://arxiv.org/pdf/0804.3240).

### Relation to earlier dissipative geometric-gate analysis

The basic loss mechanism is inherited. [Müller, Luoma and Strunz, Sec. III.1](https://arxiv.org/html/1907.08033v2#S3.SS1) analyze a damped coherent branch pair and obtain both attenuation determined by path separation and an additional dissipative phase. Their Sec. III.2 gives damped closure conditions and discusses reducing dephasing by increasing angular motion at fixed area. Equation (L4) states those mechanisms for an arbitrary number of independently driven data coefficients in one matrix convention. Its normalization follows directly from (L2). Independent complex quadratures enable the arbitrary path-preserving compensation $`u=\dot A+\kappa A/2`$ used here; a real laboratory-force restriction must be imposed separately.

## 2. Operational error and first-order gate metrics

### A nonperturbative floor relative to any unitary target

Let $`\mathcal{V}`$ be any unitary channel on the data, and let

```math
\epsilon_V=\frac12\Vert \mathcal{E}_A-\mathcal{V}\Vert _\diamond .
```

For a sign vector $`s`$, apply the channel to

```math
\vert \psi_s\rangle=\frac{\vert s\rangle+\vert -s\rangle}{\sqrt2}.
```

The output remains in this two-dimensional span with equal populations. Its off-diagonal magnitude is $`a_s/2`$, where

```math
a_s=e^{-2\kappa s^TFs}.
```

Indeed, $`s^TKs=(-s)^TK(-s)`$ and $`s^TJs=0`$. Local diagonal corrections would change only the off-diagonal phase and not the following argument. The output eigenvalues are $`(1\pm a_s)/2`$. The target output $`\mathcal{V}(\vert \psi_s\rangle\langle\psi_s\vert )`$ is pure. Its trace distance from the actual output is at least $`1-\lambda_{\max}=(1-a_s)/2`$: measure the projector onto that target pure state and use its expectation value at most $`\lambda_{\max}`$.

The diamond norm dominates this particular input distinguishability. Averaging $`s^TFs`$ over independent uniform signs gives $`\mathrm{tr}F=X`$, so at least one sign vector has $`s^TFs\geq X`$. Hence

**(L5)**

```math
\boxed{
\epsilon_V\geq
\frac{1-e^{-2\kappa\max_s s^TFs}}{2}
\geq\frac{1-e^{-2\kappa X}}{2}.
}
```

The bound applies in particular to the intended diagonal gate, whether or not its phase matrix equals $`K`$. For $`\kappa\gt 0`$, achieving $`\epsilon_V\leq\epsilon\lt 1/2`$ requires

**(L6)**

```math
X\leq\frac{-\log(1-2\epsilon)}{2\kappa}.
```

This is a global gate criterion, not a local stochastic error parameter. The bound may be strict.

### Entanglement and average gate fidelity

For comparison specifically with $`\mathcal{U}_K`$, write $`d=2^n`$. The entanglement fidelity on a maximally entangled input is exactly

**(L7)**

```math
F_{\rm e}(\mathcal{E}_A,\mathcal{U}_K)
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

The phase–exposure inequality in [model.md](model.md) gives $`GX\geq EX\geq\Vert K\Vert _*^2`$. If $`G\leq G_{\max}`$ and $`K\neq0`$, then

**(L10)**

```math
X\geq\frac{\Vert K\Vert _*^2}{G_{\max}},\qquad
\epsilon_V\geq
\frac{1-\exp[-2\kappa\Vert K\Vert _*^2/G_{\max}]}{2}.
```

This is a necessary bound at the realized $`K`$. For a gate-level statement, its allowed phase representatives and diagonal completions must still be accounted for. The exact fixed-$`K`$ force–exposure tradeoff below can strengthen the scalar estimate. With unbounded control cost, no positive exposure floor is asserted.

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

The ODE excludes any other eigenvalues. The compact self-adjoint spectral theorem, together with the trivial kernel, gives a complete $`q_\lambda`$-orthogonal eigenbasis. For $`b`$ buses, each signed eigenvalue has complex multiplicity $`b`$ and real multiplicity $`2b`$. This real multiplicity is the source of the factor $`2b`$ below.

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

be the positive eigenvalues of $`K`$ and the magnitudes of its negative eigenvalues. The two lists are indexed separately. Set $`r_j=\lceil j/(2b)\rceil`$.

**Theorem.** For every real symmetric $`K`$, $`T\gt 0`$, $`b\geq1`$, and $`\lambda\geq0`$,

**(L15)**

```math
\boxed{
\min_{\substack{A\in H^1_0([0,T];\mathbb{C}^{b\times n})\\
 \mathrm{Im}\int A^\dagger\dot A=K}}
(E+\lambda X)
 =
2\sum_{\sigma\in\{+,-\}}\sum_j
\sqrt{(r_j\pi/T)^2+\lambda}\,\ell_j^\sigma .
}
```

The minimum is attained by a finite sum of the modes (L13).

### Lower bound

Expand the trajectory columns in a real $`q_\lambda`$-orthonormal eigenbasis of the $`b`$-bus area operator. For each signed eigenvalue there are $`2b`$ real coefficients per column. Consequently

```math
K=\sum_{k\geq1}(X_k-Y_k),\qquad
X_k,Y_k\succeq0,\qquad
\mathrm{rank}X_k,\mathrm{rank}Y_k\leq2b,
```

**(L16)**

```math
E+\lambda X=\sum_{k\geq1}s_k\mathrm{tr}(X_k+Y_k),
\qquad
s_k=2\sqrt{(k\pi/T)^2+\lambda}.
```

For example, if the real coefficient matrix at positive mode $`k`$ is $`B_k`$, then $`X_k=\rho_{k,+}B_k^TB_k`$, and its cost is $`\mathrm{tr}(B_k^TB_k)=s_k\mathrm{tr}X_k`$.

Write $`X_+=\sum_kX_k`$. The partial sum through $`k=l`$ is bounded above by $`X_+`$ and has rank at most $`2bl`$. The variational principle for eigenvalue sums yields

```math
\mathrm{tr}\left(X_+-\sum_{k\leq l}X_k\right)
\geq\sum_{j\gt 2bl}\lambda_j(X_+).
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

The last step uses $`X_+\succeq K`$ and eigenvalue monotonicity; extra nonnegative terms can be dropped. Applying the same argument to $`X_-=\sum_kY_k\succeq-K`$ gives the negative list. Finite cost ensures convergence, and the nonnegative tail sums justify the infinite-dimensional passage.

### Explicit attaining trajectories

Choose real orthonormal eigenvectors $`q_j^\sigma`$ of $`K`$ with eigenvalues $`\sigma\ell_j^\sigma`$. Within each group having fixed $`(\sigma,r_j)`$, choose bus vectors $`v_j^\sigma\in\mathbb{C}^b`$ satisfying

```math
\mathrm{Re}\bigl[(v_i^\sigma)^\dagger v_j^\sigma\bigr]=\delta_{ij}.
```

There are at most $`2b`$ vectors in each group, so this is possible using the real and imaginary quadratures of the $`b`$ standard bus vectors. Vectors can be reused in different signed temporal modes. Then

**(L18)**

```math
\boxed{
A(t)=\sum_{\sigma,j}
\sqrt{\frac{2\ell_j^\sigma}{T\omega_{r_j}}}\,
v_j^\sigma(q_j^\sigma)^T
e^{\sigma i\omega_{r_j}t}
\sin(r_j\pi t/T)
}
```

has zero endpoints and exactly the prescribed $`K`$. Different temporal eigenmodes are area-orthogonal; within a degenerate mode, the real orthogonality of the $`v_j^\sigma`$ gives the required independent directions. Equations (L14) show that each term pays $`2\omega_{r_j}\ell_j^\sigma`$, attaining (L15).

This is a precise use of independent complex coupling control. It does not imply that a platform with a fixed global force pattern can implement (L18).

### Lossless specialization and mathematical inheritance

At $`\lambda=0`$,

**(L19)**

```math
E_{\min}(K,T,b)=\frac{2\pi}{T}\Phi_b(K),\qquad
\Phi_b(K)=\sum_{\sigma,j}
\left\lceil\frac{j}{2b}\right\rceil\ell_j^\sigma.
```

The weighted spectral optimization method has close prior art. [Wong and Baillieul, Theorem 5.1 and Corollary 5.1](https://arxiv.org/pdf/1201.6527v2) give exact weighted singular-value control costs for bilinear target maps, including closed Brockett–Heisenberg loops. Related rank-weighted area formulas appear in [Rizzi and Serres, Appendix A, Proposition 15](https://arxiv.org/html/1610.01596v2#A1). Equations (L13)–(L18) give the symmetric signed-area and exposure-priced specialization used here; they do not claim that weighted bilinear control cost or matrix isoperimetry originated in this project.

## 5. Paid damping and the complete fixed-$`K`$ exposure frontier

The physical drive cost is obtained by setting $`\lambda=\kappa^2/4`$ in (L15):

**(L20)**

```math
\boxed{
G_{\min}(K,T,b,\kappa)=
\sum_{\sigma,j}
\sqrt{(2\pi r_j/T)^2+\kappa^2}\,\ell_j^\sigma .
}
```

To price exposure, minimize $`G+\mu X`$ for $`\mu\geq0`$. This is (L15) with $`\lambda=\kappa^2/4+\mu`$. Define

**(L21)**

```math
a_j=(r_j\pi/T)^2+\frac{\kappa^2}{4},\qquad
S(\mu)=2\sum_{\sigma,j}\ell_j^\sigma\sqrt{a_j+\mu}.
```

The attaining pulse (L18), with $`\omega_{r_j}=\sqrt{a_j+\mu}`$ and physical force $`u=\dot A+\kappa A/2`$, has

**(L22)**

```math
\boxed{
X(\mu)=\sum_{\sigma,j}
\frac{\ell_j^\sigma}{\sqrt{a_j+\mu}},
\qquad
G(\mu)=\sum_{\sigma,j}
\frac{(2a_j+\mu)\ell_j^\sigma}{\sqrt{a_j+\mu}} .
}
```

These expressions can be checked directly: the trace over data coordinates removes cross terms between the orthogonal $`q_j^\sigma`$; a mode carrying area magnitude $`\ell`$ has exposure $`\ell/\omega`$. Its derivative cost plus $`\kappa^2X/4`$ gives the second expression. Equivalently, $`S'(\mu)=X(\mu)`$ and $`G(\mu)=S(\mu)-\mu X(\mu)`$.

### Why this is the whole nondominated $`(G,X)`$ frontier

Assume $`K\neq0`$. The function $`X(\mu)`$ is continuous and strictly decreasing from $`X(0)\gt 0`$ to zero. Every exposure $`0\lt X\leq X(0)`$ therefore has a unique parameter $`\mu\geq0`$. For any competing admissible trajectory with exposure $`\widetilde X\leq X(\mu)`$, the supporting bound (L15) gives

```math
\widetilde G+\mu\widetilde X\geq S(\mu)
=G(\mu)+\mu X(\mu),
```

so $`\widetilde G\geq G(\mu)`$. At equal exposure, (L18) attains this lower bound. Any point with exposure larger than $`X(0)`$ has cost at least $`G(0)`$ and is dominated by the $`\mu=0`$ solution. Thus (L22) describes all nondominated resource pairs.

Also $`G'(\mu)=-\mu X'(\mu)\gt 0`$ for $`\mu\gt 0`$. Given a budget $`G_{\max}\geq G(0)`$, its exact minimum achievable exposure is found by the unique $`\mu`$ satisfying $`G(\mu)=G_{\max}`$, with $`\mu=0`$ at equality. A budget below $`G(0)`$ cannot realize this full matrix $`K`$. If $`K=0`$, the zero trajectory dominates all others.

### Limits and interpretation

Let $`L=\Vert K\Vert _*=\sum_{\sigma,j}\ell_j^\sigma`$. At large exposure price,

**(L23)**

```math
X(\mu)\sim\frac{L}{\sqrt{\mu}},
\qquad
G(\mu)\sim L\sqrt{\mu},
\qquad
G(\mu)X(\mu)\longrightarrow L^2.
```

Arbitrarily small exposure is therefore possible only by sending the control cost to infinity in this unrestricted waveform model. The optimal pulses also acquire arbitrarily rapid phase rotation. A force, occupation, slew, or modulation constraint changes the feasible problem.

For finite $`G_{\max}`$, inserting the exact minimum exposure from (L22) into (L5) gives a rigorous error lower bound. It does **not** establish a matching achievable diamond error: two attaining pulses with the same $`X`$ can have different full $`F`$ and $`J`$, and (L5) itself can be loose. The frontier concerns the specified $`K`$; optimizing over gate-equivalent diagonal completions or phase lifts is a further problem.

The spectral construction optimizes integrated force cost. Its damped pulses need not satisfy a separately specified instantaneous force cap at the same numerical value $`G/T`$. A converse may use $`G\leq PT`$ when such a cap is given, but attainment under that cap requires its own pulse analysis.

## 6. Attribution and remaining boundaries

The following distinctions are essential when using these formulas in an architectural claim.

- **Established dissipative physics.** [Louis et al.](https://arxiv.org/pdf/0804.3240) derive effective qubit operations from lossy bus overlaps in a sequential transfer model; their paired sequences remove correlated terms. [Müller, Luoma and Strunz](https://arxiv.org/html/1907.08033v2) treat Markovian damped geometric gates, including extra phases, loss of coherence, and adapted closure. Neither generic loss-induced dephasing nor compensation of endpoint closure is claimed as new.
- **Inherited mathematical method.** The spectral allocation and rank-tail strategy is closely related to the exact bilinear control optimization of [Wong and Baillieul](https://arxiv.org/pdf/1201.6527v2) and the geometric area formulas of [Rizzi and Serres](https://arxiv.org/html/1610.01596v2). The signed multiplicity and damped cost are derived explicitly here, with no priority claim for the underlying method.
- **Exact statements for this model.** The common normalization yields the paid squared-force action (L20), the attaining exposure frontier (L22), and the target-independent loss lower bound (L5). These connect finite bus resources to quantum-gate requirements.
- **Additional physics.** The formulas assume vacuum input, a common Markovian loss rate, a harmonic bus, exact conditional closure, independent complex coupling controls, and a fixed commuting data axis. Non-vacuum preparation, monitored loss, nonlinear or encoded buses, free squeezing, interspersed noncommuting data control, and approximate residual bus return require separate analysis.
- **Gate error and fault tolerance.** Neither $`X`$ nor the global diamond lower bound is a local fault-tolerance noise model. No threshold, unavoidable correlated-error statement, or exact noisy-gate optimum follows from these scalar resources alone.
