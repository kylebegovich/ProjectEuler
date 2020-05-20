


def reverse(n_str):
    return n_str[::-1]



def single_step(n, should_print):
    n_str = [int(d) for d in str(n)]  # this is one of the two slow lines
    if n_str[-1] == 0:
        return False

    n_rev = 0
    multiplier = 1
    for digit in n_str:
        n_rev += digit * multiplier
        multiplier *= 10

    flag = True
    n_sum = n + n_rev
    n_sum_str = [int(d) for d in str(n_sum)]  # this is the other slow line
    for i in range(len(n_sum_str)):
        if n_sum_str[i] % 2 == 0:
            flag = False
            break

    if flag:
        if should_print:
            print(n, n_sum, "true")
        return True
    else:
        if should_print:
            print(n, n_sum)
        return False


memo = set()

def main(start, limit):
    count = 0
    n = start

    while n < limit:
        if n in memo:
            count += 1
            # print("caught memo", n)
            n += 2
            continue

        if n == 100000:
            print(n, count)
        if n == 1000000:
            print(n, count)
        if n == 10000000:
            print(n, count)

        n_str = [int(d) for d in str(n)]  # this is one of the two slow lines
        if n_str[-1] == 0:
            n += 1
            continue

        n_rev = 0
        multiplier = 1
        for digit in n_str:
            n_rev += digit * multiplier
            multiplier *= 10

        flag = True
        n_sum = n + n_rev
        n_sum_str = [int(d) for d in str(n_sum)]  # this is the other slow line
        for i in range(len(n_sum_str)):
            if n_sum_str[i] % 2 == 0:
                flag = False
                break

        if flag:
            count += 1
            memo.add(n_rev)
            memo.add(n)
            print(n, n_sum, "true")
            n += 1
        else:
            # print(n, n_sum)
            n += 1

    print(sorted(memo))
    print(count)


def is_reversible(num):
    if num % 10 == 0:
        return False

    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10

    added = num + rev
    while added > 0:
        if (added % 10) % 2 == 0:
            return False
        added = added // 10

    return True

def optimized_brute(limit):
    count = 0
    n = 1
    while n < limit:
        if n % 10000 == 0:
            print(n, count)
        if is_reversible(n):
            count += 1
        n += 1

    print(count)
    return count


# main(1, 30)
# main(1, 1000) # = 120
# main(1, 10000)
# main(1000, 10000)
# main(100000, 500000)
# main(10000, 100000)  # there are 0 of these... interesting
# main(1, 100000)
# main(100000, 120000)
# main(1000000, 1200000)  # there are 0 of these... interesting
# main(10000000, 10100000)
# print(10 ** 9)
# main(1, 10 ** 9)

print(optimized_brute(10 ** 9))
