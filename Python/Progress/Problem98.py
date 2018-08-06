
def read_from_file(filename):
    words = open(filename, 'r')

    reference = ""
    for line in words:
        reference = line[:-1].split(",")

    words.close()
    return reference


def main():
    reference = read_from_file('p098_words.txt')
    # for r in reference:
    #     print(r)


main()
