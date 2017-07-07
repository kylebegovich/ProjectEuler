import math

L = 333333333   # 1,000,000,000 / 3


def heron_area(side_double, side_other):

    """assuming side_double is the same length for two sides of the triangle"""
    p = (side_double + side_double + side_other) / 2
    return math.sqrt(p * (p-side_double) * (p-side_double) * (p-side_other))


if __name__ == '__main__':

    summation = 0

    for side in range(2, L+1):
        if heron_area(side, side-1).is_integer():
            summation += (3*side) - 1
            print(side, "-")
        elif heron_area(side, side+1).is_integer():
            summation += (3 * side) + 1
            print(side, "+")

    print(summation)


# SOLVED :
