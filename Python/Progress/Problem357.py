from math import sqrt
from Euler import prime_sieve


# for i in range(50):
#     print(i, unique_divisors(i))

N = 100000000

primes = set(prime_sieve(N))

def meets_criteria(n):
    if 1 + n not in primes:
        return False
    if 2 + n // 2 not in primes:
        return False
    divisors = [i for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
    for d in divisors:
        print(d, n, d + n // d)
        if d + n // d not in primes:
            return False
    return True

def main(n):
    sum = 1  # as 1 works for the problem, but is the only odd to work, we set step size to 2
    for i in range(2, N+1, 2):
        if (meets_criteria(i)):
            sum += i
            print(i, "meets criteria")

    print(sum)

main(N)


# SOLVED : 1739023853137
