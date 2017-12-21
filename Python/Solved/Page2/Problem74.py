import math
import time


discovered = {0: 2, 1: 1, 145: 1, 363601: 3, 1454: 3, 169: 3,
              871: 2, 45361: 2, 872: 2, 45362: 2}


def step(curr):
    s = 0
    for digit in list(str(curr)):
        s += math.factorial(int(digit))

    return s


def count(start):

    # basically, we don't care about values that aren't 60 long and already discovered
    if start in discovered:
        return -1

    chain = [start]
    app = chain.append

    while chain[-1] not in discovered:

        app(step(chain[-1]))

        # this is a number that loops into itself, like 1 and 145, more may exist
        if chain[-2] == chain[-1]:
            discovered[chain[-1]] = 1
            break

    # start the inputs into discovered at the last new value, and add all the
    pos = discovered[chain[-1]] + 1
    for i in range(len(chain) -2, -1, -1):
        discovered[chain[i]] = pos
        pos += 1

    return discovered[start]


def main(limit):

    total = 0
    for i in range(0, limit):
        c = count(i)
        if c == 60:
            total += 1
        if c > 60:
            print("something broke :(")

    return total


print(main(1000001))


# SOLVED: 402
