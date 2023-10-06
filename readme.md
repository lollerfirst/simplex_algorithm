# Simplex Method

The simplex method is an algorithm for maximizing an objective function. It operates on linear programs:

```math
max \ \ \mathbf{c}^T\mathbf{x} \\ 
\text{s.t.} \ \ A\mathbf{x} \leq b \text{    and } \mathbf{x} \geq 0
```

Where $\mathbf{x}$ is the vector of variables of the problem, $A$ is a $p\times n$ matrix and $\mathbf{b}$ is the vector of source terms.

In geometric terms, the feasible region defined by all values of $\mathbf{x}$ such that $A x ≤ b$ and $ ∀ i , x i ≥ 0 $ is a (possibly unbounded) convex polytope. An extreme point or vertex of this polytope is known as basic feasible solution (BFS).

A linear program in standard form can be represented as a tableau of the form

```math
\begin{bmatrix}1&-\mathbf {c} ^{T}&0\\0&\mathbf {A} &\mathbf {b} \end{bmatrix}
```