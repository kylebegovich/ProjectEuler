from Euler import prime_sieve as sieve


MAX = 1000000
GOAL = 5000


def sum_ways(num, mem, primes):

    if num in mem:
        return mem[num]

    if num in primes:
        noop = 0
        # idk if something should go here...

    ways = 0
    for p in primes:
        curr = num - p
        if curr < 2:
            break
        ways += sum_ways(curr, mem, primes)

    mem[num] = ways
    return ways


def main(MAX, GOAL):
    primes = sieve(MAX)
    mem = dict()
    for i in range(2, MAX):
        if sum_ways(i, mem, primes) >= GOAL:
            return i
        if i == MAX // 3:
            print(mem)


print(main(MAX, GOAL))
