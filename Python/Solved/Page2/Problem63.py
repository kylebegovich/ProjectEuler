import math

upper_bound = 22   # 9**22 is only 21 digits long, and thus cannot be


if __name__ == '__main__':

    count = 0

    for pow in range(0, upper_bound):
        for base in range(1, 10):
            temp = base**pow
            if len(str(temp)) == pow:
                count += 1
                print(base, pow, temp)

    print(count)


# SOLVED : 49
