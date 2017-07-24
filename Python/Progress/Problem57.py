from Euler import gcd


def simplify(numerator, denominator):
    divis = gcd(numerator, denominator)
    if divis == 1:
        return numerator, denominator
    else:
        return simplify(numerator/divis, denominator/divis)  # recursive call with simplified inputs


def decimal_to_frac(decimal):
    count = 0
    while decimal % 1 > 0:
        decimal *= 10
        count += 1

    return simplify(decimal, 10**count)


def recursive_frac(level, curr):
    woooo = 1


if __name__ == '__main__':

    print(decimal_to_frac(1/3))

    for i in range(1, 1):
        tuple = recursive_frac(i, 1)
