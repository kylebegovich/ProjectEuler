import math

start = 10
upper_bound = 1000000


def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False

    return [i for i in primes if primes[i]==True]


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_fancy_prime(num):
    length = len(str(num))

    for i in range(length):
        curr = 10**(i+1)
        if not (is_prime(num/curr) and is_prime(num%curr)):
            return False

    return True


if __name__ == '__main__':
    n = start
    answers = []
    potentials = primes_sieve(upper_bound)

    for n in potentials:
        if n < 8:
            continue
        if len(answers) == 15:
            break

        if is_fancy_prime(n):
            print(n, " W O A H,   I T ' S   L I T")
            answers.append(n)

        n += 1

    print(sum(answers))


# SOLVED : 748317
