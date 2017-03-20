import math


def is_triplet(a, b, c):
    a = math.pow(a,2)
    b = math.pow(b,2)
    c = math.pow(c,2)
    if (a + b == c):
        return True
    return False


if __name__ == '__main__':
    owf = True
    for c in xrange(1000):
        if owf:
            for b in xrange(c):
                if owf:
                    for a in xrange(b):
                        if is_triplet(a, b, c):
                            if a + b + c == 1000:
                                print (a*b*c, a, b, c)
                                owf = False
                                break
                else:
                    break
        else:
            break


# SOLVED : 31875000
