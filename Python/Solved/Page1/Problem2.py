in_a = 1
in_b = 2
in_c = 0
in_summation = 2
in_maximum = 4000000


def main(a, b, c, summation, maximum):
    while b < maximum:
        summation += b
        c = a + b
        a = b + c
        b = c + a

    return summation


print(main(in_a, in_b, in_c, in_summation, in_maximum))


# SOLVED : 4613732
