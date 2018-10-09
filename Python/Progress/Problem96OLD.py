import sys


all_1_to_9 = set(range(1, 10))
verbose = False


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
    #  Note: this is a single pass-through, not a repeated process
    #  Rows
    for i in range(9):
        elems = [puzzle[i][j][0] for j in range(9)]
        c = elems.count(0)
        if c == 0 or c > 1:
            continue
        missing_val = (list((all_1_to_9 - set(elems)) - {0}))[0]
        e_index = elems.index(0)
        if verbose:
            print("writing (row)", missing_val, " into (", i, e_index, ")")
        if verbose and puzzle[i][e_index][0] != 0:
            print("I AM MAD, DON'T DO THIS!")
        puzzle[i][e_index][0] = missing_val
        return puzzle

    #  Columns
    for i in range(9):
        elems = [puzzle[j][i][0] for j in range(9)]
        c = elems.count(0)
        if c == 0 or c > 1:
            continue
        missing_val = (list((all_1_to_9 - set(elems)) - {0}))[0]
        e_index = elems.index(0)
        if verbose:
            print("writing (col)", missing_val, " into (", e_index, i, ")")
        if verbose and puzzle[e_index][i][0] != 0:
            print("I AM MAD, DON'T DO THIS!")
        puzzle[e_index][i][0] = missing_val
        return puzzle

    #  Boxes
    for b in range(9):
        r, c = (b // 3) * 3, (b % 3) * 3
        elems = [puzzle[r][c][0], puzzle[r][c+1][0], puzzle[r][c+2][0],
                 puzzle[r+1][c][0], puzzle[r+1][c+1][0], puzzle[r+1][c+2][0],
                 puzzle[r+2][c][0], puzzle[r+2][c+1][0], puzzle[r+2][c+2][0]]
        count = elems.count(0)
        if count == 0 or count > 1:
            continue

        e_index = elems.index(0)
        missing_val = (list((all_1_to_9 - set(elems)) - {0}))[0]

        #  e = 0, 1, 2 -> r += 0; 3, 4, 5 -> r += 1; 6, 7, 8 -> r += 2
        #  e = 0, 3, 6 -> c += 0; 1, 4, 7 -> c += 1; 2, 5, 8 -> c += 2
        r += e_index // 3
        c += e_index % 3

        if verbose:
            print("writing (box)", missing_val, " into (", r, c, ")")
        if verbose and puzzle[r][c][0] != 0:
            print("I AM MAD, DON'T DO THIS!")
        puzzle[r][c][0] = missing_val
        return puzzle

    return puzzle


def memorization(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c][0] == 0:
                row_elems = [puzzle[r][i][0] for i in range(9)]
                col_elems = [puzzle[i][c][0] for i in range(9)]
                tr = (r // 3) * 3
                tc = (c // 3) * 3
                box_elems = [puzzle[tr][tc][0], puzzle[tr][tc+1][0], puzzle[tr][tc+2][0],
                             puzzle[tr+1][tc][0], puzzle[tr+1][tc+1][0], puzzle[tr+1][tc+2][0],
                             puzzle[tr+2][tc][0], puzzle[tr+2][tc+1][0], puzzle[tr+2][tc+2][0]]

                invalid_elems = set(row_elems + col_elems + box_elems) - {0}
                possible_elems = all_1_to_9 - invalid_elems
                if verbose:
                    print("( r c ) = (", r, c, ") invalid elems =", invalid_elems, "   possible elems =", possible_elems)

                if len(possible_elems) == 1:
                    new_elem = possible_elems.pop()
                    if verbose:
                        print("writing (mem)", new_elem, "into (", r, c, ")")
                    puzzle[r][c][0] = new_elem
                    puzzle[r][c][1] = set()
                    return puzzle
                else:
                    puzzle[r][c][1] = possible_elems

    return puzzle


def is_valid_solution(n_puzzle):
    print(n_puzzle)

    for row in n_puzzle:
        if not all(all_1_to_9) in row:
            return False

    for i in range(9):
        col = [n_puzzle[j][i] for j in range(9)]
        if not all(all_1_to_9) in col:
            return False

    for b in range(9):
        r, c = (b // 3) * 3, (b % 3) * 3
        box = [n_puzzle[r][c], n_puzzle[r][c+1], n_puzzle[r][c+2],
               n_puzzle[r+1][c], n_puzzle[r+1][c+1], n_puzzle[r+1][c+2],
               n_puzzle[r+2][c], n_puzzle[r+2][c+1], n_puzzle[r+2][c+2]]
        if not all(all_1_to_9) in box:
            return False


def mem_extrapolate(puzzle):

    #  Rows
    for i in range(len(puzzle)):
        row = puzzle[i]
        elems = [row[j][0] for j in range(9)]
        c = elems.count(0)
        if c <= 1:
            continue
        missing_vals = sorted(list(all_1_to_9 - set(elems) - {0}))

        potential_vals = list()
        for j in range(9):
            tupe = row[j]
            if tupe[0] == 0:
                potential_vals.append((list(tupe[1]), j))

        for indv_val in missing_vals:
            is_unique = False
            e_index = -1
            for indv_pot_vals in potential_vals:
                if indv_val in indv_pot_vals[0] and not is_unique:
                    is_unique = True
                    e_index = indv_pot_vals[1]
                elif indv_val in indv_pot_vals[0] and is_unique:
                    is_unique = False
                    break
            if is_unique:
                if verbose:
                    print("trying to write ROW")
                    print(puzzle[i][e_index][0], " into ", indv_val, ", and it can be", puzzle[i][e_index][1])
                if puzzle[i][e_index][0] == 0 and indv_val in puzzle[i][e_index][1]:
                    if verbose:
                        print("actually doing it too!")
                    puzzle[i][e_index][0] = indv_val
                    puzzle[i][e_index][1] = set()
                    return puzzle
                if verbose:
                    print()

    #  Columns
    for i in range(len(puzzle)):
        col = [puzzle[j][i] for j in range(9)]
        elems = [col[j][0] for j in range(9)]
        c = elems.count(0)
        if c <= 1:
            continue
        missing_vals = sorted(list(all_1_to_9 - set(elems) - {0}))

        potential_vals = list()

        for j in range(9):
            tupe = col[j]
            if tupe[0] == 0:
                potential_vals.append((list(tupe[1]), j))

        for indv_val in missing_vals:
            is_unique = False
            e_index = -1
            for indv_pot_vals in potential_vals:
                if indv_val in indv_pot_vals[0] and not is_unique:
                    is_unique = True
                    e_index = indv_pot_vals[1]
                elif indv_val in indv_pot_vals[0] and is_unique:
                    is_unique = False
                    break
            if is_unique:
                if verbose:
                    print("trying to write col")
                    print(puzzle[e_index][i][0], " into ", indv_val, ", and it can be", puzzle[e_index][i][1])
                if puzzle[e_index][i][0] == 0 and indv_val in puzzle[e_index][i][1]:
                    if verbose:
                        print("actually doing it too!")
                    puzzle[e_index][i][0] = indv_val
                    puzzle[e_index][i][1] = set()
                    return puzzle
                if verbose:
                        print()

    #  Boxes
    for b in range(9):
        r, c = (b // 3) * 3, (b % 3) * 3
        elems = [puzzle[r][c][0], puzzle[r][c+1][0], puzzle[r][c+2][0],
                 puzzle[r+1][c][0], puzzle[r+1][c+1][0], puzzle[r+1][c+2][0],
                 puzzle[r+2][c][0], puzzle[r+2][c+1][0], puzzle[r+2][c+2][0]]
        c = elems.count(0)
        if c <= 1:
            continue
        missing_vals = sorted(list((all_1_to_9 - set(elems)) - {0}))
        potential_vals = list()

        tupes = [puzzle[r][c], puzzle[r][c+1], puzzle[r][c+2],
                 puzzle[r+1][c], puzzle[r+1][c+1], puzzle[r+1][c+2],
                 puzzle[r+2][c], puzzle[r+2][c+1], puzzle[r+2][c+2]]

        for j in range(9):
            if tupes[j][0] == 0:
                potential_vals.append((list(tupes[j][1]), j))

        for indv_val in missing_vals:
            is_unique = False
            e_index_row, e_index_col = -1, -1
            temp_ipvs = []
            for indv_pot_vals in potential_vals:
                if indv_val in indv_pot_vals[0] and not is_unique:
                    is_unique = True
                    e_index_row, e_index_col = (indv_pot_vals[1] // 3), (indv_pot_vals[1] % 3)
                    temp_ipvs = indv_pot_vals
                elif indv_val in indv_pot_vals[0] and is_unique:
                    is_unique = False
                    break
            if is_unique:
                if verbose:
                    print("trying to write box at", e_index_row, e_index_col)
                    print("from", puzzle[e_index_row][e_index_col][0], " to ", indv_val, ", and it can be", puzzle[e_index_row][e_index_col][1])
                    print("\n", temp_ipvs)
                if puzzle[e_index_row][e_index_col][0] == 0 and indv_val in puzzle[e_index_row][e_index_col][1]:
                    if verbose:
                        print("actually doing it too!")
                    puzzle[e_index_row][e_index_col][0] = indv_val
                    puzzle[e_index_row][e_index_col][1] = set()
                    return puzzle
                if verbose:
                        print()

    return puzzle


def nice_puzzle(puzzle):
    n1 = [[0 for i in range(9)] for i in range(9)]
    n2 = [[0 for i in range(9)] for i in range(9)]
    for row in range(9):
        for col in range(9):
            n1[row][col] = puzzle[row][col][0]
            n2[row][col] = puzzle[row][col][1]

    return n1, n2


def solve(puzzle_list):
    if verbose:
        print("begin solving")
    new_list = []
    count = 0
    for puzzle in puzzle_list:

        cycles = 0
        while not is_puzzle_done(puzzle):

            puzzle = crosshatch(puzzle)
            if verbose:
                for row in nice_puzzle(puzzle)[0]:
                    print(row)
                print("\nMem:")

            puzzle = memorization(puzzle)

            if verbose:
                for row in nice_puzzle(puzzle)[0]:
                    print(row)
                print("\nMem Extrapolate:")


            puzzle = mem_extrapolate(puzzle)
            cycles += 1

            if verbose:
                for row in nice_puzzle(puzzle)[0]:
                    print(row)
                print("\nCross")
                print("cycles = ", cycles)

        if verbose:
            print("\nfinished a puzzle in ", cycles, "cycles!\n\n")
            for row in nice_puzzle(puzzle)[0]:
                print(row)
            print()

        if not is_puzzle_done(puzzle):
            print("bad solution generated!")
            return

        count += 1
        print("COUNT =", count)
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


def read_from_file2(file_name):
    matrix = open(file_name, 'r')

    # init puzzles to [0, set()] for every cell in every puzzle
    puzzles = [[[0 for k in range(9)] for j in range(9)] for i in range(50)]

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


# ----- from https://www.reddit.com/r/ProgrammerHumor/comments/7yecbo/my_conjecture_any_solvable_problem_can_be/ -------
lambda grid: all(map(lambda x: len(x) == len(set(x)),grid + list(zip(*tuple(grid))) + [(lambda a: list(a[0]+a[1]+a[2]))(list(zip(*tuple(grid[3*y:3*y+3])))[3*x:3*x+3]) for x in range(3) for y in range(3)]))


def main2():
    puzzles = read_from_file("p096_sudoku.txt")
    solved_list = []
    for puzz in puzzles:
        solved_list.append(grid(puzz))
    summation = add_first_three_all_puzzles(solved_list)
    return summation


def main():
    puzzles = read_from_file("p096_sudoku.txt")
    solved = solve(puzzles)
    summation = add_first_three_all_puzzles(solved)
    return summation


# verbosity flag setting
if len(sys.argv) > 1 and sys.argv[1] == "-v":
    verbose = True

print(main2())
