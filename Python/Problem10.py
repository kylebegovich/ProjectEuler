import math

ceiling = 2000000


def is_prime(x):
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        else:
            i += 1
    return True


if __name__ == '__main__':
    i = 0
    summation = 0
    for x in xrange(2, ceiling):
        if is_prime(x):
            summation += x

    print summation


# SOLVED : 142913828922