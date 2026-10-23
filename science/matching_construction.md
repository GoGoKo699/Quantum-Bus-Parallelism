# An explicit matching gate layer

This construction implements the target layer exactly in the [commuting-force model](model.md), with every oscillator path closed. It uses the freedom to change the diagonal of the phase matrix: those entries affect only global phase. The resulting action and peak-force duration match the order of the [gate-layer lower bounds](gate_layer_bounds.md).

## 1. Four real slots per mode and harmonic

Let $`c=\pi/8`$, and label the pairs by $`r=1,\ldots,K`$. Give pair $`r`$ the positive harmonic number

```math
n_r=\left\lceil\frac r{4m}\right\rceil.
\tag{1}
```

At each harmonic number, there are $`4m`$ slots: a frequency sign $`s\in\{+1,-1\}`$, a mode $`\ell\in\{1,\ldots,m\}`$, and a quadrature $`p\in\{0,1\}`$. Assign distinct pairs to distinct slots before moving to the next harmonic. For definiteness, order frequency sign $`+`$ before $`-`$, then mode, then quadrature. Put

```math
a_n=\frac{\sqrt{2\pi c n}}T=\frac{\pi\sqrt n}{2T}.
\tag{2}
```

For the pair $`(A_r,B_r)`$ assigned to $`(n,s,\ell,p)`$, use

```math
u_{A_r,\ell}(t)=i^p a_n e^{is2\pi nt/T},\qquad
u_{B_r,\ell}(t)=s\,i^p a_n e^{is2\pi nt/T}.
\tag{3}
```

All other mode drives on those two qubits vanish. Thus each qubit has exactly one tone of constant magnitude. Every tone has a nonzero integer frequency over $`[0,T]`$, so every conditional path closes exactly.

For a Fourier coefficient vector $`v_{\ell,n}\in\mathbb C^{2K}`$, the phase contribution is

```math
A=\frac{T^2}{2\pi}\sum_{\ell,n\ne0}
\frac{\operatorname{Re}(v_{\ell,n}v_{\ell,n}^\dagger)}{n}.
\tag{4}
```

The [spectral cost proof](spectral_cost.md) derives this identity for the full $`L^2`$ control class. Here the Fourier sum is finite.

The two qubits of a positive-frequency pair receive the same force, while a negative-frequency pair receives opposite forces. Their blocks in $`A`$ are respectively

```math
c\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
-c\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\tag{5}
```

Both have the desired cross entry $`+c`$, hence the desired $`ZZ`$ angle $`2c=\pi/4`$. Each block has only one nonzero real eigenvalue, respectively $`+2c`$ or $`-2c`$.

Two pairs can share a mode and signed harmonic because their coefficients have relative phase $`i`$: the real part of their cross outer product is zero. Distinct modes add independently, and distinct signed harmonics are orthogonal in (4). Therefore every unwanted off-diagonal entry vanishes. The only departure from the target phase matrix is its diagonal, and

```math
U_A=e^{i\operatorname{tr}A}V_K.
\tag{6}
```

This explains all four slots per mode and harmonic: two real quadratures at each of two frequency signs.

## 2. Exact action and force-limited duration

Each pair contributes two coefficient magnitudes $`a_{n_r}`$. Parseval gives

```math
\boxed{\displaystyle
\mathcal ET=2T^2\sum_{r=1}^K a_{n_r}^2
=\frac{\pi^2}{2}\sum_{r=1}^K
\left\lceil\frac r{4m}\right\rceil.}
\tag{7}
```

This also equals the prescribed-matrix optimum for the particular $`A`$ in (5): its positive and negative eigenvalues occupy their respective lowest available spectral slots. Optimality over every physically equivalent phase matrix is not asserted.

For a finite-size expression, write $`K=4mJ+s`$ with integers $`J\ge0`$ and $`0\le s<4m`$. Then

```math
\sum_{r=1}^K\left\lceil\frac r{4m}\right\rceil
=4m\frac{J(J+1)}2+s(J+1)
\le K+\frac{K(K-1)}{8m}.
\tag{8}
```

The inequality follows by summing
$`\lceil r/(4m)\rceil\le1+(r-1)/(4m)`$.
Combining (7) with the lower bound proves the action law
$`\mathcal A_\epsilon(K,m)=\Theta_\epsilon(K+K^2/m)`$ for each fixed $`0\le\epsilon<1/\sqrt2`$.

Put $`L=\lceil K/(4m)\rceil`$. Since each qubit has only one tone, the largest per-qubit collective force norm is $`a_L`$. The constraint
$`\sum_\ell|u_{j\ell}(t)|^2\le g^2`$ is met by choosing

```math
\boxed{\displaystyle T=\frac\pi{2g}\sqrt L.}
\tag{9}
```

The layer is exact at that duration. Together with the converse it establishes
$`T_\epsilon(K,m,g)=\Theta_\epsilon(\sqrt{1+K/m}/g)`$ in the specified ideal control model. The separate lower and upper constants are not claimed to coincide.

## 3. Bandwidth of the construction

The highest angular frequency of the effective-force envelope in (3) is

```math
\Omega_{\max}=\frac{2\pi L}{T}.
\tag{10}
```

At the duration (9), this is $`4g\sqrt L`$. Thus the matching clock law uses increasingly rapid modulation when $`K/m`$ grows. An independent bandwidth restriction can increase the achievable duration. A lower bound proved while granting arbitrary bandwidth remains a lower bound for such a restricted system.

For this construction, an envelope-frequency ceiling $`\Omega`$ can be met by stretching the pulse to
$`T\ge2\pi L/\Omega`$. Imposing both this ceiling and the peak-force constraint therefore permits the sufficient duration

```math
T=\max\left\{\frac\pi{2g}\sqrt L,\frac{2\pi L}{\Omega}\right\}.
\tag{11}
```

Equation (11) is an upper construction under a specified Fourier-envelope restriction, not a general duration converse for every notion of physical actuator bandwidth. Carrier frequencies, rotating frames, and hardware transfer functions must be accounted for separately; see [hardware resources](hardware_resources.md).

## 4. Displacement and oscillator excursion

The primitive of the tone in (3) is

```math
\alpha_{A_r,\ell}(t)=i^p a_n
\frac{e^{is2\pi nt/T}-1}{is2\pi n/T},\qquad
\alpha_{B_r,\ell}(t)=s\,\alpha_{A_r,\ell}(t).
\tag{12}
```

For a participating qubit,

```math
|\alpha_{j\ell}(t)|
=\frac{|\sin(\pi nt/T)|}{2\sqrt n}
\le\frac1{2\sqrt n}.
\tag{13}
```

The trajectory size per qubit is independent of duration because the amplitude and duration are scaled together. For a computational-basis string $`z`$, the conditional bus displacement is
$`\beta_\ell(z,t)=\sum_jz_j\alpha_{j\ell}(t)`$.
Each pair contributes at most $`1/\sqrt n`$ to its magnitude. With at most four pairs per mode and harmonic,

```math
|\beta_\ell(z,t)|\le4\sum_{n=1}^L\frac1{\sqrt n}
\le8\sqrt L.
\tag{14}
```

For a bus initially in vacuum this is a sufficient worst-case occupation bound $`|\beta_\ell|^2\le64L`$ per mode. It is deliberately loose and is not a necessary occupation lower bound for the task.

Uniform averaging over computational-basis strings eliminates cross terms. When all four slots of a mode are occupied at every harmonic $`1,\ldots,L`$,

```math
\mathbb E_z|\beta_\ell(z,t)|^2
=\sum_j|\alpha_{j\ell}(t)|^2
=2\sum_{n=1}^L\frac{\sin^2(\pi nt/T)}n.
\tag{15}
```

The time average is the harmonic number $`H_L=\sum_{n=1}^L1/n`$, and the instantaneous average is at most $`2H_L`$. Partial filling only lowers these sums. The worst-case bound (14) and the ensemble average (15) describe different resources. The [hardware account](hardware_resources.md) discusses their relevance to oscillator nonlinearity, dissipation, and validity of the effective-force approximation.

## 5. Exact capacity with finitely many Fourier harmonics

Suppose the allowed controls have finite Fourier support

```math
u_{j\ell}(t)=\sum_{1\le|n|\le L}
v_{j\ell,n}e^{2\pi int/T}.
\tag{16}
```

For each signed harmonic and each mode, $`\operatorname{Re}(vv^\dagger)`$ has real rank at most two. Equation (4) therefore implies

```math
\operatorname{rank}A\le4mL.
\tag{17}
```

An exact target layer, including all local phase corrections and wraps, has an invertible cross block $`C=c(I+2M)`$ by the [parity argument](gate_layer_bounds.md#2-exact-gates-force-an-odd-determinant-cross-block). Since $`\operatorname{rank}C\le\operatorname{rank}A`$,

```math
\boxed{K\le4mL.}
\tag{18}
```

The construction in Section 1 attains every $`K\le4mL`$, so this is the exact capacity for the finite Fourier-support control class. Equation (16) is a specific restriction on harmonics of a pulse of duration $`T`$; it is not interchangeable with every continuous-frequency definition of bandwidth. The exactness assumption in (18) is essential, as the following proposition shows.

## 6. A boundary of the exact harmonic-capacity law

**Proposition.** Fix an integer $`K\ge2`$. For every positive layer-error tolerance there is a real symmetric matrix $`A`$ of rank two whose gate approximates the target within that tolerance, up to local $`Z`$ phases, and which can be synthesized with one bus mode using only the harmonics $`n=+1`$ and $`n=-1`$. A sequence of these approximations has divergent action. Thus an approximate version of (18) cannot hold without a further charged resource.

**Proof.** Let $`N`$ be the $`K\times K`$ upper shift, with $`N_{j,j+1}=1`$ and all other entries zero. For an integer $`t\ge1`$, put

```math
B_t=(I-2tN)^{-1}
=\sum_{j=0}^{K-1}(2t)^jN^j.
\tag{19}
```

The sum is finite because $`N^K=0`$. It is an integer matrix congruent to the identity modulo two, with determinant one. Hence

```math
D_t=cB_t=c(I+2M_t),\qquad M_t\in\mathbb Z^{K\times K}
\tag{20}
```

is an exactly allowed cross block for the target up to local phases.

The first $`K-1`$ singular values of $`-2tN`$ equal $`2t`$. Adding the identity changes each singular value by at most one, so

```math
s_j(I-2tN)\ge2t-1\quad(1\le j\le K-1).
```

Singular values of an inverse are the reciprocals in reverse order. It follows that

```math
s_2(B_t)=\frac1{s_{K-1}(I-2tN)}\le\frac1{2t-1}.
\tag{21}
```

Let $`C_t`$ be a real best rank-one singular-value approximation to $`D_t`$. Its residual obeys

```math
\lVert C_t-D_t\rVert_{\rm op}
=c\,s_2(B_t)\le\frac c{2t-1}.
\tag{22}
```

With the full symmetric matrix

```math
A_t=\begin{pmatrix}0&C_t\\C_t^{\mathsf T}&0\end{pmatrix},
\tag{23}
```

the residual phase relative to the exactly allowed cross block $`D_t`$ is uniformly bounded by

```math
2|a^{\mathsf T}(C_t-D_t)b|
\le2K\lVert C_t-D_t\rVert_{\rm op}
\le\frac{2Kc}{2t-1}.
\tag{24}
```

For sufficiently large $`t`$ this is below $`\pi/2`$, and the spectral-arc formula bounds the half-diamond error by
$`\sin(2Kc/(2t-1))`$. It tends to zero for every fixed $`K`$. In particular, a requested tolerance $`0<\epsilon<1`$ is met whenever $`2Kc/(2t-1)\le\arcsin\epsilon`$.

The only nonzero eigenvalues of $`A_t`$ are $`+\sigma_t`$ and $`-\sigma_t`$, where $`\sigma_t=c\,s_1(B_t)`$. Choose corresponding real unit eigenvectors $`v_+`$ and $`v_-`$. On a single mode the force vector

```math
u(t')=\frac{\sqrt{2\pi\sigma_t}}T
\left(v_+e^{2\pi it'/T}+v_-e^{-2\pi it'/T}\right),
\qquad 0\le t'\le T,
\tag{25}
```

has exact closure and produces $`A_t`$ through (4). It uses only the first positive and negative harmonics and has action

```math
\mathcal ET=4\pi\sigma_t
=4\pi c\,s_1(B_t)
\ge4\pi c(2t)^{K-1}\longrightarrow\infty,
\tag{26}
```

where the lower bound uses the top-right matrix entry $`(B_t)_{1K}=(2t)^{K-1}`$. This action is also the prescribed-matrix optimum. At fixed duration the fluence diverges; enforcing a fixed peak-force bound instead requires stretching the pulse. Neither choice gives a low-cost implementation. For $`K=1`$ the first harmonics already realize the target exactly, so the approximation statement is trivial. $`\square`$

The proposition exposes a genuine boundary between exact capacity and fixed-error resource bounds. The action converse remains valid because it charges the large surviving singular values. The simpler two-pair shear example in [gate-layer bounds](gate_layer_bounds.md#8-why-approximate-rank-is-insufficient) gives a numerically well-conditioned illustration of the same issue.

## Verification

The [verification script](../verification/verify_bus.py) checks the phase matrix, cancellation of unwanted couplings, action, peak-force normalization, and closure for finite instances. Direct integration checks the Fourier phase sign independently. Further small Boolean-cube checks exercise the wrap and error conversions, and the shear examples verify that rank reduction can coexist with small gate error and large action. The universal claims above follow from their proofs; finite computations provide checks of formulas and implementation.
