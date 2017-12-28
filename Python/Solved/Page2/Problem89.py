input_strs = open("text_files/p089_roman.txt", 'r')
to_replace = ["DCCCC", "LXXXX", "VIIII", "CCCC", "XXXX", "IIII"]


def compress(roman):
    new = roman
    for elem in to_replace:
        new = new.replace(elem, "AA")

    return len(roman) - len(new)


def main():
    saved = 0

    for line in input_strs:
        saved += compress(line)

    print(saved)

    input_strs.close()


main()


# SOLVED : 743
