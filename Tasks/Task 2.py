import numpy as np

def jacobi_method(A, b, tol=0.001):
    n = len(A)
    x = np.zeros(n)
    iteration = 0
    print("Iteration |          x")
    print("-" * 30)
    print(f"    {iteration:<8} | {' | '.join([f'{val:.8f}' for val in x])}")
    while True:
        x_new = np.zeros(n)
        for i in range(n):
            sum_val = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum_val) / A[i, i]
        iteration += 1
        x_str = ' | '.join([f"{val:.8f}" for val in x_new])
        print(f"    {iteration:<8} | {x_str}")
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new

def gauss_seidel_method(A, b, tol=0.001):
    n = len(A)
    x = np.zeros(n)
    iteration = 0
    print("Iteration |          x")
    print("-" * 30)
    print(f"    {iteration:<8} | {' | '.join([f'{val:.8f}' for val in x])}")
    while True:
        for i in range(n):
            sum_val = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - sum_val) / A[i, i]
        iteration += 1
        x_str = ' | '.join([f"{val:.8f}" for val in x])
        print(f"    {iteration:<8} | {x_str}")
        if np.linalg.norm(np.dot(A, x) - b) < tol:
            return x

def check_diagonal_dominance(A):
    n = len(A)
    for i in range(n):
        if 2 * abs(A[i, i]) <= sum(abs(A[i, :])) - abs(A[i, i]): # Checking strong diagonal dominance
            print("The matrix is not diagonally dominant.")
            return False
    return True



def main():
    A = np.array([[3, -1, 1],
                  [0, 1, -1],
                  [1, 1, -2]])
    b = np.array([4, -1, -3])

    if check_diagonal_dominance(A):
        print("Jacobi Method:")
        solution_jacobi = jacobi_method(A, b)
        print("Solution:", solution_jacobi)

        print("\nGauss-Seidel Method:")
        solution_gauss_seidel = gauss_seidel_method(A, b)
        print("Solution:", solution_gauss_seidel)


if __name__ == "__main__":
    main()