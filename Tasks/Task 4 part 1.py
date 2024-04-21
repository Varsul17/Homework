from Quizzes.Quiz01.matrix_utility import *

def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


def linearInterpolation(table_points, point):
    p = []
    result = 0
    flag = 1
    for i in range(len(table_points)):
        p.append(table_points[i][0])
    for i in range(len(p) - 1):
        if i <= point <= i + 1:
            x1 = table_points[i][0]
            x2 = table_points[i + 1][0]
            y1 = table_points[i][1]
            y2 = table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print("\nThe approximation (interpolation) of the point ", point, " is: ", round(result, 4))
            flag = 0
    if flag:
        x1 = table_points[0][0]
        x2 = table_points[1][0]
        y1 = table_points[0][1]
        y2 = table_points[1][1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (point - x1)
        print("\nThe approximation (extrapolation) of the point ", point, " is: ", round(result, 4))


def GaussJordanElimination(matrix, vector):
    """
    Function for solving a linear equation using gauss's elimination method
    :param matrix: Matrix nxn
    :param vector: Vector n
    :return: Solve Ax=b -> x=A(-1)b
    """
    # Pivoting process
    matrix, vector = RowXchange(matrix, vector)
    # Inverse matrix calculation
    invert = InverseMatrix(matrix, vector)
    return MulMatrixVector(invert, vector)


def UMatrix(matrix, vector):
    """
    :param matrix: Matrix nxn
    :return:Disassembly into a  U matrix
    """
    # result matrix initialized as singularity matrix
    U = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # pivoting process
        matrix, vector = RowXchageZero(matrix, vector)
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            # Finding the M(ij) to reset the organs under the pivot
            elementary[j][i] = -(matrix[j][i]) / matrix[i][i]
            matrix = MultiplyMatrix(elementary, matrix)
    # U matrix is a doubling of elementary matrices that we used to reset organs under the pivot
    U = matrix_multiply(U, matrix)
    return U


def LMatrix(matrix, vector):
    """
       :param matrix: Matrix nxn
       :return:Disassembly into a  L matrix
       """
    # Initialize the result matrix
    L = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # pivoting process
        matrix, vector = RowXchageZero(matrix, vector)
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            # Finding the M(ij) to reset the organs under the pivot
            elementary[j][i] = -(matrix[j][i]) / matrix[i][i]
            # L matrix is a doubling of inverse elementary matrices
            L[j][i] = (matrix[j][i]) / matrix[i][i]
            matrix = MultiplyMatrix(elementary, matrix)

    return L


def solveMatrix(matrixA, vectorb):
    detA = Determinant(matrixA, 1)

    if detA != 0:
        result = GaussJordanElimination(matrixA, vectorb)
        return result
    else:
        result = MultiplyMatrix(LMatrix(matrixA, vectorb), UMatrix(matrixA, vectorb))
        return result


def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points]  # Makes the initial matrix
    b = [[point[1]] for point in table_points]
    matrixSol = solveMatrix(matrix, b)
    result = sum([matrixSol[i][0] * (x ** i) for i in range(len(matrixSol))])
    print(f"\nThe Result of P(X={x}) is:", )
    print(result)
    return result


if __name__ == '__main__':
    table_points = [(1, 3), (2, 6), (3, 9)]
    x_data = [1, 2, 3]
    y_data = [3, 6, 9]
    x = 1.5
    valid = True
    while (valid):
        print("You can solve the problem in 3 ways:\n"
              "1. lagrange interpolation\n"
              "2. linear Interpolation\n"
              "3. polynomial Interpolation\n"
              "What way will you chose?")
        interpolationMethod = input()
        valid = False
        if interpolationMethod == "1":
            print("By the lagrange interpolation")
            print("y is: ", lagrange_interpolation(x_data, y_data, x))
        elif interpolationMethod == "2":
            print("By the polynomial interpolation")
            linearInterpolation(table_points, x)
        elif interpolationMethod == "3":
            print("By the linear Interpolation")
            polynomialInterpolation(table_points, x)
        else:
            print("incorrect option please try again")
            valid = True
