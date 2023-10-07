# Simplex Method

The simplex method is an algorithm for maximizing an objective function. It operates on linear programs:

```math
max \ \ \mathbf{c}^T\mathbf{x} \ \ \text{s.t.} \ \ A\mathbf{x} \leq b \text{    and } \mathbf{x} \geq 0
```

Where $\mathbf{x}$ is the vector of variables of the problem, $A$ is a $p\times n$ matrix and $\mathbf{b}$ is the vector of source terms.

In geometric terms, the feasible region defined by all values of $\mathbf{x}$ such that $A x ≤ b$ and $ ∀ i , x i ≥ 0 $ is a (possibly unbounded) convex polytope. An extreme point or vertex of this polytope is known as basic feasible solution (BFS).

A linear program in standard form can be represented as a tableau of the form

```math
\begin{bmatrix}1&-\mathbf {c} ^{T}&0\\0&\mathbf {A} &\mathbf {b} \end{bmatrix}
```

By adding slack variables coefficients $\mathbf{c_B^T}$ the new tableu will look like:

```math
\begin{bmatrix}
    1 &-\mathbf{c_B^T} &-\mathbf{c_A^T} &0 \\
    \mathbf{0} &I &A &\mathbf{b}
\end{bmatrix}
```

Where $I$ is the Identity matrix. The coefficients $c_B^T$ will initially be 0, so the initial tableu will look like:

```math
\begin{bmatrix}
    1 &\mathbf{0^T} &-\bar{\mathbf{c}}_A^T &z_B \\
    \mathbf{0} &I &A &\mathbf{b}
\end{bmatrix}
```
Where $\bar{\mathbf{c}}_A^T$ are the relative cost coefficients for the non-basic variables (How much the solution changes for each unit change of non-basic variable) and $z_B$ is the value of the Objective function evalued at the current basic feasible solution.

## Pivot Operations