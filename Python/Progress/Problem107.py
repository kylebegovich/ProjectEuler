# High level plan: Kruskall


def text_to_matrix(file_name):
    f = open(file_name, 'r')
    to_ret = []
    app = to_ret.append
    for line in f:
        arr = line[:-1].split(",")
        app([int(c) if c != "-" else -1 for c in arr])
    f.close()
    return to_ret


def count_edges(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] != -1:
                count += 1

    return count


def is_neighbor(index1, set2):
    pass


def main():
    text_file = "p107_network.txt"
    matrix = text_to_matrix(text_file)
    # for line in matrix:
    #     print(line)

    edges = count_edges(matrix)
    print(edges)


main()
