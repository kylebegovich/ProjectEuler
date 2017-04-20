import math
import collections

def is_permutation(a, b, c):
    a_list = list(str(a))
    b_list = list(str(b))
    c_list = list(str(c))

    if collections.Counter(a_list) == collections.Counter(b_list) and collections.Counter(a_list) == collections.Counter(c_list):
        return True

    return False

def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False

    return [i for i in primes if primes[i]==True]


if __name__ == '__main__':
    x = 3339
    primes = primes_sieve(10000)
    for i in range(1000, x):
        if i == 1487 or i not in primes or (i+3330) not in primes or (i+6660) not in primes:
            continue
        elif is_permutation(i, i + 3330, i + 6660):
            print(str(i) + str(i + 3330) + str(i + 6660))
            break
        else:
            print(":(")


# SOLVED : 296962999629
