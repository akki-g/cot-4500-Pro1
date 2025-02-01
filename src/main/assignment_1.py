
#root aproximation
def root_approximation(x0=1.5, tol=0.000001, max = 1000):
    iter = 0
    diff = x0
    x = x0

    print("iter: ", iter, " x: ", x, " diff: ", diff)
    while (diff > tol and iter < max):
        iter += 1
        y = x
        x = (x / 2) + (1 / x)
        print("iter: ", iter, " x: ", x, " diff: ", diff)
        diff = abs(x - y)
    print("Convergence reached after ", iter, " iterations")
    return x, iter


#bisection
def bisection_method(func, a, b, error_threshold):
    left = a
    right = b
    iter = 0
    max = 1000
    while (abs(right - left) > error_threshold and iter < max):
        iter += 1
        p = (left + right) / 2
        if ((func(left) < 0 and func(p) < 0) or (func(left) > 0 and func(p) > 0)):
            left = p
        else:
            right = p

    return iter


#fixed point iter
import math

def fixed_point_iter(func, p0=1.5, tol = 0.000001, N0=50):
    i = 1
    p = 0
    p0 = float(p0)
    while (i <= N0):
        p = func(p0)
        if (math.isnan(p)):
            print("result diverges")
            return p, i, "fail"
        if (abs(p - p0) < tol):
            return p, i, "success"
        i += 1
        p0 = p
    return p, i, "fail"


#newtons
import numpy as np
def newtons(func, func_prime, a, b, error_threshold, max = 1000):
    p = np.zeros(1000)
    p[0] = (a + b) / 2
    print("n :", 0, "p[0]: ", p[0])
    n = 1
    while (n < max):
        p[n] = p[n - 1] - func(p[n - 1]) / func_prime(p[n - 1])
        if (abs(p[n] - p[n - 1]) < error_threshold):
            print("n :", n, f"p[{n}]: ", p[n])
            return n
        print("n :", n, f"p[{n}]: ", p[n])
        n += 1
    print("Method failed to converge")