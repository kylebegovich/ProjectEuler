import math

num = math.factorial(100)


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
        print (n, s)
    return s


if __name__ == '__main__':
    print sum_digits(num)


# SOLVED : 648
