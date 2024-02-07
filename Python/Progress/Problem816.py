from itertools import combinations
from Euler import euclidean_dist_sq
from math import sqrt

START = 290797
MOD = 50515093

def step(n):
    return (n ** 2) % MOD

def d(points):
    combos = combinations(points, 2)
    min_distance = None
    for c in combos:
        dist = euclidean_dist_sq(c[0][0], c[1][0], c[0][1], c[1][1])
        if min_distance is None or dist < min_distance:
            print("new min distance!")
            print(c)
            min_distance = dist

    return sqrt(min_distance)

def main(iters):
    curr = START
    s_nums = [START]
    print("step {}, curr= {}".format(0, curr))
    for i in range(iters*2):
        next = step(curr)
        s_nums.append(next)
        curr = next
        print("step {}, curr= {}".format(i, curr))

    print()
    print("s_nums", s_nums)
    print()

    points = []
    for i in range(iters):
        n = 2*i
        points.append((s_nums[n], s_nums[n+1]))

    print()
    print("points", points)
    print()

    print(d(points))
    
main(14)