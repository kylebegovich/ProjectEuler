import sys


all_1_to_9 = set(range(1, 10))
L = 9


def read_from_file(file_name):
    matrix = open(file_name, 'r')
    num_lines = sum(1 for line in open(file_name, 'r'))

    # init puzzles to 0 for every cell in every puzzle
    puzzles = [[[0 for k in range(9)] for j in range(9)] for i in range(num_lines//10)]

    # print(puzzles)

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
                puzzles[grid_index][row_index][col_index] = e
                col_index += 1

        row_index += 1

    return puzzles


def is_puzzle_done(puzzle):
    for row in puzzle:
        for elem in row:
            if elem == 0:
                return False

    return True

#
# def is_puzzle_valid(puzzle):
#     for r in range(L):
#         for c in range(L):
#             curr = puzzle[r][c][0]
#             if curr == 0:
#                 continue
#             for i in range(L):
#                 if puzzle[r][i][0] == curr and i != c:
#                     print('contradiction:', r, c, puzzle[r][c][0], 'and', r, i, puzzle[r][i][0], 'are in the same row')
#                     return False
#                 if puzzle[i][c][0] == curr and i != r:
#                     print('contradiction:', r, c, puzzle[r][c][0], 'and', i, c, puzzle[i][c][0], 'are in the same column')
#                     return False
#
#             r0, c0 = r - (r % 3), c - (c % 3)
#             curr_box = [puzzle[r0][c0][0],   puzzle[r0][c0+1][0],   puzzle[r0][c0+2][0],
#                         puzzle[r0+1][c0][0], puzzle[r0+1][c0+1][0], puzzle[r0+1][c0+2][0],
#                         puzzle[r0+2][c0][0], puzzle[r0+2][c0+1][0], puzzle[r0+2][c0+2][0]]
#             flag = False
#             for elem in curr_box:
#                 if elem == curr:
#                     if not flag:
#                         flag = True
#                     else:
#                         print('contradiction:', r, c, puzzle[r][c][0], 'and', elem, 'are in the same box')
#                         return False
#
#     return True
#

def get_curr_box(puzzle, r, c):
    # print(r, type(r), c, type(c))
    # ro and co are the row and column 'origin', where it's the top left of the box
    # ONLY WORKS FOR 9x9
    ro = r - (r % 3)
    co = c - (c % 3)
    return [puzzle[ro][co],   puzzle[ro][co+1],   puzzle[ro][co+2],
            puzzle[ro+1][co], puzzle[ro+1][co+1], puzzle[ro+1][co+2],
            puzzle[ro+2][co], puzzle[ro+2][co+1], puzzle[ro+2][co+2]]
#
#
# def guess_next(puzzle):
#     potential_next = []
#     for r in range(L):
#         for c in range(L):
#             if puzzle[r][c][0] != 0:
#                 continue
#             for elem in puzzle[r][c][1]:
#                 copy = dc(puzzle)
#                 copy[r][c][0] = elem
#                 copy[r][c][1] = []
#                 potential_next.append(copy)
#             return potential_next
#
#
# def update_missing_values(puzzle):
#     #print("updating missing values")
#     for r in range(L):
#         for c in range(L):
#             if puzzle[r][c][0] != 0:
#                 continue
#             curr_missing = list(all_1_to_9)
#             curr_row = [puzzle[r][i][0] for i in range(L)]
#             curr_col = [puzzle[i][c][0] for i in range(L)]
#             curr_box = get_curr_box(puzzle, r, c)
#             #print(r, c, curr_row, curr_col, curr_box)
#             for c_r in curr_row:
#                 if c_r in curr_missing:
#                     curr_missing.remove(c_r)
#             for c_c in curr_col:
#                 if c_c in curr_missing:
#                     curr_missing.remove(c_c)
#             for c_b in curr_box:
#                 if c_b in curr_missing:
#                     curr_missing.remove(c_b)
#             if len(curr_missing) == 1:
#                 puzzle[r][c][0] = curr_missing[0]
#                 puzzle[r][c][1] = []
#                 print(r, c, "is now", puzzle[r][c][0], "    update missing values")
#                 #return puzzle  # not sure if I should return here, it may break things?
#             else:
#                 puzzle[r][c][1] = curr_missing
#             #print(curr_missing)
#
#     return puzzle
#
#
# def should_add_value(puzzle, loc_row, loc_col):
#     possible_values = list(all_1_to_9)
#     for k in range(L):
#         if puzzle[loc_row][k][0] in possible_values:
#             possible_values.remove(puzzle[loc_row][k][0])
#     for k in range(L):
#         if puzzle[k][loc_col][0] in possible_values:
#             possible_values.remove(puzzle[k][loc_col][0])
#
#
# def box_helper_function(r0, c0, puzzle, missing_val):
#     poss_index = None
#     for radd in range(int(L**0.5)):
#         r = r0 + radd
#         for cadd in range(int(L**0.5)):
#             c = c0 + cadd
#             print(r, c, puzzle[r][c][0], puzzle[r][c][1])
#             if missing_val in puzzle[r][c][1]:
#                 if poss_index == None:
#                     poss_index = (r, c)
#                 else:
#                     return None;
#     return poss_index
#
#
# def crosshatch(puzzle):
#
#     # rows
#     for r in range(L):
#         curr_missing = list(all_1_to_9)
#         curr_row = [puzzle[r][i][0] for i in range(L)]
#         print('row ', r, '= ', curr_row)
#         for elem in curr_row:
#             if elem in curr_missing:
#                 curr_missing.remove(elem)
#
#         print(curr_missing)  # the missing values in the row
#         for missing_val in curr_missing:
#             poss_index = -1
#             print("curr missing val =", missing_val)
#             for c in range(L):
#                 print(r, c, puzzle[r][c][0], puzzle[r][c][1])
#                 if missing_val in puzzle[r][c][1]:
#                     if poss_index == -1:
#                         poss_index = c
#                     else:
#                         poss_index = -2
#                         break
#             if poss_index >= 0:
#                 puzzle[r][poss_index][0] = missing_val
#                 puzzle[r][poss_index][1] = []
#                 print(r, poss_index, "is now", missing_val, "    cross row")
#                 return puzzle
#
#     print()
#
#     # columns
#     for c in range(L):
#         curr_missing = list(all_1_to_9)
#         curr_col = [puzzle[i][c][0] for i in range(L)]
#         print('col ', c, '= ', curr_col)
#         for elem in curr_col:
#             if elem in curr_missing:
#                 curr_missing.remove(elem)
#
#         print(curr_missing)  # the missing values in the col
#         for missing_val in curr_missing:
#             poss_index = -1
#             print("curr missing val =", missing_val)
#             for r in range(L):
#                 print(r, c, puzzle[r][c][0], puzzle[r][c][1])
#                 if missing_val in puzzle[r][c][1]:
#                     if poss_index == -1:
#                         poss_index = r
#                     else:
#                         poss_index = -2
#                         break
#             if poss_index >= 0:
#                 puzzle[poss_index][c][0] = missing_val
#                 puzzle[poss_index][c][1] = []
#                 print(poss_index, c, "is now", missing_val, "    cross col")
#                 return puzzle
#
#     print()
#
#     # boxes
#     for b in range(9):
#         # for r in range(L):
#         #     for c in range(L):
#         #         print(r, c, puzzle[r][c][0], puzzle[r][c][1])
#         curr_missing = list(all_1_to_9)
#         r0, c0 = (b // 3) * 3, (b % 3) * 3
#         curr_box = [puzzle[r0][c0][0],   puzzle[r0][c0+1][0],   puzzle[r0][c0+2][0],
#                     puzzle[r0+1][c0][0], puzzle[r0+1][c0+1][0], puzzle[r0+1][c0+2][0],
#                     puzzle[r0+2][c0][0], puzzle[r0+2][c0+1][0], puzzle[r0+2][c0+2][0]]
#         print('box ', b, '= ', curr_box)
#         for elem in curr_box:
#             if elem in curr_missing:
#                 curr_missing.remove(elem)
#
#         print(curr_missing) # the missing values in the box
#         for missing_val in curr_missing:
#             print("curr missing val =", missing_val)
#             poss_index = box_helper_function(r0, c0, puzzle, missing_val)
#             if poss_index is not None:
#                 puzzle[poss_index[0]][poss_index[1]][0] = missing_val
#                 puzzle[poss_index[0]][poss_index[1]][1] = []
#                 print(poss_index[0], poss_index[1], "is now", missing_val, "    cross box")
#                 return puzzle
#
#     print("i should do a guess and check")
#     puzzle = guess_and_check(puzzle)
#     return puzzle
#

def solve_puzzle(puzzle):
    print_pretty(puzzle)
    for row in range(len(puzzle)):
        for col in range(len(puzzle)):
            if puzzle[row][col] == 0:
                for value in all_1_to_9:

                    # check not in row
                    if value in puzzle[row]:
                        continue

                    # check not in col
                    column = [puzzle[i][col] for i in range(len(puzzle))]
                    if value in column:
                        continue

                    # check not in box
                    box = get_curr_box(puzzle, row, col)
                    if value in box:
                        continue

                    puzzle[row][col] = value
                    if is_puzzle_done(puzzle):
                      print("Puzzle Complete and Checked")
                      return True
                    else:
                      if solve_puzzle(puzzle):
                        return True
                break
    puzzle[row][col] = 0


def print_pretty(puzzle):
    for r in range(L):
        row_to_print = ""
        for c in range(L):
            row_to_print += str(puzzle[r][c]) + " "
        print(row_to_print)
    print()


def print_puzzles(puzzles):
    for p in puzzles:
        for line in p:
            print(line)
        print()


def main():
    #puzzles = read_from_file("p096_sudoku.txt")
    puzzles = read_from_file("p096_sudoku.txt")
    sum = 0
    count = 1
    for p in puzzles:
        print_pretty(p)
        if solve_puzzle(p):
            count += 1
            sum += 100 * p[0][0] + 10 * p[0][1] + p[0][2]
            print('able to solve p #' + str(count), 'sum = ')
        else:
            print('failed to solve p #' + str(count), ', breaking')
            return -1




def new_main():
    #puzzles = read_from_file("p096_sudoku.txt")
    puzzles = read_from_file("simple.txt")
    sum = 0
    for p in puzzles:
        potent = [p]
        count = 0
        print_pretty(p)
        while not any([is_puzzle_done(p) for p in potent]):
            for p in potent:
                unchanged = dc(p)
                print()
                print_pretty(p)
                time.sleep(1)
                p = update_missing_values(p)
                p = crosshatch(p)
                if p == unchanged:
                    guesses = guess_next(p)
                    for guess in guesses:
                        potent.append(guess)
        if is_solution_valid(p):
            sum += 100 * p[0][0][0] + 10 * p[0][1][0] + p[0][2][0]
            print(sum)
        else:
            print_pretty(p)


# print_puzzles(read_from_file('p096_sudoku.txt'))
print(main())
