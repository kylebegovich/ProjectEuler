import math
sup = 100000
inf = 100

pandigital_set = {}


def is_pandigital(multiplicand, multiplier, product):
    temp_str = str(multiplicand) + str(multiplier) + str(product)

    print(multiplicand, multiplier, product, temp_str)

    if len(temp_str) != 9:
        return False

    temp_set = set(temp_str)
    if len(temp_set) == 9 and '0' not in temp_set:
        print("TRUE: ", set(temp_str))
        return True


def has_pandigital_set(num):
    if num in pandigital_set:
        print("this shouldn't happen, but it did:", num)
        return

    square = int(math.sqrt(num))
    for x in range(1, square):

        factor = (0.0 + num) / (x + 0.0)
        if factor.is_integer():
            if is_pandigital(x, int(factor), num):
                return True

    return False


if __name__ == '__main__':

    count = 0

    for i in range(inf, sup+1):
        if has_pandigital_set(i):
            count += i

    print(count)


# SOLVED : 45228
