in_a = 1
in_b = 2
in_c = 0
in_summation = 2
in_maximum = 4000000


def main(a, b, c, summation, maximum):
    while True:
        c = a + b
        a = b + c
        b = c + a
        if b < maximum:
            summation += b
        else:
            break

    return summation


print(main(in_a, in_b, in_c, in_summation, in_maximum))


# SOLVED : 4613732
