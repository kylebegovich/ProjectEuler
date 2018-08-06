from math import sqrt
import heapq
import time

INFINITY = 2147483646


def heuristic(curr, length):
    return sum(abs(length - 1 - curr[i]) for i in range(len(curr)))


def init_grid():
    matrix = open("text_files/p083_matrix.txt", 'r')
    grid = list()

    for line in matrix:
        line_arr = line.split(',')
        temp = list()
        for elem in line_arr:
            temp.append(int(elem))
        grid.append(temp)

    matrix.close()
    # print(grid)
    return grid


def sum_path(path, grid):
    out = 0
    for term in path:
        out += grid[term[0]][term[1]]

    return out


def get_neighbors(curr, grid):

    length = len(grid)
    row = curr[0]
    col = curr[1]

    if row == 0 and col == 0:                                                                   # top left
        return [(row + 1, col), (row, col + 1)]
    elif row == 0 and col == length - 1:                                                        # top right
        return [(row + 1, col), (row, col - 1)]
    elif row == length - 1 and col == 0:                                                        # bottom left
        return [(row - 1, col), (row, col + 1)]
    elif row == length - 1 and col == length - 1:                                               # bottom right
        return [(row - 1, col), (row, col - 1)]

    elif row == 0 and col != length - 1:                                                        # top
        return [(row + 1, col), (row, col + 1), (row, col - 1)]
    elif col == 0 and row != length - 1:                                                        # left
        return [(row + 1, col), (row - 1, col), (row, col + 1)]
    elif col == length - 1 and row != 0:                                                        # right
        return [(row + 1, col), (row - 1, col), (row, col - 1)]
    elif row == length - 1 and col != 0:                                                        # bottom
        return [(row - 1, col), (row, col + 1), (row, col - 1)]

    else:                                                                                       # all other
        return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def main():

    # pseudocode from https://en.wikipedia.org/wiki/A*_search_algorithm
    grid = init_grid()
    length = len(grid[0])
    start = (0, 0)
    closed_set = set()
    open_set = {(0, 0)}
    frontier_queue = [(4603, [start])]

    g_score = dict()
    g_score[start] = 4603
    f_score = dict()
    f_score[start] = heuristic(start, length)

    best_answer = INFINITY

    while len(open_set) != 0:
        # time.sleep(1)
        # print(open_set)
        obj = heapq.heappop(frontier_queue)
        path = obj[1]
        curr = path[-1]
        # print("path =", path)
        # print("curr =", curr)
        if curr[0] == length - 1 and curr[1] == length - 1:
            answer = sum_path(path, grid)
            if answer < best_answer:
                best_answer = answer
            # for p in path[::-1]:
            #     print(p)

        open_set.remove(curr)
        closed_set.add(curr)

        for neighbor in get_neighbors(curr, grid):
            # print("neighbor:", neighbor)
            if neighbor in closed_set or neighbor in open_set:
                continue

            # discover a new node
            open_set.add(neighbor)
            new_path = path + [neighbor]
            g_score[neighbor] = g_score[curr] + grid[neighbor[0]][neighbor[1]]
            f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, length)
            heapq.heappush(frontier_queue, (f_score[neighbor], new_path))

    return best_answer


print(main())


# SOLUTION : 425185
