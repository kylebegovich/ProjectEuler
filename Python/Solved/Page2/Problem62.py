from collections import defaultdict


def cube(x): return x**3


def main():
    cubes = defaultdict(list)
    for i in range(10000):
        c = cube(i)
        digits = ''.join(sorted([d for d in str(c)]))
        cubes[digits].append(c)

    print(min([min(v) for k, v in list(cubes.items()) if len(v) == 5]))

main()

# SOLVED : 127035954683






# old code:

"""
from itertools import permutations


tested_up_to = 600
arbitrary_max_cubes = 100000
arbitrary_min_answer = 10000000000
arbitrary_max_answer = 100000000000000

cubes = [n ** 3 for n in range(tested_up_to, arbitrary_max_cubes)]

print(cubes)
print()
print()


for curr in cubes:
    count = 0  # would be 1, as curr is a cube, but it is included in the arr of permuatations
    counted_arr = []
    for perm in [int(''.join(x)) for x in permutations(str(curr))]:
        if perm in cubes and perm not in counted_arr:
            count += 1
            counted_arr.append(perm)

    print(curr, count)
    if count == 5:
        print(curr)
        break

# should work... but quite slow... sad reax onlee
"""
