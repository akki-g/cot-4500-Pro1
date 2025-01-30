from ..main.assignment_1 import *
import math

#approximation test
aproxX, aproxIter = root_approximation()
print("Root approximation: ", aproxX, " after ", aproxIter, " iterations")
print("\n\n\n")


#bisection test
def test_func(x):
    return x**3 + 4*x**2 - 10

bisectionIter = bisection_method(test_func, 1, 2, 1e-3)
print("Bisection method converges after", bisectionIter, " iterations")
print("\n\n\n")

#fixed point iter test
def test1(x):
    return (x - x*x*x - 4*x*x + 10)
def test2(x):
    return ((10 - x**3)**0.5)/2
def test3(x):
    return (x**2 - 1)/3
def test4(x):
    return math.tan(x)

fixedPointX, fixedPointIter, fixedPointStatus = fixed_point_iter(test1)
print("Fixed point iteration with x-x^3-4x^2+10: ", fixedPointX, " after ", fixedPointIter, " iterations. Status: ", fixedPointStatus)

fixedPointX, fixedPointIter, fixedPointStatus = fixed_point_iter(test2)
print("Fixed point iteration with (10-x^3)^0.5/2: ", fixedPointX, " after ", fixedPointIter, " iterations. Status: ", fixedPointStatus)

fixedPointX, fixedPointIter, fixedPointStatus = fixed_point_iter(test3, p0=0)
print("Fixed point iteration with (x^2-1)/3: ", fixedPointX, " after ", fixedPointIter, " iterations. Status: ", fixedPointStatus)

fixedPointX, fixedPointIter, fixedPointStatus = fixed_point_iter(test4, p0=4, tol=1e-4)
print("Fixed point iteration with tan(x): ", fixedPointX, " after ", fixedPointIter, " iterations. Status: ", fixedPointStatus)
print("\n\n\n")

#newtons test

def test(x):
    return math.cos(x) - x
def test_prime(x):
    return -math.sin(x) - 1
newtIter = newtons(test, test_prime, 0, (math.pi/2), 1e-3)
print("Newtons method with a=0 b=π/2 converges after", newtIter, " iterations")
newtIter = newtons(test, test_prime, 0.5, (math.pi/4), 1e-3)
print("Newtons method with a=0.5 b=π/4 converges after", newtIter, " iterations")

