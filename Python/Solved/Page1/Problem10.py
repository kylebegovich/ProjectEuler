from Euler import prime_sieve


in_ceiling = 2000000


def main(ceiling):
    primes = prime_sieve(ceiling)
    return sum(primes)


print(main(in_ceiling))


# SOLVED : 142913828922
