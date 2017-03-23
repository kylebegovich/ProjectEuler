import math

goal_divisors = 501

def num_divisors(num):
    count = 0
    for x in xrange(1, num):
        if float(num) / x == num / x:
            count += 1
            print x

    return count


# need time to run / a more efficient method
if __name__ == '__main__':
    index = 1
    curr = 1
    divs = 2
    while divs < goal_divisors:
        index += 1
        curr += index
        divs = num_divisors(curr)
        print (curr, divs)

    print (curr, divs)
