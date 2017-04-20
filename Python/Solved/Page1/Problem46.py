import math


def gen_primes(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False

    return [i for i in primes if primes[i]==True]


def gen_comp_odds(limit):
    limitn = limit + 1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False

    return [i for i in primes if not primes[i] and i%2 == 1]


def gen_squares(num):
    arr = []
    for i in range(1, num):
        arr.append(i**2)

    return arr



if __name__ == '__main__':
    lim = 10000

    primes = gen_primes(lim)
    print(primes)
    print("done generating primes")

    comp_odds = gen_comp_odds(lim)
    print(comp_odds)
    print("done generating composite odds")

    squares = gen_squares(100)
    print(squares)
    print("done generating squares")

    for curr in comp_odds:
        for prime in primes:
            if prime > curr:
                print(curr, prime, "breaking")
                break
            else:
                temp = curr - prime
                temp /= 2
                if temp in squares:
                    break


# SOLVED : 5777
