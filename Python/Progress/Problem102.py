from Euler import parse_file


def line_to_triange(line):
    nums = line.split(',')
    # print(nums)
    return [(nums[0], nums[1]), (nums[2], nums[3]), (nums[4], nums[5])]


def is_right_of_origin(points):
    slope = (points[0][1] - points[1][1])/(points[0][0] - points[0][0])
    print(points, slope)
    return True


def point_in_triange(triangle):
    return True


def main():
    lines = parse_file("p102_triangles.txt")
    triangles = [line_to_triange(line) for line in lines]

    return 1

main()
