import itertools
import math


def generate_pannumerals(size):
    list = []
    for i in range(1, size+1):
        list.append(i)
    perms = itertools.permutations(list)
    to_ret = []

    for perm in perms:
        cat = ""
        for p in perm:
            cat += str(p)

        to_ret.append(int(cat))
        print (cat)

    return to_ret


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':

    maximum = -1
    for i in range(2, 10):
        arr = generate_pannumerals(i)
        i += 1

        for pan in arr:
            if is_prime(pan):
                if pan > maximum:
                    maximum = pan
                    print ("FREAK THE FREAK OUT", pan)

    print ("Maximum: ", maximum)

# SOLVED : 7652413
