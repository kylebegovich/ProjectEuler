

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


def main():
    puzzles = read_from_file("p096_sudoku.txt")


main()
