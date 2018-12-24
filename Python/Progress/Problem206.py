
# we can figure the last unknown is 0, as our square necessitates the last to end with either 00 or not end with 0

from math import sqrt, floor, ceil

example = "1_2_3_4_5_6_7_8_9"


def is_condition(val):
    # l = [int(d) for d in str(val)]
    #if all(l[2*n] == n+1 for n in range(9)):
        #return True

    for i in range(9):
        if not ((val % (10 ** ((2 * i) + 1))) // (10 ** ((2 * i)))) == (9 - i):
            return False

    return True

    # if (val % 10) // 1 == 9 and \
    #     (val % 1000) // 100 == 8 and \
    #     (val % 100000) // 10000 == 7 and \
    #     (val % 10000000) // 1000000 == 6 and \
    #     (val % 1000000000) // 100000000 == 5 and \
    #     (val % 100000000000) // 10000000000 == 4 and \
    #     (val % 10000000000000) // 1000000000000 == 3 and \
    #     (val % 1000000000000000) // 100000000000000 == 2 and \
    #     (val % 100000000000000000) // 10000000000000000 == 1:
    #         return True
    #
    # return False


def main(min_val, max_val):

    # ends in 9, so must be odd, skip the evens
    for i in range(min_val, max_val, 2):
        if is_condition(i ** 2):
            return (i ** 2) * 10


    return "FAILED"


def better_main(min_val, max_val):
    curr = min_val**2
    diff = (min_val+2)**2 - min_val**2
    max_val = max_val**2

    while curr < max_val:
        for i in range(10000):
            if is_condition(curr):
                return curr * 100, sqrt(curr * 100)
            curr += diff
            diff += 8
        print(curr)

    return "FAILED"


max_val = 138902663  # = int(ceil(sqrt(19293949596979899)))
# max_val = 101010109  # = int(ceil(sqrt(19293949596979899)))
min_val = 101010101  # = int(floor(sqrt(10203040506070809)))
# print(is_condition(12233447506877809))


print(better_main(min_val, max_val))


# SOLVED : 1389019170
