


def reverse(n_str):
    return n_str[::-1]


memo = set()


def main(limit):
    count = 0
    n = 1

    while n < limit:
        if n in memo:
            count += 1
            print("caught memo", n)
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
            n += 2
            print(n, n_sum, "true")
        else:
            n += 1
            print(n, n_sum)

    print(sorted(memo))
    print(count)

# main(30)
# main(1000)
main(10000)
# main(100000)
# main(120000)
# print(10 ** 9)
# main(10 ** 9)
