from Euler import parse_file


def line_to_triangle(line):
    nums = line.split(',')
    # print(nums)
    return [(int(nums[0]), int(nums[1])),
            (int(nums[2]), int(nums[3])),
            (int(nums[4]), int(nums[5]))]


def positive_line_intersects(point, line):
    print(line)
    slope = 0
    if line[0][0] - line[1][0] == 0:
        # slope = infinity
        return line[0][0] > point[0], False
    if line[0][1] - line[1][1] == 0:
        # slope = 0, does not intersect y-axis
        return False, line[0][1] > point[1]
    slope = (line[0][1] - line[1][1])/(line[0][0] - line[1][0])

    print(slope)

    x_intersect = (-1 * line[0][1] / slope) + line[0][0]
    y_intersect = slope * -1 * line[0][0] - line[0][1]

    print(x_intersect, y_intersect)

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

    point_in_triangle(origin, [(5, 5), (-10, -3), (1, -15)])

    return 1

main()
