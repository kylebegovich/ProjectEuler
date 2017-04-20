import math

a = 999
b = 999


def is_palendrome(num):
    if num > 100000 and num % 10 == num / 100000:
        num = num % 100000
        num = num / 10
        if num % 10 == num / 1000:
            num = num % 1000
            num = num / 10
            if num % 10 == num / 10:
                return True
    else:
        return False

if __name__ == '__main__':
    while a > 99:
        while b > 99:
            if is_palendrome(a*b):
                print (a*b, a, b)
                break
            else:
                b -= 1
        a -= 1
        b = 999


# SOLVED : 906609
