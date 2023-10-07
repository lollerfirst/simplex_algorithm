# Simplex Method
## The Tableau
The simplex method is an algorithm for maximizing an objective function. It operates on linear programs:

```math
max \ \ \mathbf{c}^T\mathbf{x} \ \ \text{s.t.} \ \ A\mathbf{x} \leq b \text{    and } \mathbf{x} \geq 0
```

Where $\mathbf{x}$ is the vector of variables of the problem, $A$ is a $m\times n$ matrix and $\mathbf{b}$ is the vector of source terms.

In geometric terms, the feasible region defined by all values of $\mathbf{x}$ such that $A x ≤ b$ and $\forall{i,x}: i \geq 0$ is a (possibly unbounded) convex polytope. An extreme point or vertex of this polytope is known as basic feasible solution (BFS).

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
\text{tableau} = \begin{bmatrix}
     1 &\mathbf{0^T} &-\bar{\mathbf{c}}_A^T &z_B \\
    \mathbf{0} &I &A &\mathbf{b}
\end{bmatrix}
```
Where $\bar{\mathbf{c}}_A^T$ are the relative cost coefficients for the non-basic variables (How much the solution changes for each unit change of non-basic variable) and $z_B$ is the value of the Objective function evalued at the current basic feasible solution, which will also be equal to 0 in the beginning.

## Pivot Operations

The geometrical operation of moving from a basic feasible solution to an adjacent basic feasible solution is implemented as a pivot operation. First, a nonzero pivot element is selected in a nonbasic column. The row containing this element is multiplied by its reciprocal to change this element to 1, and then multiples of the row are added to the other rows to change the other entries in the column to 0. The result is that, if the pivot element is in a row r, then the column becomes the r-th column of the identity matrix. The variable for this column is now a basic variable, replacing the variable which corresponded to the r-th column of the identity matrix before the operation. In effect, the variable corresponding to the pivot column enters the set of basic variables and is called the entering variable, and the variable being replaced leaves the set of basic variables and is called the leaving variable. The tableau is still in canonical form but with the set of basic variables changed by one element.

## Entering variable selection

Since $-\mathbf{\bar{c}^T}$ represents the vector of relative cost coefficients for the variables $\mathbf{x}$, choosing the index of the largest entry ensures the variable entering the basis maximizes the objective function for the current iteration. So, the index $i$ is chosen as follows:

```math 
i = \mathop{\arg \max}\limits_{k \in \{1, 2, \ \ldots \ , n\}}(-\bar{c}[k])$
```
## Leaving Variable Selection
The pivot element is the chosen amongst the element of the $i$-th column. In particular, the pivot element $p$ is chosen as the entry with the lowest ratio to his corresponding entry in the $b$ column. This is called the minimum-ratio-test:

```math
j = \mathop{\arg \min}\limits_{k \in \{2, 3, \ \ldots \, m\}} \left( \frac{\text{tableau}[k,i]}{\text{tableau}[k,-1]} \right)
```
