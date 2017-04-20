import math

def isPrime(x):
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        else:
            i += 1
    return True

if __name__ == '__main__':
    index = 3
    actual = 3
    while index < 10003:
        actual += 2
        if isPrime(actual):
            index += 1
            print actual


# SOLVED : 104743