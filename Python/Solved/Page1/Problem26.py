def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False

    return [i for i in primes if primes[i]==True]


def get_repeater_length(blank, num):
    for t in range(1, num):
        if 1 == 10 ** t % num:
            return t
    return 0


if __name__ == '__main__':
    longest = max(get_repeater_length(1, i) for i in range(2, 1001))
    print([i for i in range(2, 1001) if get_repeater_length(1, i) == longest][0])


# SOLVED : 983
