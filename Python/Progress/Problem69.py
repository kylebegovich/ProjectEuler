from math import sqrt


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


L = 10 ** 6
primes = prime_sieve(int(1.2*sqrt(L)))
del primes[:int(0.6*len(primes))]


if __name__ == '__main__':
    try:
        max_q = 0
        best_n = 0
        i = 0
        for p1 in primes:
            i += 1
            for p2 in primes[i:]:
                if (p1 + p2) % 9 != 1:
                    continue
                n = p1 * p2

                if n > L:
                    print ("the total, overall max is: ", best_n)
                    raise StopIteration

                phi = (p1 - 1) * (p2 - 1)
                ratio = n / float(phi)
                if ratio > max_q:
                    max_q = ratio
                    best_n = n
                    print("new max: ", best_n, max_q)
    except StopIteration:
        print ("done")
