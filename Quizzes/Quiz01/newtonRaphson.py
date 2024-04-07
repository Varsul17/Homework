
def newton_raphson(f, a, b, tol=1e-6, max_iter=100):
    def df(x):
        # Approximate derivative using central difference method
        h = 1e-6
        return (f(x + h) - f(x - h)) / (2 * h)

    roots = []
    already_found = set()  # Set to keep track of roots already found
    for x in range(a, b):
        x0 = float(x)
        iterations = 0  # Initialize iterations counter

        # Check if function value is close to zero at the current point
        if abs(f(x0)) < tol:
            rounded_x0 = round(x0,5)
            if (rounded_x1 > a and rounded_x1 < b):
             if rounded_x0 not in already_found:  # Check if root has already been found
                roots.append((rounded_x0, iterations))  # Append root and iterations
                already_found.add(rounded_x0)
            continue

        # Avoid division by zero
        if abs(df(x0)) < tol:
            continue

        # Newton-Raphson iteration
        for _ in range(max_iter):
            x1 = x0 - f(x0) / df(x0)
            iterations += 1  # Increment iterations counter
            if abs(x1 - x0) < tol:
                rounded_x1 = round(x1,5)
                if(rounded_x1>a and rounded_x1<b):
                 if rounded_x1 not in already_found:  # Check if root has already been found
                     roots.append((rounded_x1, iterations))  # Append root and iterations
                     already_found.add(rounded_x1)
                break
            x0 = x1

    return roots


if __name__ == '__main__':
    f = lambda x: x**3 - 3 * x ** 2

    roots = newton_raphson(f, -3, 5)
    print("Roots are:")
    for root, iterations in roots:
        print("Root:", root)