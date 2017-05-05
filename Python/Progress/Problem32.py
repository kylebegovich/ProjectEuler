import math
sup = 10000
inf = 1000


def has_pandigital_set(i):
    condition = True
    if condition:
        return True
    return False


if __name__ == '__main__':

    count = 0

    for i in range(inf, sup+1):
        if has_pandigital_set(i):
            count += 1

    print(count)