from Euler import prime_sieve as sieve
from math import sqrt


MAX = 50000000


def comp(square, cube, tetra):
    return int(square**2 + cube**3 + tetra**4)


def main(MAX):
    primes = sieve(int(sqrt(MAX)))
    found = set()
    app = found.add

    for sq in primes:
        for cb in primes:
            for tet in primes:
                c = comp(sq, cb, tet)
                # print(c, sq, cb, tet)
                if c > MAX:
                    break
                if c not in found:
                    app(c)
            c = comp(sq, cb, 2)
            # print(c, sq, cb, 2)
            if c > MAX:
                break
        c = comp(sq, 2, 2)
        # print(c, sq, 2, 2)
        if c > MAX:
            break

    # print(sorted(found))
    return len(found)


print(main(MAX))
