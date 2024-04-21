#Gal Warsulker - 206493173
#Avigail Benitta - 209476621
#Daniel Yehudai - 209089911
#Daniella Graham 209611995

#Git: https://github.com/Varsul17/Homework/blob/main/Tasks/Task%204%20part%202.py


import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral


if __name__ == '__main__':
    f = lambda x: math.sin(x)
    result = trapezoidal_rule(f, 0, math.pi, 4)
    print("Approximate integral:", result, )
