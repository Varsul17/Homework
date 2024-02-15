from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix
import numpy as np
#I am not Liron!
"""
Function that find the inverse of non-singular matrix
The function performs elementary row operations to transform it into the identity matrix.
The resulting identity matrix will be the inverse of the input matrix if it is non-singular.
 If the input matrix is singular (i.e., its diagonal elements become zero during row operations), it raises an error.
"""

def inverse(matrix):
    print(f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        # Perform row exchanges if the pivot element is zero
        if matrix[i, i] == 0:
            # Find a row below with a non-zero element in the same column
            for k in range(i + 1, n):
                if matrix[k, i] != 0:
                    # Exchange rows i and k in both the input matrix and the identity matrix
                    matrix[[i, k]] = matrix[[k, i]]
                    identity[[i, k]] = identity[[k, i]]
                    break
            else:
                raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
            matrix = np.dot(elementary_matrix, matrix)
            print(f"The matrix after elementary operation :\n {matrix}")
            print("------------------------------------------------------------------------------------------------------------------")
            identity = np.dot(elementary_matrix, identity)

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i != j and i < j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print("------------------------------------------------------------------------------------------------------------------")
                identity = np.dot(elementary_matrix, identity)

    for i in range(n)[::-1]:
        for j in range(n)[::-1]:
            if i > j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j + 1} = R{j + 1} + ({scalar}R{i + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(
                    "------------------------------------------------------------------------------------------------------------------")
                identity = np.dot(elementary_matrix, identity)

    return identity


if __name__ == '__main__':

    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    try:
        A_inverse = inverse(A)
        print("\nInverse of matrix A: \n", A_inverse)
        print("=====================================================================================================================")

    except ValueError as e:
        print(str(e))
