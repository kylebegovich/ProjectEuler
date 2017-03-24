import math

check = [11, 13, 14, 16, 17, 18, 19, 20]
minimum = 2520


def find_evenly_divis(step):

    num = minimum

    while True:
        if all(num % n == 0 for n in check):
            return num
        num += step


if __name__ == '__main__':
    print find_evenly_divis(20)


# SOLVED : 232792560
