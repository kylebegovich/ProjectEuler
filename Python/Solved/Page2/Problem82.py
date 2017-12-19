matrix = open("text_files/p082_matrix.txt", 'r')

grid = list()

for line in matrix:
    line_arr = line.split(',')
    temp = list()
    for elem in line_arr:
        temp.append(int(elem))
    grid.append(temp)

length = len(grid)
sol = [0] * length

for i in range(length):
    sol[i] = grid[i][length-1]

for i in range(length - 2, -1, -1):
    sol[0] += grid[0][i]

    for j in range(1, length):
        sol[j] = min(sol[j-1] + grid[j][i], sol[j] + grid[j][i])

    for j in range(length - 2, -1, -1):
        sol[j] = min(sol[j], sol[j+1] + grid[j][i])


print(min(sol))


# SOLVED : 260324
