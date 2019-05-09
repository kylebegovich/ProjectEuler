def Chi(n1, n2, n3):
    if (n1 ^ n2 ^ n3) % 2 == 0:
        return 1
    return 0


def main(bound):
    count = 0
    for i in range(bound):
        if Chi(i, 2*i, 3*i) == 0:
            count += 1

    return count



# print(main(2**10))
# print(main(2**30))
print(2**30)
