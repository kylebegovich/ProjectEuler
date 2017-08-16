from itertools import permutations


tested_up_to = 500
arbitrary_max_cubes = 1000
arbitrary_min_answer = 100000
arbitrary_max_answer = 1000000000

cubes = [n ** 3 for n in range(tested_up_to, arbitrary_max_cubes)]

print(cubes)


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
