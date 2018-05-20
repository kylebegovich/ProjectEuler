from decimal import *
getcontext().prec = 102


def get_squares(upper_bound):

    lst = []
    app = lst.append
    i = 1
    while i**2 <= upper_bound:
        app(i**2)
        i += 1

    return lst


def sum_digits_irrat_sqrt(num):

    s = str(Decimal(num).sqrt())
    # print(s)
    str_list = list(s[:-2])

    return sum([int(c) for c in str_list if c != '.'], 0)


def main(upper_bound):

    upper_bound += 1
    total = 0
    squares = get_squares(upper_bound)

    for i in range(1, upper_bound):
        if i not in squares:
            total += sum_digits_irrat_sqrt(i)

    return total


print(main(100))


# SOLVED : 40886
