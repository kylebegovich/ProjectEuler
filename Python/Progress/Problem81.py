matrix = open("p081_matrix.txt", 'r')

grid = list()

for line in matrix:
    line_arr = line.split(',')
    temp = list()
    for elem in line_arr:
        temp.append(int(elem))
    grid.append(temp)

length = len(grid)

for i in range(length-2, -1, -1):
    grid[length-1][i] += grid[length - 1][i+1]
    grid[i][length-1] += grid[i+1][length-1]

for i in range(length-2, -1, -1):
    for j in range(length-2, -1, -1):
        grid[i][j] += min(grid[i+1][j], grid[i][j+1])

print(grid[0][0])
