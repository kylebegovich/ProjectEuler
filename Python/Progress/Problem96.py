

def read_from_file(file_name):
    matrix = open(file_name, 'r')

    # init puzzles to [0, set()] for every cell in every puzzle
    puzzles = [[[[0, set()] for k in range(9)] for j in range(9)] for i in range(50)]

    # fill in the actual values
    grid_index = -1
    row_index = 9
    for line in matrix:
        if "Grid" in line:
            row_index = -1
            grid_index += 1
        else:
            col_index = 0
            for e in [int(i) for i in list(line)[:-1]]:
                puzzles[grid_index][row_index][col_index][0] = e
                col_index += 1

        row_index += 1

    return puzzles


def is_puzzle_done(puzzle):
    for row in puzzle:
        for elem in row:
            if elem[0] == 0:
                return False

    return True


def crosshatch(puzzle):
    return puzzle  # write algorithm


def memorization(puzzle):
    return puzzle  # write algorithm


def solve(puzzle_list):
    print("begin solving")
    new_list = []
    for puzzle in puzzle_list:
        while not is_puzzle_done(puzzle):
            puzzle = crosshatch(puzzle)
            puzzle = memorization(puzzle)
        print(puzzle)
        new_list.append(puzzle)

    return new_list


def add_first_three_all_puzzles(puzzles):
    summation = 0
    for puzzle in puzzles:
        first_digit = puzzle[0][0][0]
        second_digit = puzzle[0][1][0]
        third_digit = puzzle[0][2][0]
        summation += (first_digit * 100) + (second_digit * 10) + third_digit

    return summation


def main():
    puzzles = read_from_file("p096_sudoku.txt")
    solved = solve(puzzles)
    summation = add_first_three_all_puzzles(solved)
    return summation


print(main())
