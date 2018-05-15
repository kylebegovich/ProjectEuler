from math import sqrt
import heapq

INFINITY = 2147483646


def heuristic(curr, length):
    return 2 * int(sqrt((length - curr[0])**2 + (length - curr[1])**2))


def init_grid():

    matrix = open("p083_matrix.txt", 'r')

    grid = list()

    for line in matrix:
        line_arr = line.split(',')
        temp = list()
        for elem in line_arr:
            temp.append(int(elem))
        grid.append(temp)

    return grid


def reconstruct_path(came_from, curr):
    total_path = [curr]
    while curr in came_from.keys():
        curr = came_from[curr]
        total_path.append(curr)
    return total_path


def get_neighbors(curr, grid):

    length = len(grid)
    row = curr[0]
    col = curr[1]

    if row == 0 and col == 0:                                                                   # top left
        grid[row][col] += min([grid[row + 1][col], grid[row][col + 1]])
    elif row == 0 and col == length - 1:                                                        # top right
        grid[row][col] += min([grid[row + 1][col], grid[row][col - 1]])
    elif row == length - 1 and col == length - 1:                                               # bottom right
        grid[row][col] += min([grid[row - 1][col], grid[row][col - 1]])
    elif row == length - 1 and col == 0:                                                        # bottom left
        grid[row][col] += min([grid[row - 1][col], grid[row][col + 1]])

    elif row == 0 and col != length - 1:                                                        # top
        grid[row][col] += min([grid[row + 1][col], grid[row][col - 1], grid[row][col + 1]])
    elif col == 0 and row != length - 1:                                                        # left
        grid[row][col] += min([grid[row - 1][col], grid[row + 1][col], grid[row][col + 1]])
    elif col == length - 1 and row != 0:                                                        # right
        grid[row][col] += min([grid[row - 1][col], grid[row + 1][col], grid[row][col - 1]])
    elif row == length - 1 and col != 0:                                                        # bottom
        grid[row][col] += min([grid[row - 1][col], grid[row][col + 1], grid[row][col - 1]])

    else:                                                                                       # all other
        grid[row][col] += min([grid[row - 1][col], grid[row + 1][col], grid[row][col - 1], grid[row][col + 1]])


def main():

    # pseudocode from https://en.wikipedia.org/wiki/A*_search_algorithm
    grid = init_grid()
    length = len(grid[0])
    start = (0, 0)
    closed_set = set()
    open_set = [start]
    came_from = dict()
    g_score = dict()
    g_score[start] = 0
    f_score = dict()
    f_score[start] = heuristic(start, length)

    """while len(open_set) != 0:
        curr = heapq.heappop(open_set)
        if curr[0] == length - 1 and curr[1] == length - 1:
            return reconstruct_path(came_from, curr)
    """
    print(heuristic((0, 0), length))
    print(heuristic((5, 0), length))
    print(heuristic((50, 50), length))
    print(heuristic((79, 40), length))
    print(heuristic((79, 50), length))
    print(heuristic((79, 78), length))
    print(heuristic((79, 79), length))


print(main())
