from Euler import is_prime, prime_sieve


guess_upper_bound = 1000000
in_index = 10001


def main(index, upper_bound):
    primes = prime_sieve(upper_bound)
    return primes[index]


print(main(in_index-1, guess_upper_bound))


# SOLVED : 104743
