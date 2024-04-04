from math import e
import sympy as sp
import math


def EvaluateError(startPoint, endPoint):
    """
    This function Helps us find out if we can find a root in a limited amount of tries in a specific range.
    :param startPoint: start of range.
    :param endPoint: end of range.
    :return:
    """
    exp = pow(10, -10)
    if endPoint - startPoint == 0:
        return 100
    return ((-1)*math.log(exp/(endPoint-startPoint), e))/math.log(2, e)


def NewtonsMethod(f, x0, tries=100, epsylon=0.0001, symbole=sp.symbols('x')):
    """
    This function find a root to a function by using the newton raphson method by a given first guess.
    :param f: The function with sympy symbols.
    :param x0: The first guess.
    :param tries: Number of tries to find the root.
    :param symbole: The symbol you entered in the function (Default is lower case x)
    :param epsylon: The tolerance of the deviation of the solution ;
    How precise you want the solution (the smaller the better).
    :return:Returns the local root by raphson method ,
    if it fails to find a solutions in the given tries limit it will return None .
    """
    for i in range(tries):
        print("Attempt #", i + 1, ":")
        print("f({0}) = {1} = {2}".format(x0, f, round(f.subs(symbole, x0), 2)))
        print("f'({0}) = {1} = {2}".format(x0, sp.diff(f, symbole),
                                           round(sp.diff(f, symbole).subs(symbole, x0), 2)))
        if sp.diff(f, symbole).subs(symbole, x0) == 0.0:
            continue
        next_x = (x0 - f.subs(symbole, x0) / sp.diff(f, symbole).subs(symbole, x0))

        print("next_X = ", round(next_x, 2))
        t = abs(next_x - x0)
        if t < epsylon:
            print("Found a Root Solution ; X =", round(next_x, 8))
            return next_x
        x0 = next_x
    print("Haven't Found a Root Solution ; (returning None)")
    return None


def NewtonsMethodInRangeIterations(f, check_range, tries=10, epsilon=0.0001, symbol=sp.symbols('x')):
    """
    This function find a root to a function by using the newton raphson method by a given list of guesses.
    :param f: The function with sympy symbols.
    :param check_range: List of guesses.
    :param tries: Number of tries to find the root.
    :param symbole: The symbol you entered in the function (Default is lower case x)
    :param epsylon: The tolerance of the deviation of the solution ;
    How precise you want the solution (the smaller the better).
    :return:Returns a list roots by raphson method ,
    if it fails to find a solutions in the given tries limit it will return an empty list .
    """
    roots = []
    for i in check_range:
        if i == check_range[-1]:
            break
        for sep in range(0, 10):
            check_number = round(i + (sep * 0.1), 2)
            print("First guess:", check_number)
            local_root = NewtonsMethod(f, check_number, tries, epsilon, symbol)
            if local_root is not None and round(local_root,6) not in roots:
                roots+=[round(local_root,6)]
                print(roots)
                for i in range(0, 100):
                    print()
            else:
                print("Already found that root.")

    return roots


def SecantMethodInRangeIterations(f, check_range, epsilon=0.0001):
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
            endPoint = round(i + ((sep+1) * 0.1), 2)
            print("Checked range:", startPoint, "-",endPoint)
            local_root = SecantMethod(f, startPoint, endPoint, epsilon, iterCounter)
            if local_root is not None and round(local_root,6) not in roots:
                roots += [round(local_root,6)]
            else:
                print("Already found that root.")
    return roots


def SecantMethod(polynomial,firstGuess, secondGuess,epsilon, iterCounter):
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

    if abs(secondGuess - firstGuess) < epsilon: #Stop condition
        print("after ", iterCounter, "iterations The root found is: ",round(secondGuess, 6))
        return round(secondGuess, 6) # Returns the root found

    next_guess = (firstGuess * polynomial(secondGuess) - secondGuess * polynomial(firstGuess))/(polynomial(secondGuess) - polynomial(firstGuess))

    return SecantMethod(polynomial, secondGuess, next_guess, epsilon, iterCounter+1)



if __name__ == "__main__":
    roots = []
    valid = True
    x = sp.symbols('x')

    # if you want to try other functions please change here my_f

    my_f = x**2 + 3*x + 2


    ##my_f = x**2-4*x
    # my_f = x**3-sp.cos(x)

    def Polynomial(X):
        return my_f.subs(x, X)


    my_f_diff = lambda a: sp.diff(my_f, x).subs(x, a)

    checkRange = range(-5, 6)
    epsilon = 0.0001

    print("Finding roots of the equation\n")
    choice = int(input(
        "Which method Which methods do you want? \n\t1.Newton Raphson\n\t2.Secant Method\n"))
    if choice == 1:
        roots += NewtonsMethodInRangeIterations(my_f, checkRange, 10, 0.000001)
    elif choice == 2:
        roots += SecantMethodInRangeIterations(Polynomial, checkRange, 0.0000001)
    else:
        print("Invalid input")
        valid = False

    if valid:
        print("\nThere are ", len(roots), "roots: ", roots)
