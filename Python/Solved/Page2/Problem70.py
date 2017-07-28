from math import sqrt


# Problem:

# Euler's Totient function, phi(n) [sometimes called the phi function],
# is used to determine the number of positive numbers less than or equal to n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so phi(1)=1.

# Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

# Find the value of n, 1 < n < 107, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))


if __name__ == "__main__":

    LIMIT = 10 ** 7
    primes = prime_sieve(int(1.2 * sqrt(LIMIT)))
    del primes[:int(0.6 * len(primes))]

    min_q = 2
    min_n = 0
    i = 0

    try:
        for curr_prime in primes:
            i += 1
            for p2 in primes[i:]:
                if (curr_prime + p2) % 9 != 1:
                    continue
                n = curr_prime * p2
                if n > LIMIT:
                    raise StopIteration
                phi = (curr_prime - 1) * (p2 - 1)
                q = n / float(phi)
                if is_perm(phi, n) and min_q > q:
                    min_q = q
                    min_n = n

    except StopIteration:
        print("Project Euler 70 Solution =", min_n)

    print("Done")


# SOLVED : 8319823
