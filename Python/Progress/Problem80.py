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
    print(s)
    str_list = list(s[s.find('.')+1:])

    return sum([int(c) for c in str_list], 0)


def main(upper_bound):

    upper_bound += 1
    total = 0
    squares = get_squares(upper_bound)

    for i in range(1, upper_bound):
        if i not in squares:
            total += sum_digits_irrat_sqrt(i)
        else:
            print(i**0.5)

    return total


print(main(100))
