import numpy as np

def simplex_maximize(c, A, b):

    # Convert input to NumPy arrays
    c = np.array(c)
    A = np.array(A)
    b = np.array(b)

    # Check if the problem is feasible
    if np.any(b < 0):
        raise Exception("The problem has infeasible constraints")

    # Add slack variables to convert inequalities to equalities
    m, n = A.shape
    A_slack = np.hstack((A, np.eye(m)))
    z = np.zeros(m)
    A_slack = np.hstack((np.atleast_2d(z).T, A_slack))

    c = np.concatenate((c, np.zeros(m)))
    c = np.concatenate((np.array([-1]), c))

    # Initialize the tableau
    tableau = np.vstack((np.hstack((-c, np.zeros(1))),
                         np.hstack((A_slack, np.atleast_2d(b).T))))
    
    #tableau = tableau.T

    iteration = 1

    while True:
        print(f"Iteration {iteration}:\n", tableau)

        # Find the entering variable (most negative coefficient in the objective function)
        entering_col = np.argmin(tableau[0, :-1])

        # Check for optimality
        if tableau[0, entering_col] >= 0:
            break

        # Find the leaving variable (minimum ratio test)
        ratios = tableau[1:, -1] / tableau[1:, entering_col]
        min_ratio_idx = np.argmin(ratios)
        leaving_row = min_ratio_idx + 1

        # Pivot to make the entering variable basic
        pivot_element = tableau[leaving_row, entering_col]
        tableau[leaving_row, :] /= pivot_element
        for i in range(m + 1):
            if i != leaving_row:
                pivot_row_multiplier = -tableau[i, entering_col]
                tableau[i, :] += pivot_row_multiplier * tableau[leaving_row, :]

        iteration += 1

    # Extract the solution and objective function value
    max_value = tableau[0,-1]

    return x, max_value

# Example usage:
c = [2, 3, 4]  # Coefficients of the objective function to maximize: -2x1 - 3x2
A = [[3, 2, 1],  # Coefficients of the constraints: x1 + x2 <= 4, 2x1 + x2 <= 7
     [2, 5, 3]]
b = [10, 15]    # Right-hand side of the constraints

x, max_value = simplex_maximize(c, A, b)
print("Optimal solution:", x)
print("Maximum value of the objective function:", max_value)
