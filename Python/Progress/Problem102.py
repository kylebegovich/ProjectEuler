from Euler import parse_file


# Triangle 


def line_to_triangle(line):
    nums = line.split(',')
    # print(nums)
    return [(int(nums[0]), int(nums[1])),
            (int(nums[2]), int(nums[3])),
            (int(nums[4]), int(nums[5]))]


def positive_line_intersects(point, line):
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    # print(line)
    slope = 0
    if x1 - x2 == 0:
        # slope = infinity
        return x1 > point[0], False
    if y1 - y2 == 0:
        # slope = 0, does not intersect y-axis
        return False, y1 > point[1]
    slope = (y1 - y2)/(x1 - x2)

    # print(slope)

    x_intersect = (-1 * y1 / slope) + x1
    y_intersect = (-1 * x1 * slope) + y1

    # print(x_intersect, y_intersect)
    # print(x1, slope, y1)

    return x_intersect > point[0], y_intersect > point[1]


def point_in_triangle(point, triangle):
    print(triangle, point)
    AB_x_sign, AB_y_sign = positive_line_intersects(point, [triangle[0], triangle[1]])
    # print(AB_x_sign, AB_y_sign)

    AC_x_sign, AC_y_sign = positive_line_intersects(point, [triangle[0], triangle[2]])
    # print(AC_x_sign, AC_y_sign)

    BC_x_sign, BC_y_sign = positive_line_intersects(point, [triangle[1], triangle[2]])
    # print(BC_x_sign, BC_y_sign)

    #begin x splits
    if AB_x_sign and not AC_x_sign and BC_y_sign and triangle[0][0] < point[0]:
        return True
    if not AB_x_sign and AC_x_sign and BC_y_sign and triangle[0][0] < point[0]:
        return True
    if AB_x_sign and not AC_x_sign and not BC_y_sign and triangle[0][0] > point[0]:
        return True
    if not AB_x_sign and AC_x_sign and not BC_y_sign and triangle[0][0] > point[0]:
        return True

    if AB_x_sign and not BC_x_sign and AC_y_sign and triangle[1][0] < point[0]:
        return True
    if not AB_x_sign and BC_x_sign and AC_y_sign and triangle[1][0] < point[0]:
        return True
    if AB_x_sign and not BC_x_sign and not AC_y_sign and triangle[1][0] > point[0]:
        return True
    if not AB_x_sign and BC_x_sign and not AC_y_sign and triangle[1][0] > point[0]:
        return True

    if AC_x_sign and not BC_x_sign and AB_y_sign and triangle[2][0] < point[0]:
        return True
    if not AC_x_sign and BC_x_sign and AB_y_sign and triangle[2][0] < point[0]:
        return True
    if AC_x_sign and not BC_x_sign and not AB_y_sign and triangle[2][0] > point[0]:
        return True
    if not AC_x_sign and BC_x_sign and not AB_y_sign and triangle[2][0] > point[0]:
        return True

    # begin y splits
    if AB_y_sign and not AC_y_sign and BC_x_sign and triangle[0][1] < point[1]:
        return True
    if not AB_y_sign and AC_y_sign and BC_x_sign and triangle[0][1] < point[1]:
        return True
    if AB_y_sign and not AC_y_sign and not BC_x_sign and triangle[0][1] > point[1]:
        return True
    if not AB_y_sign and AC_y_sign and not BC_x_sign and triangle[0][1] > point[1]:
        return True

    if AB_y_sign and not BC_y_sign and AC_x_sign and triangle[1][1] < point[1]:
        return True
    if not AB_y_sign and BC_y_sign and AC_x_sign and triangle[1][1] < point[1]:
        return True
    if AB_y_sign and not BC_y_sign and not AC_x_sign and triangle[1][1] > point[1]:
        return True
    if not AB_y_sign and BC_y_sign and not AC_x_sign and triangle[1][1] > point[1]:
        return True

    if AC_y_sign and not BC_y_sign and AB_x_sign and triangle[2][1] < point[1]:
        return True
    if not AC_y_sign and BC_y_sign and AB_x_sign and triangle[2][1] < point[1]:
        return True
    if AC_y_sign and not BC_y_sign and not AB_x_sign and triangle[2][1] > point[1]:
        return True
    if not AC_y_sign and BC_y_sign and not AB_x_sign and triangle[2][1] > point[1]:
        return True

    return False


def main():
    origin = (0, 0)
    lines = parse_file("p102_triangles.txt")
    triangles = [line_to_triangle(line) for line in lines]

    print(point_in_triangle(origin, [(1,1), (10, 10), (3, 3)]))
    print(point_in_triangle(origin, [(10,1), (-10, 10), (-1, -10)]))
    print(point_in_triangle(origin, [(5,0), (0, 5), (1, -1)]))

    count = 0
    for t in triangles:
        if point_in_triangle(origin, t):
            count += 1

    return count


print(main())
