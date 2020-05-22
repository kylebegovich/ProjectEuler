from Euler import prime_factor

MAX = 100000
temp = 10

found = []


for n in range(1, MAX + 1):
    factors = prime_factor(n)
    rad = 1
    for pair in factors:
        rad *= pair[0]

    found.append((rad, n))

    print(n, rad)


sorted_found = sorted(found)
[print(f) for f in sorted_found]
print(sorted_found[10001])


# SOLVED: 21417
