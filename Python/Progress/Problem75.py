import numpy as np

# vague algorithm here: https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples


MAX = 1500000
GLOBAL_ARR = list()
A = np.array([[1, -2, 2],
              [2, -1, 2],
              [2, -2, 3]])
B = np.array([[1, 2, 2],
              [2, 1, 2],
              [2, 2, 3]])
C = np.array([[-1, 2, 2],
              [-2, 1, 2],
              [-2, 2, 3]])


def get_children(parent):
    out1 = A.dot(parent)
    out2 = B.dot(parent)
    out3 = C.dot(parent)
    return out1, out2, out3


def apply_primitive_trip(trip, maximum, factor):
    s = sum(trip)
    if s > maximum:
        return False
    while s < maximum:
        curr = trip * factor
        s = sum(curr)
        GLOBAL_ARR[s] = (1 if GLOBAL_ARR[s] == 0 else -1)
        factor += 1
    return True


def main(maximum):
    GLOBAL_ARR = [1] * maximum
    parent = np.array([3, 4, 5])
    outs = get_children(parent)
    for elem in outs:
        print(elem)


print(main(MAX))
