import math


def digi_sum(num):
    return sum([int(d) for d in str(num)])


if __name__ == '__main__':

    maximum = 0

    for a in range(99, 1, -1):
        for b in range(99, 1, -1):
            temp = digi_sum(a**b)
            if temp > maximum:
                print("new max: ", temp)
                maximum = temp

    print("final max: ", maximum)


# SOLVED : 972
