import math


def is_prime(x):
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        else:
            i += 1
    return True

if __name__ == '__main__':
    product = 1
    for x in xrange(2, 20):
        if is_prime(x):
            product *= x
            print (x, product)
        x += 1

    print (product, product/19/17/13/11/7/5/3/2)
    print (math.factorial(10))
