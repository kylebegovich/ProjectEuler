
# Huge props to Euler's generating function, link here: https://en.wikipedia.org/wiki/Partition_%28number_theory%29


def main(first_div_by):
    partitions = [1]
    n = 0
    while True:
        i = 0
        curr_pent = 1
        partitions.append(0)

        while curr_pent <= n:
            sign = -1 if i % 4 > 1 else 1
            partitions[n] += sign * partitions[n - curr_pent]
            partitions[n] %= first_div_by
            i += 1

            j = int((i / 2 + 1)) if i % 2 == 0 else int(-(i / 2 + 1))
            curr_pent = int(j * (3 * j - 1) / 2)

        if partitions[n] == 0:
            return n
        n += 1


print(main(1000000))


# SOLVED : 55374
