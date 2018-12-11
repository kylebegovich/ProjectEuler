import itertools, Euler, math

def shuffle(deck):
    l = len(deck) // 2
    shuffled = []
    app = shuffled.append
    for i in range(l):
        app(deck[i])
        app(deck[i+l])

    return shuffled


def s(n):
    deck = [i for i in range(1, n+1)]
    curr = shuffle(deck)
    count = 1

    while curr != deck:
        # print(curr)
        count += 1
        curr = shuffle(curr)

    return count


def all_X_in_Y():
    for i in range(2, 30, 2):
        print(s(i))
        print()

# print(s(14))
# print(s(86))

def solve():
    n = 2
    summation = 0
    while True:
        s_val = s(n)
        print(n, s_val, n//2, math.log(n, 2))
        if s_val == 60:
            summation += n
            # print(summation, n)
        if n % 1000 == 0:
            print(n)
        n += 2


def pows_of_2():
    n = 4
    # summation = 0
    while True:
        print(n, s(n))
        print(n+2, s(n+2))
        print(n-2, s(n-2))
        print()
        n *= 2
        if n > 100:
            break


solve()
# pows_of_2()
