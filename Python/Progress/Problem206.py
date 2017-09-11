
# we can figure the last unknown is 0, as our square necessitates the last to end with either 00 or not end with 0
# we can also, since the square now ends in 9, that our square ends with either 3 or 7, and thus must be odd

max_square = 19293949596979899
min_square = 10203040506070809


def is_condition(val):
    string = str(val)
    if string[0] == 1 and string[2] == 2 and string[4] == 3 and string[6] == 4 and \
       string[8] == 5 and string[10] == 6 and string[12] == 7 and string[14] == 8 and string[16] == 9:
        return True
    return False


def main():
    max_val = int(max_square ** 0.5)
    min_val = int(min_square ** 0.5)

    min_val += 2  # round up to the nearest value that ends in 3 or 7

    for i in range(min_val, max_val, 10):  # checks both the 3 and 7 step
        if is_condition(i ** 2):
            return i
        elif is_condition((i + 4) ** 2):
            return i + 4

    return "FAILED"

print(main())
