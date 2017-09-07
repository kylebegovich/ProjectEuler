import math


def is_triplet(a, b, c):

    a **= 2
    b **= 2
    c **= 2

    if a + b == c:
        return True

    return False


def main():
    for c in range(1000):
        for b in range(c):
            a = 1000 - b - c
            if is_triplet(a, b, c):
                return a * b * c


print(main())


# SOLVED : 31875000
