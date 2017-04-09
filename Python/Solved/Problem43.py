import math
import itertools

to_check = [2, 3, 5, 7, 11, 13, 17]


def generate_pannumerals(size):
    list = []
    for i in range(0, size+1):
        list.append(i)
    perms = itertools.permutations(list)
    to_ret = []

    for perm in perms:
        cat = ""
        for p in perm:
            cat += str(p)

        to_ret.append(cat)
        print (cat)

    return to_ret


def has_property(num):
    for i in range(1, 8):
        converted = int(num[i] + num[i+1] + num[i+2])
        print(converted, to_check[i-1])
        if not converted % to_check[i-1] == 0:
            print("false")
            return False

    return True


if __name__ == '__main__':

    arr = generate_pannumerals(9)
    print(arr)

    summation = 0
    for p in arr:
        if has_property(p):
            print (p)
            summation += int(p)

    print (summation)


# SOLVED : 16695334890
