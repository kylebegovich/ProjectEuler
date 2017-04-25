import math

max_perim = 1000


def clean_triples():
    triples = [[3, 4, 5], [5, 12, 13], [7, 24, 25], [8, 15, 17], [9, 40, 41], [11, 60, 61], [12, 35, 37], [13, 84, 85],
               [15, 112, 113], [16, 63, 65], [17, 144, 145], [19, 180, 181], [20, 21, 29], [20, 99, 101],
               [21, 220, 221], [23, 264, 265], [24, 143, 145], [25, 312, 313], [27, 364, 365], [28, 45, 53],
               [28, 195, 197], [29, 420, 421], [31, 480, 481], [32, 255, 257], [33, 56, 65], [35, 612, 613],
               [36, 77, 85], [36, 323, 325], [37, 684, 685], [39, 80, 89], [39, 760, 761], [40, 399, 401],
               [41, 840, 841], [43, 924, 925], [44, 117, 125], [44, 483, 485], [48, 55, 73], [51, 140, 149],
               [52, 165, 173], [52, 675, 677], [56, 783, 785], [57, 176, 185], [60, 91, 109], [60, 221, 229],
               [60, 899, 901], [65, 72, 97], [68, 285, 293], [69, 260, 269], [75, 308, 317], [76, 357, 365],
               [84, 187, 205], [84, 437, 445], [85, 132, 157], [87, 416, 425], [88, 105, 137], [93, 476, 485],
               [95, 168, 193], [96, 247, 265], [100, 621, 629], [104, 153, 185], [105, 208, 233], [105, 608, 617],
               [108, 725, 733], [111, 680, 689], [115, 252, 277], [116, 837, 845], [119, 120, 169], [120, 209, 241],
               [120, 391, 409], [123, 836, 845], [124, 957, 965], [129, 920, 929], [132, 475, 493], [133, 156, 205],
               [135, 352, 377], [136, 273, 305], [140, 171, 221], [145, 408, 433], [152, 345, 377], [155, 468, 493],
               [156, 667, 685], [160, 231, 281], [161, 240, 289], [168, 425, 457], [168, 775, 793], [175, 288, 337],
               [180, 299, 349], [189, 340, 389], [203, 396, 445], [204, 253, 325], [207, 224, 305], [216, 713, 745],
               [217, 456, 505], [220, 459, 509], [225, 272, 353], [228, 325, 397], [252, 275, 373], [261, 380, 461],
               [297, 304, 425]]

    for i in triples:

        # get rid of the one's who's perimeter is > 1000
        s = sum(i)
        if s > max_perim:
            triples.remove(i)

        # add any multiples that are less than the max perimeter
        n = 2
        while s*n < max_perim:
            triples.append([i[0]*n, i[1]*n, i[2]*n])
            n += 1

    # prepend the sum of the digits to the front of the triple
    for trip in triples:
        s = sum(trip)
        print (trip, s)
        trip.insert(0, s)

    correct_list = []
    for i in triples:
        if i not in correct_list:
            correct_list.append(i)

    return correct_list


def find_n_for_p(p, triples):
    summation = 0
    for trip in triples:
        if trip[0] == p:
            summation += 1

    print (summation)
    return summation


if __name__ == '__main__':

    triples = clean_triples()

    maximum = 3
    max_p = 120
    for p in range(12, max_perim+1):
        n = find_n_for_p(p, triples)
        if n > maximum:
            maximum = n
            max_p = p
            print (n, p)

    print (maximum, max_p)