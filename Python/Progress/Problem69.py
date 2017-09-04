from fractions import gcd
from Euler import prime_sieve


bound = 1000000


def naive():

    curr_max = 1
    for n in range(0, bound+1, 2):

        phi_n = 1
        denom = n / curr_max  # used to prevent too many operations being done within the loop
        for p in range(1, n):
            if gcd(n, p) == 1:
                phi_n += 1
            if denom < phi_n:
                break

        if n / phi_n > curr_max:
            curr_max = n / phi_n
            print("new max:", curr_max, n, phi_n)


def main():
    primes = prime_sieve(500)

    curr = 1
    for i in primes:
        if curr * i > bound:
            return curr
        else:
            curr *= i


print(main())


# SOLVED : 510510
