from Euler import prime_sieve


in_nums = 20


def main(nums):
    primes = prime_sieve(nums)
    answer = 1
    for i in range(2, nums):
        if i in primes:
            answer *= i
        elif not answer % i == 0:
            for p in primes:
                if i % p == 0 and answer % (i // p) == 0:
                    answer *= p

    return answer


print(main(in_nums))


# SOLVED : 232792560
