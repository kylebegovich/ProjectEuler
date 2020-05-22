from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import numpy as np


def u(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10


def eval_poly(coefs, x):
    print(coefs, x)
    rev_coefs = coefs[::-1]
    agg = 0
    for i in range(x-1):
        temp = rev_coefs[i] * (x ** i)
        print("x, i, temp", x, i, temp, np.around(temp))
        agg += np.around(temp)

    print(agg)
    return agg


# first, an attempt to implement lagrange interpolation w/ Scipy and Numpy
def BOP(points, index):
    # print()
    # print("INDEX", index)
    x = np.array(points[:index])
    # print(x)
    w = u(x)
    # print(w)

    poly = lagrange(x, w)
    # print(poly)
    coefs = Polynomial(poly).coef
    # print(coefs)
    return coefs



points = list(range(1,11))
# for p in points:
#     print(p, u(p))

def main():
    agg = 0
    for i in points:
        coefs = BOP(points, i)
        FIT = eval_poly(coefs, i+1)
        agg += FIT

    return agg


print(main())


# SOLVED: 37076114526
