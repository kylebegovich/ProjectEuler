import math
from decimal import *

start = 1000000000000
goal = 0.5


def condition(blue, red, total):
    """ checks if the kinda odd condition described in the problem is met or not """

    if Decimal((blue/total) * ((blue - 1)/(total - 1))) == Decimal(1/2):
        print (blue, red, total, "W O A H D O O D")
        return True
    else:
        print (blue, red, total, "false")
        return False


def need_total_increment(blue, total):
    if (blue - 0.0)/(total - 0.0) * (blue - 1.0)/(total - 1.0) > goal + 0.000000000001:
        return True
    else:
        return False


if __name__ == '__main__':

    getcontext().prec = 100

    total = float(start)
    blue = math.floor((total + 0.0) * math.sqrt(0.5))
    red = float(total - blue)

    print(Decimal(1/2), Decimal(0.5), Decimal(1/2)*Decimal(2))

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
