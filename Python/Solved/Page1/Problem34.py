import math

upper_limit = 2540160


def is_digit_factorial(n):
    summation = 0
    num = n
    while num > 0:
        summation += int(math.factorial(int(num % 10)))
        #print(int(math.factorial(int(num % 10))))
        #print(summation)
        num = int(num / 10)

    if summation == n:
        print("true")
        return True
    return False


if __name__ == '__main__':
    summation = 0
    for x in range(3, upper_limit):
        if is_digit_factorial(x):
            summation += x
            print(x, summation)
    print(summation)


# SOLVED : 40730
