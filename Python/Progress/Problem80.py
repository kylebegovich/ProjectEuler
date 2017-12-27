from decimal import *
getcontext().prec = 100


def get_squares(upper_bound):

    lst = []
    i = 1
    while i**2 <= upper_bound:
        lst.append(i**2)
        i += 1

    return lst


def sum_digits_irrat_sqrt(num):

    s = str(Decimal(num).sqrt())
    str_list = list(s[s.find('.')+1:])

    total = 0
    for i in str_list:
        total += int(i)

    return total


def main(upper_bound):

    total = 0
    squares = get_squares(upper_bound+1)
    for i in range(2, upper_bound):
        if i not in squares:
            total += sum_digits_irrat_sqrt(i)

    return total


print(main(100))
