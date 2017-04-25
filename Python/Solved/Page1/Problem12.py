from math import sqrt

goal_divisors = 500


# my version, not nearly quick enough runtime
def num_divisors(num):
    count = 0
    for x in range(1, num):
        if float(num) / x == num / x:
            count += 1

    return count


# stack overfolw ftw
def factors(n):
    return len(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


if __name__ == '__main__':
    index = 1
    curr = 1
    divs = 2
    while divs < goal_divisors:
        index += 1
        curr += index
        divs = factors(curr)
        print (index, curr, divs)

    print (curr, divs)


# SOLVED : 76576500
