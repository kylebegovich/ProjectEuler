import math

x = 1
product = 1

def isPrime(x):
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        else:
            i += 1
    return True

if __name__ == '__main__':
    while x < 20:
        if isPrime(x):
            product *= x
            print x
        x += 1

    print product