import numpy as np
from numpy.linalg import inv, norm

def condition_number(A):

  # Step 1: Calculate the max norm (infinity norm) of A
  norm_A = norm(A, ord=np.inf)

  # Step 2: Calculate the inverse of A
  A_inv = inv(A)

  # Step 3: Calculate the max norm of the inverse of A
  norm_A_inv = norm(A_inv, ord=np.inf)

  # Step 4: Compute the condition number
  cond = norm_A * norm_A_inv

  return cond, A_inv

# Example usage
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

cond, A_inv = condition_number(A)

print("Matrix A:")
print(A)
print()
print("Inverse of A:")
print(A_inv)
print(cond)
