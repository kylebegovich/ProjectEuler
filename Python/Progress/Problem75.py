from Euler import factors
from math import ceil

L = 1500000
maximum = 339812


discovered = set()
duplicates = set()


max_perim = lambda r: int(3*r + 2*((r**2)/2) + 2)
min_perim = lambda r: int(ceil(3*r + 2*r/(2**0.5)))


def perim(r, s, t):
    return 3*r + 2*s + 2*t


def main():
    discapp = discovered.add
    dupeapp = duplicates.add
    discrem = discovered.remove
    for r in range(2, maximum, 2):   # needs r to be even for Dickson's formula to work
        for tupe in factors((r**2)/2):
            temp = perim(r, tupe[0], tupe[1])
            if temp > L:
                continue
            if temp not in duplicates and temp not in discovered:
                discapp(temp)
            elif temp not in duplicates and temp in discovered:
                dupeapp(temp)
                discrem(temp)

        print("working:", r)


def find_maximum():

    for i in range(2, 1000000000000, 2):
        if min_perim(i) > L:
            print(i, min_perim(i))
            break


# find_maximum()  # found: 339812

main()
print(discovered, len(discovered))
