from math import sqrt

# useful link about Pell's Equation: https://en.wikipedia.org/wiki/Pell%27s_equation


def main(maximum):
    result = 0
    pmax = 0

    squares = set([i ** 2 for i in range(1, int(maximum ** 0.5 + 1))])
    non_squares = [i for i in range(2, maximum+1) if i not in squares]

    for D in non_squares:

        m = 0
        d = 1
        a = int(sqrt(D))

        numm1 = 1
        numerator = a

        denm1 = 0
        denominator = 1

        while ((numerator ** 2) - (D * denominator ** 2)) != 1:  # checks if it satisfies the equation
            m = d * a - m
            d = (D - m * m) // d
            a = (int(sqrt(D)) + m) // d

            numm2 = numm1
            numm1 = numerator
            denm2 = denm1
            denm1 = denominator

            numerator = a * numm1 + numm2
            denominator = a * denm1 + denm2

        if numerator > pmax:
            pmax = numerator
            result = D

    return result


print(main(1000))


# SOLVED : 661
