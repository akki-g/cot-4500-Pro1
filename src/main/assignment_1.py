
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
def newtons(func, func_prime, a, b, error_threshold):
    p = func((a+b)/2)
    iter = 0
    max = 1000
    while (iter < max):
        iter += 1
        p = p - func(p) / func_prime(p)
        if (abs(func(p)) < error_threshold):
            break
    return iter