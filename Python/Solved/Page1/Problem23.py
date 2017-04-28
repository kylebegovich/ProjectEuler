import math
lower_bound = 12
upper_bound = 28123

known = {0: 0, 1: 1}
abundant_nums = {}


def sum_proper_divisors(num):
    if known.has_key(num):
        return known[num]

    s = 0
    for x in range(1, num):
        if float(num) / x == float(num / x):
            s += x

    known[num] = s
    return s


def is_sum_of_abundants(num):
    for a in abundant_nums:
        if (num-a) in abundant_nums:
            return True
        elif (num-(2*a)) < 0:
            return False

    return False


if __name__ == '__main__':

    print("establishing abundant numbers")
    for i in range(lower_bound, (upper_bound-lower_bound)+1):
        if sum_proper_divisors(i) > i:
            print(i, "is an abundant number")
            abundant_nums[i] = i

    print("done finding relevant abundant nums")


    summation = 0
    for i in range(1, upper_bound+1):
        if not is_sum_of_abundants(i):
            summation += i
            print(i, "doesn't have an abundant pair")

    print(summation)


# SOLVED : 4179871
