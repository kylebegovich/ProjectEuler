from Euler import prime_sieve, is_prime

# we need to replace a modulo 3 set of digits, as if we don't, every third will be divisible by 3 and thus not prime

assumed_bound = 1000000
primes = prime_sieve(assumed_bound)


def generate_patterns(length):

    # all these patterns have 0's for replacing digits and 1's for non-replacing digits
    if length == 5:
        return [[1, 0, 0, 0, 1],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 0, 1, 1]]
    elif length == 6:
        return [[1, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 1, 1],
                [0, 1, 1, 0, 0, 1],
                [0, 1, 0, 1, 0, 1],
                [0, 1, 0, 0, 1, 1],
                [0, 0, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 1],
                [0, 0, 0, 1, 1, 1]]


def fill_pattern(to_fill, number):
    for fi in range(len(to_fill)):
        if to_fill[fi] == 1:
            to_fill[fi] = number % 10
            number /= 10
        else:
            to_fill[fi] = -1

    return to_fill


def generate_number(repeated_num, filled_pattern):
    temp = 0
    for gi in range(len(filled_pattern)):
        temp *= 10
        if filled_pattern[gi] == -1:
            temp += repeated_num
        else:
            temp += filled_pattern[gi]

    return temp


def get_family_size(repeated_num, pattern_fam):
    family_size = 1

    for i in range(repeated_num, 10):
        if is_prime(generate_number(i, pattern_fam)):
            family_size += 1

    return family_size


# start main algorithm
best = 1000000000
for i in range(11, 1000, 2):

    patterns = generate_patterns(5)
    if i > 100:
        patterns = generate_patterns(6)

    for j in range(len(patterns)):
        for k in range(3):

            if patterns[j][0] == 0 and k == 0:
                continue

            pattern = fill_pattern(patterns[j], i)
            candidate = generate_number(k, pattern)

            if is_prime(candidate) and get_family_size(k, pattern) >= 8 and candidate < best:
                # best = candidate
                print("answer: ", candidate, i, j, k)
                break


# SOLVED :
