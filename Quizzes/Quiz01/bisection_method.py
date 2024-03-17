
import numpy as np


"""
Receives 3 parameters:
    1.  a - start value.
    2.  b - end  value. 
    3.  err - value of tolerable error

Returns variables:
    1.  S - The minimum number of iterations required to reach the desired accuracy
"""
def max_steps(a, b, err):
    #Calculates the minimum number of iterations required to reach the desired accuracy
    s = int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))
    return s

"""
Performs Iterative methods for Nonlinear Systems of Equations to determine the roots of the given function f
Receives 4 parameters:
    1. f - continuous function on the interval [a, b], where f (a) and f (b) have opposite signs.
    2. a - start value.
    3. b - end  value. 
    4. tol - the tolerable error , the default value will set as 1e-16

Returns variables:
    1.  c - The approximate root of the function f
"""
def bisection_method(f, a, b, tol=1e-6):
    # Checks if the signs of f(a) and f(b) are the same.
    # If they are, it means the root is not bracketed between a and b.
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("The scalars a and b do not bound a root")
    c, k = 0, 0
    steps = max_steps(a, b, tol)  # calculate the max steps possible

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "f(a)", "b", "f(b)", "c", "f(c)" , "update"))

    # while the diff af a&b is not smaller than tol, and k is not greater than the max possible steps
    while abs(b - a) > tol and k < steps:
        c = ( a + b ) / 2  # Calculation of the middle value

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15}".format(k, a, f(a), b, f(b), c, f(c) , "a=c" if f(c) * f(a) > 0 else "b=c"))

        if f(c) * f(a) > 0:  # if sign changed between steps
            a = c  # move forward
        else:
            b = c  # move backward
        k += 1
    if k == steps:
        print("Maximum number of steps reached without convergence.")

    return c  # return the current root



if __name__ == '__main__': #defining function
    f = lambda x: x**2-6*x+8
    try :
        roots = bisection_method(f, 3, 5)
        print(f"\nThe equation f(x) has an approximate root at x = {roots}")
    except  ValueError as e :
        print(e)
