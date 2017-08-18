from copy import deepcopy

from Euler import prime_sieve, is_prime


# we need to replace a modulo 3 set of digits, as if we don't, every third will be divisible by 3 and thus not prime


def fill_pattern(to_fill, number):
    for fi in range(len(to_fill)-1, -1, -1):
        if to_fill[fi] == 1:
            to_fill[fi] = number % 10
            number /= 10
        else:
            to_fill[fi] = -1

    for fi in range(len(to_fill)):
        to_fill[fi] = int(to_fill[fi])

    return to_fill


def generate_number(repeated_num, filled_pattern):
    temp = 0
    for gi in range(len(filled_pattern)):
        temp *= 10
        if filled_pattern[gi] == -1:
            temp += repeated_num
        else:
            temp += filled_pattern[gi]

    return int(temp)


def get_family_size(repeated_num, pattern_fam):
    family_size = 0

    for i in range(repeated_num, 10):
        if is_prime(generate_number(i, pattern_fam)):
            family_size += 1

    return int(family_size)


assumed_bound = 1000000
primes = prime_sieve(assumed_bound)
patterns5 = [[1, 0, 0, 0, 1], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
patterns6 = [[1, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 1],
             [0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1]]


# start main algorithm
def main():
    best = int(1000000)
    for i in range(11, 1000, 2):

        if i % 5 == 0:
            i += 2

        patterns = deepcopy(patterns5)
        if i > 100:
            patterns = deepcopy(patterns6)

        for j in range(len(patterns)):

            pattern = fill_pattern(patterns[j], i)
            for k in range(3):

                if pattern[0] == -1 and k == 0:
                    continue

                candidate = generate_number(k, pattern)

                #  print(i, j, k, patterns[j], pattern, candidate, is_prime(candidate), get_family_size(k, pattern))
                if is_prime(candidate) and get_family_size(k, pattern) >= 8 and candidate < best:

                    best = candidate
                    break

    print(best)

main()


# SOLVED : 121313
