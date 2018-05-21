from itertools import combinations


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
square_nums = [(0, 1), (0, 4), (0, 6), (1, 6), (1, 8), (2, 5), (3, 6), (4, 6)]


def all_possibilities(sides):
    return list(combinations(digits, sides))


def is_valid(cube1, cube2):
    for square in square_nums:
        if not ((square[0] in cube1 and square[1] in cube2) or (square[1] in cube1 and square[0] in cube2)):
            return False

    return True


def main(sides):
    cubes = all_possibilities(sides)
    #print(cubes, len(cubes))

    for i in range(len(cubes)):
        if 9 in cubes[i] and 6 not in cubes[i]:
            cubes[i] = cubes[i] + (6,)

    #print(cubes, len(cubes))
    count = 0

    for cube1 in cubes:
        for cube2 in cubes:
            if is_valid(cube1, cube2):
                #print(cube1, cube2)
                count += 1

    return count//2  # divide by 2 because (cube1, cube2) == (cube2, cube1), and I count both


print(main(6))


# SOLVED : 1217
