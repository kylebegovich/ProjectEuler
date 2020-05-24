from Euler import parse_file


X0 = 0
Y0 = 0
TOLERANCE = 0.001

def triangle_area(x_1, y_1, x_2, y_2, x_3, y_3):
    print(x_1, y_1, x_2, y_2, x_3, y_3)
    return abs((x_1*(y_2 - y_3) + x_2*(y_3 - y_1) + x_3*(y_1 - y_2)) / 2)

# attempts to do area calculations for the 4 triangles made with the 4 points
def origin_in_triangle(line):
    values = line.split(",")

    x1 = int(values[0])
    y1 = int(values[1])
    x2 = int(values[2])
    y2 = int(values[3])
    x3 = int(values[4])
    y3 = int(values[5])

    area_full = triangle_area(x1, y1, x2, y2, x3, y3)
    print("area_full", area_full)
    area_1 = triangle_area(X0, Y0, x2, y2, x3, y3)
    print("area_1", area_1)
    area_2 = triangle_area(x1, y1, X0, Y0, x3, y3)
    print("area_2", area_2)
    area_3 = triangle_area(x1, y1, x2, y2, X0, Y0)
    print("area_3", area_3)

    area_sum = area_1 + area_2 + area_3

    print(area_full, area_sum, area_full - area_sum)

    if area_full - area_sum < TOLERANCE:
        return 1

    return 0

def main():
    lines = parse_file("p102_triangles.txt")[:10]
    # triangles = [line_to_triangle(line) for line in lines]

    print("should be 1:", origin_in_triangle("-340,495,-153,-910,835,-947"))
    print("should be 0:", origin_in_triangle("-175,41,-421,-714,574,-645"))

    # return sum([origin_in_triangle(line) for line in lines])



print(main())
