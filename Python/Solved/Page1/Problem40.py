import math


def generate_fancy_number():
    i = 1
    number = ""
    while len(number) < 1000000:
        number += str(i)
        i += 1
        print (i, len(number))

    return number


if __name__ == '__main__':
    number = generate_fancy_number()
    my_set = [int(number[0]), int(number[9]), int(number[99]), int(number[999]), int(number[9999]), int(number[99999]), int(number[999999])]
    print (my_set)
    product = 1
    for i in my_set:
        product *= i
    print (product)


# SOLVED : 210
