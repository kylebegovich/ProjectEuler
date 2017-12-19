import math

test = [7, 3, 1, 6, 2, 8, 9, 0]


def check_valid(num):

    num = map(int, list(num))
    counter = 0
    for i in num:
        if counter >= len(test):
            return False
        if i == test[counter]:
            counter += 1
        else:
            counter += 1

    return True


if __name__ == '__main__':

    # open file to read
    attempts = open("text_files/p079_keylog.txt", 'r')

    # do everything else
    for line in attempts:
        if line[0:3].__contains__("9"):
            print(line[0:3])
        if not check_valid(line[0:3]):
            print ("Not a valid test", line, test)
            break

    print ("it worked! hopefully it's a minimum")

    # close file from reading
    attempts.close()


# SOLVED : 73162890     ...     I'll be honest, this one was sort enough that guess and check was sufficient
