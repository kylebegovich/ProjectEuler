from math import sqrt, floor

# useful link about Pell's Equation: https://en.wikipedia.org/wiki/Pell%27s_equation

"""
Define x(0) = 1, x(1) = a(n), x(i+2) = 2*a(n)*x(i+1) - x(i) for i >= 0
Then x(i) satisfies the Pell equation x^2 - D*y^2 = 1
"""


def y(n):
    return 7


def a(n):
    return sqrt(1 + (n + int(floor(1/2 + sqrt(n))))*y(n)^2)


def x(n):
    if n == 0:
        return 1
    if n == 1:
        return a(n)
    return 2 * a(n) * x(n - 1) - x(n - 2)


