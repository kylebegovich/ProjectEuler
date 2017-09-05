in_a = 3
in_b = 5
in_maximum = 1000


def main(a, b, maximum):
    return sum(list(filter((lambda x: x % a == 0 or x % b == 0), range(1, 1000))))


print(main(in_a, in_b, in_maximum))


# SOLVED : 233168
