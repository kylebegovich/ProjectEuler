from Euler import parse_file


X0 = 0
Y0 = 0

def triangle_area(x_1, y_1, x_2, y_2, x_3, y_3):
    return abs((x_1*(y_2 - y_3) + x_2*(y_3 - y_1) + x_3*(y_1 - y_2)) / 2.0)

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
    area_1 = triangle_area(X0, Y0, x2, y2, x3, y3)
    area_2 = triangle_area(x1, y1, X0, Y0, x3, y3)
    area_3 = triangle_area(x1, y1, x2, y2, X0, Y0)

    area_sum = area_1 + area_2 + area_3

    if area_full == area_sum:
        return 1

    return 0

def main():
    lines = parse_file("p102_triangles.txt")
    return sum([origin_in_triangle(line) for line in lines])



print(main())


# SOLVED : 228
