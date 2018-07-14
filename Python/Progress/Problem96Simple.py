import sys
import time

# Grid 01
# 123406789
# 456789123
# 789123456
# 234567891
# 567891234
# 891234567
# 345678912
# 678912345
# 912345678

# Grid 01
# 003020600
# 900305001
# 001806400
# 008102900
# 700000008
# 006708200
# 002609500
# 800203009
# 005010300



all_1_to_9 = set(range(1, 10))
L = 9


def read_from_file(file_name):
    matrix = open(file_name, 'r')

    # init puzzles to [0, set()] for every cell in every puzzle
    puzzles = [[[[0, ([0] * 9)] for k in range(9)] for j in range(9)] for i in range(50)]

    #print(puzzles)

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


def is_solution_valid(n_puzzle):
    for i in range(L):
        row = [n_puzzle[i][j][0] for j in range(L)]
        if not all(all_1_to_9) in row:
            return False

    for i in range(9):
        col = [n_puzzle[j][i][0] for j in range(9)]
        if not all(all_1_to_9) in col:
            return False

    for b in range(9):
        r, c = (b // 3) * 3, (b % 3) * 3
        box = [n_puzzle[r][c][0], n_puzzle[r][c+1][0], n_puzzle[r][c+2][0],
               n_puzzle[r+1][c][0], n_puzzle[r+1][c+1][0], n_puzzle[r+1][c+2][0],
               n_puzzle[r+2][c][0], n_puzzle[r+2][c+1][0], n_puzzle[r+2][c+2][0]]
        if not all(all_1_to_9) in box:
            return False

    return True


def get_curr_box(puzzle, r, c):

    # ro and co are the row and column 'origin', where it's the top left of the box
    # ONLY WORKS FOR 9x9
    ro = r - (r % 3)
    co = c - (c % 3)
    return [                     puzzle[ro][co+1][0],   puzzle[ro][co+2][0],
            puzzle[ro+1][co][0], puzzle[ro+1][co+1][0], puzzle[ro+1][co+2][0],
            puzzle[ro+2][co][0], puzzle[ro+2][co+1][0], puzzle[ro+2][co+2][0]]


def update_missing_values(puzzle):
    #print("updating missing values")
    for r in range(L):
        for c in range(L):
            if puzzle[r][c][0] != 0:
                continue
            curr_missing = list(all_1_to_9)
            curr_row = [puzzle[r][i][0] for i in range(L)]
            curr_col = [puzzle[i][c][0] for i in range(L)]
            curr_box = get_curr_box(puzzle, r, c)
            #print(r, c, curr_row, curr_col, curr_box)
            for c_r in curr_row:
                if c_r in curr_missing:
                    curr_missing.remove(c_r)
            for c_c in curr_col:
                if c_c in curr_missing:
                    curr_missing.remove(c_c)
            for c_b in curr_box:
                if c_b in curr_missing:
                    curr_missing.remove(c_b)
            if len(curr_missing) == 1:
                puzzle[r][c][0] = curr_missing[0]
                puzzle[r][c][1] = []
                print(r, c, "is now", puzzle[r][c][0], "    update missing values")
                #return puzzle  # not sure if I should return here, it may break things?
            else:
                puzzle[r][c][1] = curr_missing
            #print(curr_missing)

    return puzzle


def should_add_value(puzzle, loc_row, loc_col):
    possible_values = list(all_1_to_9)
    for k in range(L):
        if puzzle[loc_row][k][0] in possible_values:
            possible_values.remove(puzzle[loc_row][k][0])
    for k in range(L):
        if puzzle[k][loc_col][0] in possible_values:
            possible_values.remove(puzzle[k][loc_col][0])


def mem(puzzle):
    for row in range(L):
        for col in range(L):
            if puzzle[row][col][0] == 0:
                val = should_add_value(puzzle, row, col)
                if val is not None and len(val) == 1:
                    puzzle[row][col] = [val[0], []]
                    print(row, col, "is now", puzzle[row][col], "    mem")
                    return puzzle

    return puzzle


def crosshatch(puzzle):

    # rows
    for r in range(L):
        curr_missing = list(all_1_to_9)
        curr_row = [puzzle[r][i][0] for i in range(L)]
        #print('curr row = ', curr_row)
        for elem in curr_row:
            if elem in curr_missing:
                curr_missing.remove(elem)
            #print(curr_missing)  # the missing values in the row
        for missing_val in curr_missing:
            poss_index = -1
            for c in range(L):
                if missing_val in puzzle[r][c][1]:
                    if poss_index == -1:
                        poss_index = c
                    else:
                        poss_index = -2
                        break
            if poss_index >= 0:
                puzzle[r][poss_index][0] = missing_val
                puzzle[r][poss_index][1] = []
                print(r, poss_index, "is now", missing_val, "    cross row")
                return puzzle

    # columns
    for c in range(L):
        curr_missing = list(all_1_to_9)
        curr_col = [puzzle[i][c][0] for i in range(L)]
        # print(curr_col, curr_missing)
        for elem in curr_col:
            if elem in curr_missing:
                curr_missing.remove(elem)
            # print(curr_missing)  # the missing values in the col
        for missing_val in curr_missing:
            poss_index = -1
            for r in range(L):
                if missing_val in puzzle[r][c][1]:
                    if poss_index == -1:
                        poss_index = r
                    else:
                        poss_index = -2
                        break
            if poss_index >= 0:
                puzzle[poss_index][c][0] = missing_val
                puzzle[poss_index][c][1] = []
                print(poss_index, c, "is now", missing_val, "    cross col")
                return puzzle

    # boxes
    for b in range(9):
        r0, c0 = (b // 3) * 3, (b % 3) * 3
        curr_box = [puzzle[r0][c0][0], puzzle[r0][c0+1][0], puzzle[r0][c0+2][0],
               puzzle[r0+1][c0][0], puzzle[r0+1][c0+1][0], puzzle[r0+1][c0+2][0],
               puzzle[r0+2][c0][0], puzzle[r0+2][c0+1][0], puzzle[r0+2][c0+2][0]]
        print("curr box", curr_box)
        for elem in curr_box:
            if elem in curr_missing:
                curr_missing.remove(elem)
            print(curr_missing)  # the missing values in the box

        for missing_val in curr_missing:
            poss_index = None
            for radd in range(int(L**0.5)):
                r = r0 + radd
                for cadd in range(int(L**0.5)):
                    c = c0 + cadd
                    if missing_val in puzzle[r][c][1]:
                        if poss_index == None:
                            poss_index = (r, c)
                        else:
                            poss_index == None
                            # 'break' both loops
                            radd = L
                            cadd = L
            if poss_index is not None:
                puzzle[poss_index[0]][poss_index[1]][0] = missing_val
                puzzle[poss_index[0]][poss_index[1]][1] = []
                print(poss_index[0], poss_index[1], "is now", missing_val, "    cross box")
                return puzzle

    return puzzle


def print_pretty(puzzle):
    for r in range(L):
        row_to_print = ""
        for c in range(L):
            row_to_print += str(puzzle[r][c][0]) + " "
        print(row_to_print)
    print()


def print_puzzles(puzzles):
    for p in puzzles:
        for line in p:
            print(line)
        print()


def main():
    puzzles = read_from_file("p096_sudoku.txt")
    #puzzles = read_from_file("simple.txt")
    sum = 0
    for p in puzzles:
        while not is_puzzle_done(p):
            # time.sleep(1)
            print()
            print_pretty(p)
            p = update_missing_values(p)
            p = crosshatch(p)
            # p = mem(p)
        if is_solution_valid(p):
            sum += 100 * p[0][0][0] + 10 * p[0][1][0] + p[0][2][0]
            print(sum)
        else:
            print_pretty(p)



print(main())
