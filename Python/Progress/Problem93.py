from itertools import permutations
from math import floor, ceil


def add(a, b):
    if a is None or b is None:
        return None
    return int(a + b)


def sub(a, b):
    if a is None or b is None:
        return None
    return int(a - b)


def mul(a, b):
    if a is None or b is None:
        return None
    return int(a * b)


def div(a, b):
    if a is None or b is None or b == 0 or a % b != 0:
        return None
    return a // b


operators = [add, sub, mul, div]


def longest_streak(values):
    streak = 0
    last = 0
    for v in values:
        if v == last + 1:
            streak += 1
            last = v
        else:
            return streak

    return streak


def bruteforce():

    max_val = 0
    max_list = [1, 2, 3, 4]

    for a in range(1, 10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):

                    values = set()
                    app = values.add

                    for p in list(permutations([a, b, c, d])):
                        # print(p)
                        for op1 in operators:
                            for op2 in operators:
                                for op3 in operators:
                                    v = op3(op2(op1(p[0], p[1]), p[2]), p[3])
                                    if v is not None and v > 0:
                                        app(v)

                                    v = op3(op1(p[0], op2(p[1], p[2])), p[3])
                                    if v is not None and v > 0:
                                        app(v)

                                    v = op1(p[0], op3(op2(p[1], p[2]), p[3]))
                                    if v is not None and v > 0:
                                        app(v)

                                    v = op1(p[0], op2(p[1], op3(p[2], p[3])))
                                    if v is not None and v > 0:
                                        app(v)

                                    v = op2(op1(p[0], p[1]), op3(p[2], p[3]))
                                    if v is not None and v > 0:
                                        app(v)

                    streak = longest_streak(sorted(list(values)))
                    # print(sorted(list(values)))
                    if streak > max_val:
                        max_val = streak
                        max_list = [a, b, c, d]
                        print("MAX")
                        print(max_val, max_list)
                        print(sorted(list(values)))

    return max_list


print(bruteforce())
