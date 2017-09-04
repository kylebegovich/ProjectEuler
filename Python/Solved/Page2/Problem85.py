

def dims_to_rects(l, w):
    if l < 1 or w < 1:
        return 0
    if l is 1 and w is 1:
        return 1

    curr_sum = 0
    for i in range(l):
        for j in range(w):
            curr_sum += (l - i) * (w - j)

    return curr_sum


def main():
    closestarearects = 0
    closestarea = 0
    target = 2000000

    for i in range(1, 2000):
        for j in range(1, 2000):
            rects = dims_to_rects(i, j)
            if abs(rects - target) < abs(closestarearects - target):
                closestarearects = rects
                closestarea = i * j
            if rects > target:
                break

    print(closestarearects, closestarea)


main()


# SOLVED : 2772
