import math


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


if __name__ == '__main__':
    count = 0

    """
    for n in range(22, 101):
        try:
            temp = int(math.ceil(n/2.0)) + 1
            for r in range(1, temp):
                if nCr(n, r) > 1000000:
                    if (temp-1) % 2 == 0:
                        count += 2 * (temp - r)
                    else:
                        count += 2 * (temp - r) - 1
                    raise StopIteration

        except StopIteration:
            print("broke loop")
    """

    for n in range(22, 101):
        print("n = ", n)
        for r in range(2, n):
            if nCr(n, r) > 1000000:
                count += 1

    print(count)


# SOLVED : 4075
