#importsregion
import numpy as np
from scipy.linalg import solve, inv
#endregion

"""
The goal of this program is to solve two different sets of linear algebra equations
and checking them with various methods.
Step 1: define both matrices (A1 & A2) using numpy
Step 2: define both vectors (b1 & b2) using numpy
Step 3: solve both matrix problems using scipy
Step 4: verify solutions using 'np.matmul' and 'np.dot' to multiply the coefficient
matrices by the solution vectors
Step 5: perform an additional verification by calculating the inverse of the coefficient 
matrices and multiplying them by the constant vectors
Step 6: print solutions of the problems and true / false statements of 
"""

#setup the coefficient matrices and the constant vectors for both problems using numpy
A1 = np.array([[3, 1, -1],
               [1, 4, 1],
               [2, 1, 2]])
b1 = np.array([2, 12, 10])

A2 = np.array([[1, -10, 2, 4],
               [3, 1, 4, 12],
               [9, 2, 3, 4],
               [-1, 2, 7, 3]])
b2 = np.array([2, 12, 21, 37])

#compute solutions for both problems using scipy
sol1 = solve(A1, b1)
sol2 = solve(A2, b2)

#check solutions using np.matmul
check1_matmul = np.matmul(A1, sol1)
check2_matmul = np.matmul(A2, sol2)

#check solutions using np.dot
check1_dot = np.dot(A1, sol1)
check2_dot = np.dot(A2, sol2)

#compute and check solutions using the inverse of A1 and A2 (scipy)
inv_A1 = inv(A1)
inv_A2 = inv(A2)
check1_inv = np.dot(inv_A1, b1)
check2_inv = np.dot(inv_A2, b2)

#print solutions & checks
#chatgpt was used for printing statements
print("Solutions for Problem 1:")
for i, value in enumerate(sol1, start=1):
    print(f"x{i} = {value:.3f}")
print("Verification using np.matmul:", np.allclose(check1_matmul, b1))
print("Verification using np.dot:", np.allclose(check1_dot, b1))
print("Verification using inverse:", np.allclose(check1_inv, sol1))

print("\nSolutions for Problem 2:")
for i, value in enumerate(sol2, start=1):
    print(f"x{i} = {value:.3f}")
print("Verification using np.matmul:", np.allclose(check2_matmul, b2))
print("Verification using np.dot:", np.allclose(check2_dot, b2))
print("Verification using inverse:", np.allclose(check2_inv, sol2))

