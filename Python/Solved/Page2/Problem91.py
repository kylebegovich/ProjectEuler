from Euler import euclidean_dist_sq


def count_bottom_left(bound):
    count = 0

    for i in range(1, bound+1):
        for j in range(1, bound+1):
            print(0, i, '  ', j, 0)
            count += 1

    return count


def count_along_ident(bound):
    count = 0

    for i in range(1, (bound//2) + 1):
        print(0, 2*i, '  ', i, i)
        count += 1

    return count


def is_right_triangle(x1, x2, y1, y2):
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        return False

    s1 = euclidean_dist_sq(0, x1, 0, y1)
    s2 = euclidean_dist_sq(0, x2, 0, y2)
    s3 = euclidean_dist_sq(x1, x2, y1, y2)

    if s1 == 0 or s2 == 0 or s3 == 0:
        return False

    if s1 + s2 == s3 or s1 + s3 == s2 or s2 + s3 == s1:
        #print(x1, x2, y1, y2, '   ', s1, s2, s3)
        return True

    return False


def bruteforce(bound):
    count = 0

    for x1 in range(bound+1):
        for x2 in range(bound + 1):
            for y1 in range(bound + 1):
                for y2 in range(bound + 1):
                    if is_right_triangle(x1, x2, y1, y2):
                        count += 1

    return count//2


def main(bound):
    count = 0

    #count += 3 * count_bottom_left(bound)
    #print()
    #count += 2 * count_along_ident(bound)

    count += bruteforce(bound)

    return count


print(main(50))


# SOLVED : 14234
