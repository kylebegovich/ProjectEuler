import math

upper_bound = int(6 * math.pow(9, 5) + 1)
numbers = []


def sum_pow_of_digits(num):
    summation = 0
    while num > 0:
        summation += int(math.pow(int(num % 10), 5))
        num = int(num / 10)

    return summation
    

if __name__ == '__main__':

    for curr in xrange(2, upper_bound):
        if curr == sum_pow_of_digits(curr):
            numbers.append(curr)
            print curr

    print numbers
    print sum(numbers)


# SOLVED : 443839
