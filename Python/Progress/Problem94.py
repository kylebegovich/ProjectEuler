
L = 333333333   # 1,000,000,000 / 3

#  Pell's equation nonsense goes here:
#   https://www.mathblog.dk/project-euler-94-almost-equilateral-triangles/


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


print(main())
