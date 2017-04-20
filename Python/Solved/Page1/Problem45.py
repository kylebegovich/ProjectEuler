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
    upper_bound = 1000000

    triags = generate_triangular_nums(upper_bound)
    print (triags[284], triags[285], triags[286])
    triags = triags[287:]
    print ("done with triags")
    pents = set(generate_pentagonal_nums(upper_bound))

    print ("done with pents")
    hexes = set(generate_hexagonal_nums(upper_bound))

    print ("done with hexes")

    for j in triags:
        if j in pents and j in hexes:
            print ("solved:", j)
            break


# SOLVED : 1533776805
