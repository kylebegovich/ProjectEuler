import numpy as np

# vague algorithm here: https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples


MAX = 1500000
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


def apply_primitive_trip(trip, maximum, factor, unique_lengths):
    #print(trip)
    s = sum(trip)
    #print(s)
    if s > maximum:
        return False
    while s < maximum:
        unique_lengths[s] = (1 if unique_lengths[s] == 0 else -1)
        factor += 1
        curr = trip * factor
        s = sum(curr)
        #print(s)
    return True


def follow_tree(parent, maximum, unique_lengths):
    #print("follow tree", parent)
    temp = apply_primitive_trip(parent, maximum, 1, unique_lengths)
    if temp:
        for elem in get_children(parent):
            follow_tree(elem, maximum, unique_lengths)


def main(maximum):
    unique_lengths = [0] * (maximum + 1)
    parent = np.array([3, 4, 5])

    #print(unique_lengths)
    follow_tree(parent, maximum, unique_lengths)

    print(unique_lengths)
    count = 0
    for elem in unique_lengths:
        if elem == 1:
            count += 1

    return count

print(main(MAX))


# SOLVED: 161667
