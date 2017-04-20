import math

list = []

if __name__ == '__main__':
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            curr = math.pow(a, b)
            if curr not in list:
                list.append(curr)
            print (a, b)

    print len(list)


# SOLVED : 9183
