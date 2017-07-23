from Euler import sos_digits

one_set = {1}
eighty_nine_set = {89}


def desent_to_cycle(start, curr):
    if curr in one_set:
        one_set.add(start)
    elif curr in eighty_nine_set:
        eighty_nine_set.add(start)
    else:
        desent_to_cycle(start, sos_digits(curr))


if __name__ == '__main__':
    for i in range(1, 10000001):
        desent_to_cycle(i, i)
        print(i)

    print(len(eighty_nine_set))


# SOLVED : 8581146
