from ..main.assignment_1 import *
import math

#approximation test
aproxX, aproxIter = root_approximation()
print("Root approximation: ", aproxX, " after ", aproxIter, " iterations")
print("\n\n\n")


#bisection test
def test_func(x):
    return x**3 + 4*x**2 - 10

p, bisectionIter = bisection_method(test_func, 1, 2, 1e-3)
print("Bisection method with x^3 + 4x^2 - 10 converges to", p, "after", bisectionIter, "iterations")
print("\n\n\n")

#fixed point iter test
def test1(x):
    return (x - x*x*x - 4*x*x + 10)
def test2(x):
    return ((10 - x**3)**0.5)/2
fixedPointX, fixedPointIter, fixedPointStatus = fixed_point_iter(test1)
print(f"\nFixed point iteration with x-x^3-4x^2+10: {fixedPointX} after {fixedPointIter} iterations, {fixedPointStatus}!")
print("\n")
fixedPointX, fixedPointIter, fixedPointStatus = fixed_point_iter(test2)
print(f"\nFixed point iteration with x-x^3-4x^2+10: {fixedPointX} after {fixedPointIter} iterations, {fixedPointStatus}!")
print("\n\n\n")

#newtons test

def test(x):
    return math.cos(x) - x
def test_prime(x):
    return (-math.sin(x) - 1)
error = 1e-10
newtIter = newtons(test, test_prime, (math.pi/4), error)
print(f"\nNewtons with p0=π/4 with error tolerance {error} converges after {newtIter} iterations")
error = 1e-4
newtIter = newtons(test, test_prime, (math.pi/4), error)
print(f"\nNewtons with p0=π/4 with error tolerance {error} converges after {newtIter} iterations")
