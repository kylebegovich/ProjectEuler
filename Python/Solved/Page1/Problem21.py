maximum = 10000
known = {0: 0, 1: 1}

def sum_proper_divisors(num):
    if known.has_key(num):
        return known[num]

    s = 0
    for x in range(1, num):
        if float(num) / x == float(num / x):
            s += x

    known[num] = s
    return s


def are_amicable_nums(first, second):
    if sum_proper_divisors(first) == second and sum_proper_divisors(second) == first:
        return True
    return False


if __name__ == '__main__':

    print(sum_proper_divisors(220))
    print(sum_proper_divisors(284))

    summation = 0
    for x in range(maximum+1):
        print(x)
        for y in range(x+1, maximum+1):

            if are_amicable_nums(x, y):
                summation += x + y
                print (x, y, summation)

    print(summation)


# SOLVED : 31626
