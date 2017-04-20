import math


def sum_helper(p_index, best_len, primes):
    best = 1  # longest sum so far
    goal = primes[p_index]

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    for i in range(0, p_index):
        print (goal, p_index, i, primes[i], best)
        if primes[i]*best < goal:
            try:
                for j in range(i + best_len - 1, p_index):
                    summation = sum(primes[i:j])
                    print (summation)
                    if summation > goal:
                        raise StopIteration
                    elif summation == goal and (j-i+1) > best:
                        best = (j-i)
                        print(primes[i:j])
            except StopIteration:
                a = 2

    return best


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
    primes = primes_sieve(100)
    print(primes)
    length = len(primes)  # 78,498 for 1,000,000

    best_pair = (0, 0)  # this is the prime, and the length of it's sum, in that order

    for i in range(0, length):
        curr = sum_helper(i, best_pair[1], primes)
        if curr > best_pair[1]:
            print(best_pair, " changed into: ", (primes[i], curr))
            best_pair = (primes[i], curr)


    print(best_pair)