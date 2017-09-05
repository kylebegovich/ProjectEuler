in_a = 600851475143
in_b = 3


def main(a, b):
    while a > b**2:
        if a % b == 0:
            a /= b
        else:
            b += 2
    return int(a)


print(main(in_a, in_b))


# SOLVED : 6857
