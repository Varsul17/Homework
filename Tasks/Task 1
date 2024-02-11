#Gal Warsulker - 206493173
#Liron Sasonker - 207354366
#Avigail Benitta - 209476621
#Daniel Yehudai - 209089911
#Daniella Graham 209611995


# https://github.com/Varsul17/Homework/blob/main/Tasks/Task%201



def sumatrix(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("The matrices do not have the same size")
        return None
    else:
        newmat = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                newmat[i][j] = mat1[i][j] + mat2[i][j]
        return newmat


def printmat(mat):
    for i in range(len(mat)):
        print(mat[i])
    print()


def MultiplyMatrix(matrixA, matrixB):
    """
    Function for multiplying 2 matrices.

    :param matrixA: Matrix (nxn)
    :param matrixB: Matrix (nxn)
    :return: Multiplication result matrix
    """
    # Initialize the result matrix filled with zeros
    result = [[0 for y in range(len(matrixB[0]))] for x in range(len(matrixA))]

    # Iterate through rows of matrixA
    for i in range(len(matrixA)):
        # Iterate through columns of matrixB
        for j in range(len(matrixB[0])):
            # Iterate through rows of matrixB
            for k in range(len(matrixB)):
                # Perform the matrix multiplication and accumulate the result
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    # Return the final result matrix
    return result


if __name__ == "__main__":
    mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    mat2 = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]]
    print("Matrix 1 is: ")
    printmat(mat1)
    print("Matrix 2 is: ")
    printmat(mat2)
    print("The sum of the matrices is:")
    result = sumatrix(mat1, mat2)
    if result is not None:
        printmat(result)
        print("The multiplying of the matrices is:")
        MultiplyResult = MultiplyMatrix(mat1, mat2)
        printmat(MultiplyResult)
