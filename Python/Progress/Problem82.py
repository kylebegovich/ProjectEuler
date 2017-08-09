matrix = open("p082_matrix.txt", 'r')

grid = list()

for line in matrix:
    line_arr = line.split(',')
    temp = list()
    for elem in line_arr:
        temp.append(int(elem))
    grid.append(temp)
    print(temp)

length = len(grid)
