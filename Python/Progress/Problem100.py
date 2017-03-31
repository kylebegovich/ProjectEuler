import math

start = 1000000000000
goal = 1.0/2.0


def condition(blue, red, total):
    """ checks if the kinda odd condition described in the problem is met or not """

    if (blue - 0.0)/(total - 0.0) * (blue - 1.0)/(total - 1) == goal:
        print (blue, red, total, "W O A H D O O D")
        return True
    else:
        print (blue, red, total, "false")
        return False


def need_total_increment(blue, total):
    if (blue - 0.0)/(total - 0.0) * (blue - 1.0)/(total - 1) > goal:
        return True
    else:
        return False


if __name__ == '__main__':
    total = start
    blue = math.floor((total + 0.0) * math.sqrt(0.5))
    red = total - blue

    while True:

        if condition(blue, red, total):
            break
        else:
            blue += 1
            red -= 1

        if need_total_increment(blue, total):
            total += 1
            blue = math.floor(total * math.sqrt(0.5))
            red = total - blue


    print(blue, red, total)
