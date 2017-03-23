import math


def get_collatz_count(n):
    count = 1
    while True:
        if n == 1:
            break
        else:
            count += 1
            if n % 2 == 0:
                n = n/2
            else:
                n = 3*n + 1

    return count

if __name__ == '__main__':
    maximum = 1
    for x in xrange(2, 1000000):
        count = get_collatz_count(x)
        if count > maximum:
            maximum = count
            print (maximum, x)

    print maximum
