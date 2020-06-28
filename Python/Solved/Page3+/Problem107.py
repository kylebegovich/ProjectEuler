# High level plan: Kruskal
# ref pseudocode at https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

text_file = "p107_network.txt"

def text_to_matrix(file_name):
    f = open(file_name, 'r')
    to_ret = []
    app = to_ret.append
    for line in f:
        arr = line[:-1].split(",")
        app([int(c) if c != "-" else -1 for c in arr])
    f.close()
    return to_ret


def sort_edges(matrix):
    edge_cost = 0
    sorted_edges = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] != -1:
                sorted_edges.append((matrix[i][j], i, j))
                edge_cost += matrix[i][j]

    return (sorted(sorted_edges), edge_cost)


def set_index(value, sets):
    for i in range(len(sets)):
        if value in sets[i]:
            return i


def main(text_file):
    matrix = text_to_matrix(text_file)
    # for line in matrix:
    #     print(line)

    sets = []
    for i in range(len(matrix)):
        sets.append(set([i]))
    # [print(s) for s in sets]

    sorted_edges, brute_edge_cost = sort_edges(matrix)
    # [print(e) for e in sorted_edges]

    total_edges = 0
    total_edge_cost = 0
    for edge in sorted_edges:
        if total_edges == len(matrix) - 1:
            break

        set_1 = set_index(edge[1], sets)
        set_2 = set_index(edge[2], sets)
        if set_1 == set_2:
            # print("same set!")
            continue

        sets[set_1] = sets[set_1].union(sets[set_2])
        sets.pop(set_2)

        total_edges += 1
        total_edge_cost += edge[0]

        # [print(s) for s in sets]
        # merge sets, add to edge weight count

    print("all_edge_cost =", brute_edge_cost)
    print("optimized_edge_cost =", total_edge_cost)
    print("difference =", brute_edge_cost - total_edge_cost)


main(text_file)


# SOLVED : 259679
