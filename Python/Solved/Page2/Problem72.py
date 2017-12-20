from Euler import totient


# this problem just asks you to sum up the phi(n) for n between 2 and 1,000,000


# This is optimized to run in a good amount of time
def phi_thing(limit):
    phi = list(range(0, limit + 1))

    result = 0
    for i in range(2, limit + 1):

        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] = phi[j] / i * (i - 1)
        result += phi[i]

    return int(result)


def count_possible_fracts(limit):

    result = 0
    for i in range(2, limit + 1):
        result += totient(i)

    return result


def main():
    given_limit = 1000000
    test_limit = 8
    print(phi_thing(test_limit))
    print(phi_thing(given_limit))


main()


# SOLVED : 303963552391
