maximum = 10000


def sum_proper_divisors(num):
    divisors = []
    for x in xrange(1, num):
        if float(num) / x == num / x:
            divisors.append(x)
            print x

    return sum(divisors)


def are_amicable_nums(first, second):
    if sum_proper_divisors(first) == second and sum_proper_divisors(second) == first:
        return True
    return False


if __name__ == '__main__':

    print sum_proper_divisors(220)
    print sum_proper_divisors(284)

    found = []
    for x in xrange(maximum):
        for y in xrange(maximum):

            if are_amicable_nums(x, y):
                if not found.__contains__((y, x)):
                    found.append((x, y))
                    print (x, y)

    summation = 0
    for i in xrange(len(found)):
        summation += found[i][0] + found[i][1]

    print summation


# needs time to run, may be solved, may not be