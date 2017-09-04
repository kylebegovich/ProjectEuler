matrix = open("p083_matrix.txt", 'r')

grid = list()

for line in matrix:
    line_arr = line.split(',')
    temp = list()
    for elem in line_arr:
        temp.append(int(elem))
    grid.append(temp)

length = len(grid)

for col in range(length):
    for row in range(length):

        if row == 0 and col == 0:
            grid[row][col] += min([grid[row+1][col], grid[row][col+1]])
        elif row == length - 1 and col == length - 1:
            grid[row][col] += min([grid[row-1][col], grid[row][col-1]])

        elif row == 0 and col != length-1:
            grid[row][col] += min([grid[row+1][col], grid[row][col-1], grid[row][col+1]])
        elif col == 0 and row != length-1:
            grid[row][col] += min([grid[row-1][col], grid[row+1][col], grid[row][col+1]])
        elif col == length-1 and row != 0:
            grid[row][col] += min([grid[row-1][col], grid[row+1][col], grid[row][col-1]])
        elif row == length-1 and col != 0:
            grid[row][col] += min([grid[row-1][col], grid[row][col+1], grid[row][col-1]])

        else:  # if 0 < row < length
            grid[row][col] += min([grid[row-1][col], grid[row+1][col], grid[row][col-1], grid[row][col+1]])

print(grid)


# pretty sure I'm gonna need A*... sad reax
