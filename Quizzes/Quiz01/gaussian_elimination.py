import numpy as np


def gaussianElimination(mat):
    N = len(mat)

    singular_flag = forward_substitution(mat)

    if singular_flag != -1:
        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

    # Fixing the pivots
    mat = fixPivots(mat)

    # if matrix is non-singular: get solution to system using backward substitution
    return backward_substitution(mat)


# function for elementary operation of swapping two rows
def swap_row(mat, i, j):
    N = len(mat)
    for k in range(N + 1):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp


def forward_substitution(mat):
    N = len(mat)
    for k in range(N):

        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = mat[i][k]
                pivot_row = i

        # if a principal diagonal element is zero or too close to zero, find another pivot row
        if abs(mat[k][k]) < 1e-10:
            pivot_found = False
            for i in range(k + 1, N):
                if abs(mat[i][k]) > 1e-10:
                    pivot_found = True
                    swap_row(mat, k, i)
                    break
            if not pivot_found:
                return k  # Matrix is singular

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if all(mat[i][k] == 0 for i in range(k, N)) or abs(
                mat[k][k]) < 1e-10:
            return k

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_row(mat, k, pivot_row)

        for i in range(k + 1, N):

            #  Compute the multiplier
            m = mat[i][k] / mat[k][k]

            # subtract fth multiple of corresponding kth row element
            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j] * m

            # filling lower triangular matrix with zeros
            mat[i][k] = 0

    return -1


def fixPivots(mat):
    N = len(mat)
    for k in range(N):
        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = mat[i][k]
                pivot_row = i

        # If the pivot is not 1, perform row operations to make it 1
        if mat[k][k] != 1:
            # Divide the current row by the pivot to make it 1
            pivot = mat[k][k]
            for j in range(k, N + 1):
                mat[k][j] /= pivot

        # Swap the current row with the pivot row if necessary
        if pivot_row != k:
            swap_row(mat, k, pivot_row)

    return mat


def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)

    # Start calculating from last equation up to the first
    for i in range(N - 1, -1, -1):

        x[i] = mat[i][N]

        # Initialize j to i+1 since matrix is upper triangular
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]

        x[i] = (x[i] / mat[i][i])

    return x


if __name__ == '__main__':

    A_b = [[1, 2, 3, 4, 5],
           [2, 3, 4, 5, 1],
           [8, 8, 8, 8, 1],
           [24, 15, 22, 1, 8]]

    print(gaussianElimination(A_b))

