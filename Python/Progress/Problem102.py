from Euler import parse_file


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

    print(line)
    slope = 0
    if x1 - x2 == 0:
        # slope = infinity
        return x1 > point[0], False
    if y1 - y2 == 0:
        # slope = 0, does not intersect y-axis
        return False, y1 > point[1]
    slope = (y1 - y2)/(x1 - x2)

    print(slope)

    x_intersect = (-1 * y1 / slope) + x1
    y_intersect = (-1 * x1 * slope) + y1

    print(x_intersect, y_intersect)
    print(x1, slope, y1)

    return x_intersect > point[0], y_intersect > point[1]


def point_in_triangle(point, triangle):
    print(triangle, point)
    AB_x_sign, AB_y_sign = positive_line_intersects(point, [triangle[0], triangle[1]])
    print(AB_x_sign, AB_y_sign)

    AC_x_sign, AC_y_sign = positive_line_intersects(point, [triangle[0], triangle[2]])
    print(AC_x_sign, AC_y_sign)

    BC_x_sign, BC_y_sign = positive_line_intersects(point, [triangle[1], triangle[2]])
    print(BC_x_sign, BC_y_sign)
    return True


def main():
    origin = (0, 0)
    lines = parse_file("p102_triangles.txt")
    triangles = [line_to_triangle(line) for line in lines]

    point_in_triangle(origin, [(5, 6), (-10, -3), (1, -15)])

    return 1

main()
