


def reverse(n_str):
    return n_str[::-1]



def main(limit):
    count = 0
    n = 1

    while n < limit:
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

        n_sum = n + n_rev
        n_sum_str = [int(d) for d in str(n_sum)]  # this is the other slow line
        for i in range(len(n_sum_str)):
            if n_sum_str[i] % 2 == 0:
                flag = False
                break

        count += 1

        n += 1

    print(count)

# main(30)
# main(999)
print(10 ** 9)
main(10 ** 9)
