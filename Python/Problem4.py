import math

a = 999
b = 999
list = {}


def is_palendrome(num):
    if num > 99999 and num % 10 == num / 100000 and num % 100 == num / 10000 and num % 1000 == num / 1000:
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
