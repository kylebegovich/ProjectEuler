import math
from decimal import *
prec = 1000

def get_repeater_length(num):
    frac = Decimal(1)/num
    checker = list(str(int(frac*10**16)))
    print(frac, checker)

    for i in range(2, (prec-6)):
        if str(int(frac*10**i)) == checker[10]:
            if str(int(frac*10**(i+1))) == checker[11] and str(int(frac*10**(i+2))) == checker[12] \
                    and str(int(frac*10**(i+3))) == checker[13] and str(int(frac*10**(i+4))) == checker[14] \
                    and str(int(frac*10**(i+5))) == checker[15]:
                return i
            else:
                print("false flag")

    print("BROKEN SOMETHING, SEND HELP")
    return -1

if __name__ == '__main__':

    getcontext().prec = prec
    best_pair = (7, 6)

    for i in range(1, 100):
        curr = get_repeater_length(Decimal(i))
        if curr > best_pair[1]:
            print(best_pair, "changed into:", (i, curr))
            best_pair = (i, curr)

    print(best_pair)
