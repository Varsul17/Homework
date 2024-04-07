from math import e
import sympy as sp
import math

def SecantMethod(f, check_range, epsilon=0.0001):
    """
    This function find a root to a function by using the secant method by a given list of values to check beetween.
    :param f: The function (as a python function).
    :param check_range: List of values to check between ; e.g (1,2,3,4,5) it will check between 1-2,2-3,....
    :param epsylon: The tolerance of the deviation of the solution ;
    How precise you want the solution (the smaller the better).
    :return:Returns a list roots by secant method ,
    if it fails to find a solutions in the given tries limit it will return an empty list .
    """
    roots = []
    iterCounter = 0
    for i in check_range:
        if i == check_range[-1]:
            break
        for sep in range(0, 10):
            startPoint = round(i + (sep * 0.1), 2)
            endPoint = round(i + ((sep + 1) * 0.1), 2)
            print("Checked range:", startPoint, "-", endPoint)
            local_root = SecantMethodSol(f, startPoint, endPoint, epsilon, iterCounter)
            if local_root is not None and round(local_root, 6) not in roots:
                roots += [round(local_root, 6)]
            else:
                print("Already found that root.")
    return roots


def SecantMethodSol(polynomial, firstGuess, secondGuess, epsilon, iterCounter):
    """
     This function find a root to a function by using the SecantMethod method by a given tow guess.
    :param polynomial: The function on which the method is run
    :param firstGuess: The first guess
    :param secondGuess: The second guess
    :param epsilon: The tolerance of the deviation of the solution
    :param iterCounter: number of tries until the function found the root.
    :return:Returns the local root by Secant method ,
    if it fails to find a solutions in the given tries limit it will return None .
    """
    if iterCounter > 100:
        return

    if abs(secondGuess - firstGuess) < epsilon:  # Stop condition
        print("after ", iterCounter, "iterations The root found is: ", round(secondGuess, 6))
        return round(secondGuess, 6)  # Returns the root found

    next_guess = (firstGuess * polynomial(secondGuess) - secondGuess * polynomial(firstGuess)) / (
                polynomial(secondGuess) - polynomial(firstGuess))

    return SecantMethod(polynomial, secondGuess, next_guess, epsilon, iterCounter + 1)


if __name__ == '__main__':
    roots = []
    my_f = lambda x: x** 2 - 5 * x + 2
    x = sp.symbols('x')
    def Polynomial(X):
        return my_f.subs(x, X)

    x0 = 80
    x1 = 100
    TOL = 1e-6
    N = 20
    checkRange = range(-5, 6)
    roots += SecantMethod(Polynomial, checkRange, 0.0000001)
    print(roots)
    print(f"\n The equation f(x) has an approximate root at x = {roots}", )
