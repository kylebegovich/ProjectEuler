import math

upper_bound = 1000000


def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return int(''.join(map(str, digits[::-1])))


def is_palindromic_number(n):
    if str(n) == str(n)[::-1]:
        print(n, "true")
        return True
    return False


if __name__ == '__main__':
    print(10)
    print(number_to_base(10, 2))

    summation = 0
    for i in range(0, upper_bound):
        if is_palindromic_number(i) and is_palindromic_number(number_to_base(i, 2)):
            summation += i
            print (i, summation)

    print (summation)


# SOLVED : 872187
