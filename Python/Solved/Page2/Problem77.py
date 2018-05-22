from Euler import prime_sieve as sieve


MAX = 1000
GOAL = 5000


def bruteforce(m, goal):
    primes = sieve(m)
    ways = [0] * (m + 1)
    ways[0] = 1

    #print(primes)
    #print(ways)

    for p in primes:
        for i in range(p, m + 1):
            ways[i] += ways[i - p]

    return ways


def main(m, goal):
    ways = bruteforce(m, goal)

    for i in range(m+1):
        if ways[i] > goal:
            return i


print(main(MAX, GOAL))


# SOLVED : 71
