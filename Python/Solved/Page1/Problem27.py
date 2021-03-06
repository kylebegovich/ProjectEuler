import math


def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False

    return [i for i in primes if primes[i]==True]


if __name__ == '__main__':

    aMax = 0
    bMax = 0
    nMax = 0
    primes = set(primes_sieve(87400))

    for a in range (-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            while abs(n * n + a * n + b) in primes:
                n += 1

            if n > nMax:
                aMax = a
                bMax = b
                nMax = n

    print(aMax, bMax, nMax)


# SOLVED : -59231
