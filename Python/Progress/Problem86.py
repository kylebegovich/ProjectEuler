from math import sqrt


def min_path(lst):
    return sqrt(lst[0]**2 + (lst[1] + lst[2])**2)


def is_min_path_int(lst):
    return True if sqrt(lst[0]**2 + (lst[1] + lst[2])**2).is_integer() else False


def new_boxes(m):
    boxes = []
    app = boxes.append
    for w in range(1, m+1):
        for h in range(w, m+1):
            app([m, w, h])

    return boxes


def naive(goal):
    m = 1
    count = 0
    while count < goal:
        print(m)
        boxes = new_boxes(m)
        for b in boxes:  # sorted(boxes, key=min_path):
            if is_min_path_int([b[0], b[1], b[2]]):
                #print(path, b, count)
                count += 1

        m += 1

    return m-1, count


def ref(target):
    # reference solution from https://www.mathblog.dk/project-euler-86-shortest-path-cuboid/
    l = 2
    count = 0

    while count < target:
        l += 1
        print(l)
        for wh in range(3, 2 * l):
            if sqrt(wh * wh + l * l).is_integer():
                if wh <= l:
                    #print(l, wh, wh // 2, "      less")
                    count += wh // 2
                else:
                    #print(l, wh, 1 + (l - (wh + 1) // 2), "      more")
                    count += 1 + (l - (wh + 1) // 2)

    return l, count


#print(main(1000000))
print(ref(1000000))
