import math

def generate_triangular_nums(num):
    arr = []
    for i in range(1, num+1):
        curr = i*(i-1)/2
        arr.append(curr)

    return arr


def generate_pentagonal_nums(num):
    arr = []
    for i in range(1, num+1):
        curr = i*(3*i-1)/2
        arr.append(curr)

    return arr


def generate_hexagonal_nums(num):
    arr = []
    for i in range(1, num+1):
        curr = i*(2*i-1)
        arr.append(curr)

    return arr


if __name__ == '__main__':
    upper_bound = 10000
    array = generate_triangular_nums(upper_bound)
    print (array[284], array[285], array[286])
    array = array[287:]
    print ("done with triags")
    pents = generate_triangular_nums(upper_bound)
    print ("done with pents")
    hexes = generate_triangular_nums(upper_bound)
    print ("done with hexes")

    print (array)

    for j in array:
        if j in pents and j in hexes:
            print ("hype", j)
            break


# SOLVED : 5482660
