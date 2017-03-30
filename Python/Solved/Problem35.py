import copy

upper_bound = 1000000


def primes_sieve(limit):
    limitn = limit + 1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]]


def is_circular_prime(num, primes):
    """assuming num is already a normal prime"""

    num_of_nums = len(str(num))

    print(num)
    temp = int((num % 10) * 10 ** (num_of_nums - 1)) + int(num / 10)
    print(temp)
    while not temp == n:
        if temp not in primes:
            print("false")
            return False
        temp = int((temp % 10) * 10 ** (num_of_nums - 1)) + int(temp / 10)
        print(temp, n)

    return True


if __name__ == '__main__':
    primes = primes_sieve(upper_bound)
    print(len(primes), primes)

    primes_copy = copy.deepcopy(primes)
    for n in primes_copy:
        print("")
        if not is_circular_prime(n, primes_copy):
            primes.remove(n)

    print(len(primes), primes)


# SOLVED : 55
