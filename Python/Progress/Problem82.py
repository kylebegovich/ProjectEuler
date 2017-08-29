matrix = open("p082_matrix.txt", 'r')

grid = list()

for line in matrix:
    line_arr = line.split(',')
    temp = list()
    for elem in line_arr:
        temp.append(int(elem))
    grid.append(temp)

length = len(grid)

for col in range(1, length):

    for row in range(length):
        if row == 0:  # don't check above
            grid[row][col] += min([grid[row+1][col], grid[row][col-1]])
        elif row == length-1:  # don't check below
            grid[row][col] += min([grid[row-1][col], grid[row][col-1]])
        elif 0 < row < length:  # check left, top, and bottom origin points
            grid[row][col] += min([grid[row-1][col], grid[row+1][col], grid[row][col-1]])


minimum = grid[length-1][length-1]
for i in range(length):
    if grid[i][length-1] < minimum:
        minimum = grid[i][length-1]

print(minimum)


# SOLVED : 1432
