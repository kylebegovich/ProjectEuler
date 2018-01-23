

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


all_1_to_9 = set(range(1, 10))


def crosshatch(puzzle):
    #  Note: this is a single pass-through, not a repeated process
    #  Rows
    for row in puzzle:
        elems = [row[i][0] for i in range(9)]
        c = elems.count(0)
        if c == 0 or c > 1:
            continue
        missing_val = (list((all_1_to_9 - set(elems)) - {0}))[0]
        e_index = elems.index(0)
        row[e_index][0] = missing_val

    #for row in nice_puzzle(puzzle)[0]:
        #print(row)
    #print()
    #for row in nice_puzzle(puzzle)[1]:
        #print(row)
    #print("row-col")
    #print()

    #  Columns
    for i in range(9):
        elems = [puzzle[j][i][0] for j in range(9)]
        c = elems.count(0)
        if c == 0 or c > 1:
            continue
        missing_val = (list((all_1_to_9 - set(elems)) - {0}))[0]
        e_index = elems.index(0)
        puzzle[e_index][i][0] = missing_val

    #for row in nice_puzzle(puzzle)[0]:
        #print(row)
    #print()
    #for row in nice_puzzle(puzzle)[1]:
        #print(row)
    #print("col-box")
    #print()

    #  Boxes
    for b in range(9):
        r, c = (b // 3) * 3, (b % 3) * 3
        elems = [puzzle[r][c][0], puzzle[r][c+1][0], puzzle[r][c+2][0],
                 puzzle[r+1][c][0], puzzle[r+1][c+1][0], puzzle[r+1][c+2][0],
                 puzzle[r+2][c][0], puzzle[r+2][c+1][0], puzzle[r+2][c+2][0]]
        c = elems.count(0)
        if c == 0 or c > 1:
            continue
        missing_val = (list((all_1_to_9 - set(elems)) - {0}))[0]
        e_index = elems.index(0)
        r, c = (e_index // 3) * 3, (e_index % 3) * 3
        puzzle[r][c][0] = missing_val

    #for row in nice_puzzle(puzzle)[0]:
        #print(row)
    #print()
    #for row in nice_puzzle(puzzle)[1]:
        #print(row)
    #print("box-mem")
    #print()

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

                #print(row_elems)
                #print(col_elems)
                #print(box_elems)
                #print(invalid_elems)
                #print(possible_elems)
                #print(r, c, tr, tc)

                if len(possible_elems) == 1:
                    puzzle[r][c][0] = possible_elems.pop()
                else:
                    puzzle[r][c][1] = possible_elems

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
    #print("begin solving")
    new_list = []
    count = 0
    for puzzle in puzzle_list:
        while not is_puzzle_done(puzzle):
            #for row in nice_puzzle(puzzle)[0]:
                #print(row)
            #print()
            #for row in nice_puzzle(puzzle)[1]:
                #print(row)
            #print("mem-row")
            #print()

            puzzle = crosshatch(puzzle)
            puzzle = memorization(puzzle)

        count += 1
        print(count)
        for row in nice_puzzle(puzzle)[0]:
            print(row)
        print()
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
