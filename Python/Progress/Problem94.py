
L = 333333333   # 1,000,000,000 / 3

#  Pell's equation nonsense goes here:
#   https://www.mathblog.dk/project-euler-94-almost-equilateral-triangles/
#   x_k   y_k\sqrt{n} = (x_1   y_1\sqrt{n})^k


def refernce_sol():
    x = 2
    y = 1
    limit = 1000000000
    result = 0

    while (True):
        # b = a+1
        a_times3 = 2 * x - 1
        area_times3 = y * (x - 2)
        if a_times3 > limit:
            break

        if a_times3 > 0 and area_times3 > 0 and a_times3 % 3 == 0 and area_times3 % 3 == 0:
            a = a_times3 / 3
            result += 3 * a + 1

        # b = a - 1
        a_times3 = 2 * x + 1
        area_times3 = y * (x + 2)

        if a_times3 > 0 and area_times3 > 0 and a_times3 % 3 == 0 and area_times3 % 3 == 0:
            a = a_times3 / 3
            result += 3 * a - 1

        nextx = 2 * x + y * 3
        nexty = y * 2 + x

        x = nextx
        y = nexty

    return result

"""
def main():
    summation = 0

    for side in range(2, L+1):
        temp = heron_area(side, side, side-1)
        temp2 = heron_area(side, side, side+1)
        if temp.is_integer():
            summation += (3*side) - 1
            print(side, (3*side) - 1, temp, "-")
        elif temp2.is_integer():
            summation += (3 * side) + 1
            print(side, (3 * side) + 1, temp2, "+")

    print(summation)
"""


print(refernce_sol())
