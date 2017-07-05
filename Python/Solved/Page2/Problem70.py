from math import sqrt


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))


L = 10 ** 7
primes = prime_sieve(int(1.2 * sqrt(L)))
del primes[:int(0.6 * len(primes))]


def pe70(limit):
    min_q = 2
    min_n = 0
    i = 0
    for p1 in primes:
        i += 1
        for p2 in primes[i:]:
            if (p1 + p2) % 9 != 1:
                continue
            n = p1 * p2
            if n > limit:
                return min_n
            phi = (p1 - 1) * (p2 - 1)
            q = n / float(phi)
            if is_perm(phi, n) and min_q > q:
                min_q = q
                min_n = n

    return "done"


print("Project Euler 70 Solution =", pe70(L))


# SOLVED : 8319823
