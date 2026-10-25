# Exact spectral cost of closed linear-bus gates

This page proves the minimum trajectory energy for a specified real symmetric geometric-phase matrix, and the sharp consequence when only a cross block is fixed. The gate-level minimization over physically equivalent phase matrices is treated in [matching.md](matching.md).

The weighted spectral minimization method is inherited from bilinear optimal control and matrix-area geometry. In particular, Wong and Baillieul give an exact weighted singular-value control cost in their Theorem 5.1 and its Brockett–Heisenberg specialization in Corollary 5.1 [1]. Closed-loop frequency allocation also appears in Brockett's Theorem 2 [2] and the vertical-distance formula of Rizzi and Serres, Appendix A, Proposition 15 [3]. The proofs below establish the symmetric phase-matrix specialization, its real multiplicity for $`b`$ complex buses, and the normalization needed for quantum gates. The inherited spectral method is not presented as a new general principle.

## 1. Model, regularity, and normalization

There are $`n`$ commuting spin observables $`Z_i`$, with eigenvalues $`z_i\in\{-1,1\}`$, and $`b\geq1`$ independent complex harmonic-bus coordinates. Put the conditional displacement coefficients into a matrix

```math
A(t)=[\alpha_1(t)\ \cdots\ \alpha_n(t)]
\in\mathbb{C}^{b\times n}.
```

Every entry belongs to $`H_0^1(0,T)`$: it has a square-integrable weak derivative and its continuous representative obeys

**(SC.1)**

```math
A(0)=A(T)=0.
```

Thus every computational branch $`A(t)z`$ returns exactly to the same bus state. No finite bus Fock-space cutoff or peak branch occupation bound is imposed.

Define the entrywise real and imaginary parts

**(SC.2)**

```math
\begin{aligned}
F&=\mathrm{Re}\int_0^T A^\dagger A\,dt,\\
K&=\mathrm{Im}\int_0^T A^\dagger\dot A\,dt,\\
E_{\rm mat}&=\mathrm{Re}\int_0^T\dot A^\dagger\dot A\,dt,
\qquad
X=\mathrm{tr}F,\quad E=\mathrm{tr}E_{\rm mat}.
\end{aligned}
```

Integration by parts gives
$`\int A^\dagger\dot A=-(\int A^\dagger\dot A)^\dagger`$, so $`K`$ is real symmetric. The ideal spin gate is

**(SC.3)**

```math
U_K\vert z\rangle=e^{iz^{\mathsf{T}}Kz}\vert z\rangle.
```

Consequently the coefficient of $`Z_iZ_j`$, for $`i\lt j`$, is $`2K_{ij}`$. The diagonal of $`K`$ contributes only the global phase $`\mathrm{tr}K`$. Fixing all of $`K`$ is therefore a stronger requirement than fixing the physical spin gate.

At zero loss the coefficient-force matrix is $`u=\dot A`$, and $`E=\int\Vert u\Vert _F^2dt`$. With dimensionless displacement, $`K`$ is dimensionless, $`X`$ has time units, and $`E`$ has inverse-time units. This is an independent coupling-coefficient budget. It is not $`\max_z\Vert u(t)z\Vert ^2`$, a maximum bus occupation, or a bound on the energy in an arbitrary computational branch.

## 2. Fixed-matrix optimum

Write the positive eigenvalues of $`K`$ in descending order as
$`\lambda_1^+\geq\lambda_2^+\geq\cdots\gt 0`$. Write the magnitudes of its negative eigenvalues, independently in descending order, as
$`\lambda_1^-\geq\lambda_2^-\geq\cdots\gt 0`$. Empty lists contribute zero. Define

**(SC.4)**

```math
\Phi_b(K)=
\sum_{j\geq1}\left\lceil\frac{j}{2b}\right\rceil\lambda_j^+
+
\sum_{j\geq1}\left\lceil\frac{j}{2b}\right\rceil\lambda_j^-.
```

**Theorem SC1.** For every real symmetric $`K`$, every $`T\gt 0`$, and every integer $`b\geq1`$,

**(SC.5)**

```math
\boxed{
\min_{\substack{A\in H_0^1(0,T;\mathbb{C}^{b\times n})\\
\mathrm{Im}\int A^\dagger\dot A=K}}
\int_0^T\Vert \dot A\Vert _F^2dt
=\frac{2\pi}{T}\Phi_b(K).
}
```

The minimum is attained by a finite sum of closed circular Fourier trajectories. A signed temporal harmonic supports at most $`2b`$ real phase directions, because each complex bus supplies two real quadratures.

### 2.1. Fourier representation, including the endpoint issue

Since the endpoint traces agree, $`A`$ has a periodic $`H^1`$ extension. Let its Fourier coefficients be $`V_k`$, with frequencies $`\omega_k=2\pi k/T`$. Then

```math
\sum_{k\in\mathbb{Z}}(1+k^2)\Vert V_k\Vert _F^2\lt \infty.
```

For the nonconstant coefficients, Cauchy–Schwarz gives

```math
\sum_{k\ne0}\Vert V_k\Vert _F
\leq
\left(\sum_{k\ne0}k^2\Vert V_k\Vert _F^2\right)^{1/2}
\left(\sum_{k\ne0}k^{-2}\right)^{1/2}\lt \infty.
```

The Fourier series therefore converges uniformly as well as in $`H^1`$. Its value at $`t=0`$ fixes
$`V_0=-\sum_{k\ne0}V_k`$, and hence

**(SC.6)**

```math
A(t)=\sum_{k\ne0}V_k(e^{i\omega_kt}-1).
```

The series for $`\dot A`$ converges in $`L^2`$. Products in the area integral converge in $`L^1`$ by Cauchy–Schwarz, so computing that integral from finite partial sums is legitimate. Parseval and Fourier orthogonality give

**(SC.7)**

```math
\begin{aligned}
K&=2\pi\sum_{k\ne0}k\,\mathrm{Re}(V_k^\dagger V_k),\\
E&=\frac{4\pi^2}{T}\sum_{k\ne0}k^2\Vert V_k\Vert _F^2.
\end{aligned}
```

The constant in (SC.6) does not contribute to $`K`$: its product with each derivative has zero time integral. The matrix series for $`K`$ is absolutely convergent in trace norm, since
$`\sum \vert k\vert \Vert V_k\Vert _F^2\lt \infty`$.

For $`k\geq1`$, set

```math
X_k=2\pi k\,\mathrm{Re}(V_k^\dagger V_k),
\qquad
Y_k=2\pi k\,\mathrm{Re}(V_{-k}^\dagger V_{-k}).
```

These are real positive semidefinite matrices of rank at most $`2b`$, and

**(SC.8)**

```math
K=\sum_{k\geq1}(X_k-Y_k),
\qquad
E=\frac{2\pi}{T}\sum_{k\geq1}k\,\mathrm{tr}(X_k+Y_k).
```

The rank statement follows by writing a complex matrix as its real and imaginary parts:
$`\mathrm{Re}(V^\dagger V)=(\mathrm{Re}V)^{\mathsf{T}}\mathrm{Re}V+ (\mathrm{Im}V)^{\mathsf{T}}\mathrm{Im}V`$.

### 2.2. The rank-tail lower bound

We use the following elementary fact. If $`P_k\succeq0`$ have rank at most $`r`$, their sum $`P`$ has finite trace, and $`\mu_j(P)`$ are its descending eigenvalues, then

**(SC.9)**

```math
\sum_{k\geq1}k\,\mathrm{tr}P_k
\geq
\sum_j\left\lceil\frac{j}{r}\right\rceil\mu_j(P).
```

To prove it, fix $`s\geq1`$. The sum $`L_s=\sum_{k\lt s}P_k`$ has rank at most $`r(s-1)`$ and satisfies $`0\preceq L_s\preceq P`$. The variational principle for the sum of the largest eigenvalues implies

```math
\mathrm{tr}(P-L_s)
\geq\sum_{j\gt r(s-1)}\mu_j(P).
```

For completeness, take the orthogonal projection $`Q_s`$ onto the range of $`L_s`$. Then
$`\mathrm{tr}L_s=\mathrm{tr}(Q_sL_s)\leq \mathrm{tr}(Q_sP)\leq\sum_{j\leq r(s-1)}\mu_j(P)`$.
Summing over $`s`$, with nonnegative terms, proves (SC.9) by Tonelli's theorem.

Apply (SC.9) to $`P_+=\sum X_k`$. Since $`P_+-K=\sum Y_k\succeq0`$, eigenvalue monotonicity gives
$`\mu_j(P_+)\geq\lambda_j^+(K)`$ for every index in the positive list. Apply the same argument to $`P_-=\sum Y_k\succeq-K`$ and its negative list. Equation (SC.8) proves the lower bound in (SC.5). This argument remains valid for infinite Fourier series; all required sums are nonnegative and finite when $`E\lt \infty`$.

### 2.3. Attainment and quadrature packing

Let $`q_j^+`$ and $`q_j^-`$ be real orthonormal eigenvectors for the two sign lists. Put the first $`2b`$ positive eigenvectors into harmonic $`+1`$, the next $`2b`$ into harmonic $`+2`$, and continue. Treat the negative list independently at harmonics $`-1,-2,\ldots`$. Thus the desired positive contribution at harmonic $`k`$ is

```math
X_k=\sum_{2b(k-1)\lt j\leq2bk}
\lambda_j^+q_j^+(q_j^+)^{\mathsf{T}},
```

with the analogous definition for $`Y_k`$.

Every real positive semidefinite matrix $`G`$ of rank at most $`2b`$ is
$`\mathrm{Re}(V^\dagger V)`$ for a $`b`$-by-$`n`$ complex matrix $`V`$. Indeed, factor $`G=R^{\mathsf{T}}R`$ with at most $`2b`$ real rows, pad with zero rows, and take the first $`b`$ rows of $`R`$ as $`\mathrm{Re}V`$, the remaining $`b`$ as $`\mathrm{Im}V`$.

Use this factorization for $`X_k/(2\pi k)`$ and $`Y_k/(2\pi k)`$ to choose $`V_k,V_{-k}`$. The finite series (SC.6) then realizes $`K`$ exactly and pays exactly the right-hand side of (SC.5).

## 3. Sharp cross-block cost

Let $`\mathcal{A},\mathcal{B}`$ be disjoint sets of spin coordinates, and put
$`C=K_{\mathcal{A}\mathcal{B}}`$. Its nonzero singular values are
$`\sigma_1(C)\geq\cdots\geq\sigma_m(C)\gt 0`$. Zero singular values may be appended without changing the statements.

**Theorem SC2.** Every real symmetric completion $`K`$ of $`C`$ obeys

**(SC.10)**

```math
\boxed{
\Phi_b(K)\geq
2\sum_{j=1}^m\left\lceil\frac{j}{4b}\right\rceil\sigma_j(C).
}
```

Consequently every closed trajectory obeys

**(SC.11)**

```math
E\geq\frac{4\pi}{T}\sum_{j=1}^m
\left\lceil\frac{j}{4b}\right\rceil\sigma_j(C)
\geq
\frac{\pi}{bT}\sum_{j=1}^m j\,\sigma_j(C),
```

and also $`E\geq(4\pi/T)\Vert C\Vert _*`$.
If the two diagonal blocks of $`K`$ may be chosen freely, equality in the first bound (SC.10) and in the first bound (SC.11) is attainable.

### 3.1. Proof of the lower bound

For any real symmetric block matrix $`R`$,

**(SC.12)**

```math
\Vert R\Vert _*\geq2\Vert R_{\mathcal{A}\mathcal{B}}\Vert _*.
```

If $`P`$ is the polar partial isometry of $`R_{\mathcal{A}\mathcal{B}}`$, the symmetric matrix with off-diagonal blocks $`P,P^{\mathsf{T}}`$, all other blocks zero, has operator norm at most one and pairs with $`R`$ to give $`2\Vert R_{\mathcal{A}\mathcal{B}}\Vert _*`$. The dual characterization of the nuclear norm proves (SC.12).

For $`s\geq1`$, let $`K^{\lt s}`$ retain the first $`2b(s-1)`$ positive eigenvectors of $`K`$ and the first $`2b(s-1)`$ negative eigenvectors. Its rank is at most $`4b(s-1)`$. Therefore its cross block is a rank-at-most-$`4b(s-1)`$ approximation to $`C`$. The nuclear-norm best-rank approximation principle and (SC.12) yield

```math
\begin{aligned}
\sum_{j\gt 2b(s-1)}(\lambda_j^++\lambda_j^-)
&=\Vert K-K^{\lt s}\Vert _*\\
&\geq2\Vert C-(K^{\lt s})_{\mathcal{A}\mathcal{B}}\Vert _*\\
&\geq2\sum_{j\gt 4b(s-1)}\sigma_j(C).
\end{aligned}
```

Summation over $`s`$ gives (SC.10). The different denominators $`2b`$ and $`4b`$ are essential: $`K`$ has separate positive and negative harmonic capacity.

### 3.2. Sharp completion

Write a real singular-value decomposition
$`C=\sum_j\sigma_j u_jv_j^{\mathsf{T}}`$. In each consecutive block of $`4b`$ singular directions, assign the first $`2b`$ the sign $`s_j=+1`$, and the remaining $`2b`$ the sign $`s_j=-1`$. Define

**(SC.13)**

```math
q_j=\frac{1}{\sqrt2}(u_j\oplus s_jv_j),
\qquad
K_*=\sum_j2s_j\sigma_jq_jq_j^{\mathsf{T}}.
```

The cross block of $`K_*`$ is $`C`$. Its nonzero eigenvalues are $`2s_j\sigma_j`$; within each sign, the corresponding singular directions remain in descending order. The $`j`$-th singular direction therefore receives weight $`\lceil j/(4b)\rceil`$, and

```math
\Phi_b(K_*)=2\sum_j\left\lceil\frac{j}{4b}\right\rceil\sigma_j(C).
```

Theorem SC1 supplies an attaining trajectory.

For a general $`C`$, the chosen diagonal blocks can contain same-side two-spin interactions. Thus this completion theorem alone is not an upper bound for an arbitrary prescribed spin gate. For $`C=cI_m`$, the singular vectors are coordinate vectors and both diagonal blocks in (SC.13) are ordinary diagonal matrices. Their only spin effect is a global phase, which is why the completion is directly usable for a matching of pair gates.

## 4. Phase–exposure–energy inequalities

The trajectories and their rotated derivatives form a real Gram matrix:

**(SC.14)**

```math
\begin{pmatrix}F&K\\K&E_{\rm mat}\end{pmatrix}\succeq0.
```

Hence $`\ker F\subseteq\ker K`$ and
$`E_{\rm mat}\succeq KF^+K`$, with the Moore–Penrose inverse. A useful scalar consequence is

**(SC.15)**

```math
EX\geq\Vert K\Vert _*^2.
```

It also follows directly by Cauchy–Schwarz: if $`S`$ is a real symmetric orthogonal sign matrix of $`K`$, completed arbitrarily on the kernel, then
$`\mathrm{tr}(SK)=\Vert K\Vert _*`$, while multiplication of $`A`$ by $`S`$ preserves its Frobenius norm.

Closure yields the stronger finite-time scalar inequality

**(SC.16)**

```math
\boxed{
E\geq\frac{\Vert K\Vert _*^2}{X}+\frac{\pi^2}{T^2}X
}
\qquad (X\gt 0).
```

To prove it, apply Dirichlet Poincaré to
$`B(t)=A(t)e^{-i\omega St}`$. Direct differentiation gives

```math
\int_0^T\Vert \dot B\Vert _F^2dt
=E-2\omega\Vert K\Vert _*+\omega^2X
\geq\frac{\pi^2}{T^2}X.
```

Optimizing the real parameter $`\omega`$ proves (SC.16).
If each of the positive and negative ranks of $`K`$ is at most $`2b`$, equality can be attained: in a real eigenbasis of $`K`$, use columns
$`c_j\sin(\pi t/T)e^{i\,\mathrm{sign}(\lambda_j)\omega t}`$, with the $`c_j`$ real-orthogonal within each sign and scaled to their required areas. The area cross terms between opposite signs vanish by a boundary derivative. More ranks require higher temporal modes, as quantified by Theorem SC1.

### A tempting matrix strengthening is false

One must not replace (SC.16) by
$`E_{\rm mat}\succeq KF^+K+(\pi/T)^2F`$.
For one bus and two columns, take

```math
\alpha_1(t)=\sin(\pi t/T)e^{i\pi t/T},
\qquad
\alpha_2(t)=\sin(\pi t/T)e^{-i\pi t/T}.
```

Direct integration gives

```math
F=\frac T4\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\quad
K=\frac\pi2\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\quad
E_{\rm mat}=\frac{\pi^2}{T}I_2.
```

The proposed matrix residual is

```math
E_{\rm mat}-KF^{-1}K-\frac{\pi^2}{T^2}F
=\frac{\pi^2}{T}
\begin{pmatrix}-1/6&7/12\\7/12&-1/6\end{pmatrix},
```

whose eigenvalues are $`(\pi^2/T)\{5/12,-3/4\}`$. The scalar inequality (SC.16) is nevertheless saturated. Its proof must therefore remain independent of that false matrix claim.

## 5. Physical scope of the optimum

The constructive optimum assumes arbitrary complex coefficient forces on each participating spin–bus coupling. Restricted addressing or fixed hardware force patterns can only increase the required cost. The model covers pulse shaping and concatenation of closed loops while all coupled spin observables commute. It does not cover interspersed noncommuting spin rotations, measurement and feedback, extra spin ancillas, active squeezing, uncharged bus mixing, or nonlinear mediator dynamics.

The bus is an ideal harmonic oscillator with no finite occupation cutoff. Peak branch force, peak branch displacement, finite slew, and a hard bandwidth constraint are additional resources. Circular controls have a well-defined modulation frequency within the gate interval, but switching a nonzero endpoint force on and off creates frequency tails. The constructions here are not claims of strict bandwidth limitation.

For Markovian damping at rate $`\kappa`$, when $`A`$ denotes the actual closed damped trajectory and $`u=\dot A+\kappa A/2`$, the paid drive energy is
$`G=E+\kappa^2X/4\geq E`$. Thus every lower bound on $`E`$ remains a lower bound on $`G`$. The exact damping-weighted optimum and exposure frontier require the corresponding generalized spectral problem; the zero-loss construction is not automatically a construction of an accurate noisy gate.

## References

1. W. S. Wong and J. Baillieul, *Control Communication Complexity of Distributed Actions*, especially Theorem 5.1 and Corollary 5.1, [arXiv:1201.6527v2](https://arxiv.org/abs/1201.6527v2), [full text](https://arxiv.org/pdf/1201.6527).
2. R. W. Brockett, *Control Theory and Singular Riemannian Geometry*, in *New Directions in Applied Mathematics*, Springer (1982), pp. 11–27, especially Theorem 2, [publisher record](https://doi.org/10.1007/978-1-4612-5651-9_2), [author-hosted primary text](https://hrl.harvard.edu/publications/brockett81control.pdf).
3. L. Rizzi and U. Serres, *On the cut locus of free, step two Carnot groups*, *Proceedings of the American Mathematical Society* **145**, 5341–5357 (2017), Appendix A, Proposition 15, [arXiv:1610.01596v2](https://arxiv.org/html/1610.01596v2). Their discussion explicitly records a normalization difference from Brockett's formula. The [author's publication list](https://sites.google.com/view/rizziluca/research) also links an erratum whose contents have not been reviewed here; no assertion is made about its scope. This reference is used as mathematical lineage. The proofs and constants on this page are independent and import no normalization from that source.
