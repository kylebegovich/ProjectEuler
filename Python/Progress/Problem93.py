from itertools import permutations
from math import floor, ceil


def add(a, b):
    if a is None or b is None:
        return None
    return a + b


def sub(a, b):
    if a is None or b is None:
        return None
    return a - b


def mul(a, b):
    if a is None or b is None:
        return None
    return a * b


def div(a, b):
    if a is None or b is None or b == 0:
        return None
    return a / b


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


def bruteforce(a, b, c, d):
    values = set()
    app = values.add

    for p in list(permutations([a, b, c, d])):
        for op1 in operators:
            for op2 in operators:
                for op3 in operators:
                    v = op1(op2(op3(p[0], p[1]), p[2]), p[3])  # ((a 3 b) 2 c) 1 d
                    if v is not None and v > 0 and v not in values and ((type(v) == float and v.is_integer()) or type(v) != float):
                        if op1 == add:
                            o1 = "+"
                        if op2 == add:
                            o2 = "+"
                        if op3 == add:
                            o3 = "+"
                        if op1 == sub:
                            o1 = "-"
                        if op2 == sub:
                            o2 = "-"
                        if op3 == sub:
                            o3 = "-"
                        if op1 == mul:
                            o1 = "*"
                        if op2 == mul:
                            o2 = "*"
                        if op3 == mul:
                            o3 = "*"
                        if op1 == div:
                            o1 = "/"
                        if op2 == div:
                            o2 = "/"
                        if op3 == div:
                            o3 = "/"
                        # print("1:  ", v, " = ((", p[0], o3, p[1], ")", o2, p[2], ")", o1, p[3])
                        app(v)

                    v = op1(op2(p[0], op3(p[1], p[2])), p[3])  # (a 2 (b 3 c)) 1 d
                    if v is not None and v > 0 and v not in values and ((type(v) == float and v.is_integer()) or type(v) != float):
                        if op1 == add:
                            o1 = "+"
                        if op2 == add:
                            o2 = "+"
                        if op3 == add:
                            o3 = "+"
                        if op1 == sub:
                            o1 = "-"
                        if op2 == sub:
                            o2 = "-"
                        if op3 == sub:
                            o3 = "-"
                        if op1 == mul:
                            o1 = "*"
                        if op2 == mul:
                            o2 = "*"
                        if op3 == mul:
                            o3 = "*"
                        if op1 == div:
                            o1 = "/"
                        if op2 == div:
                            o2 = "/"
                        if op3 == div:
                            o3 = "/"
                        # print("2:  ", v, " = (", p[0], o2, "(", p[1], o3, p[2], "))", o1, p[3])
                        app(v)

                    v = op1(p[0], op2(op3(p[1], p[2]), p[3]))  # a 1 ((b 3 c) 2 d)
                    if v is not None and v > 0 and v not in values and ((type(v) == float and v.is_integer()) or type(v) != float):
                        if op1 == add:
                            o1 = "+"
                        if op2 == add:
                            o2 = "+"
                        if op3 == add:
                            o3 = "+"
                        if op1 == sub:
                            o1 = "-"
                        if op2 == sub:
                            o2 = "-"
                        if op3 == sub:
                            o3 = "-"
                        if op1 == mul:
                            o1 = "*"
                        if op2 == mul:
                            o2 = "*"
                        if op3 == mul:
                            o3 = "*"
                        if op1 == div:
                            o1 = "/"
                        if op2 == div:
                            o2 = "/"
                        if op3 == div:
                            o3 = "/"
                        # print("3:  ", v, " = ", p[0], o1, "((", p[1], o3, p[2], ")", o2, p[3], ")")
                        app(v)

                    v = op1(p[0], op2(p[1], op3(p[2], p[3])))  # a 1 (b 2 (c 3 d))
                    if v is not None and v > 0 and v not in values and ((type(v) == float and v.is_integer()) or type(v) != float):
                        if op1 == add:
                            o1 = "+"
                        if op2 == add:
                            o2 = "+"
                        if op3 == add:
                            o3 = "+"
                        if op1 == sub:
                            o1 = "-"
                        if op2 == sub:
                            o2 = "-"
                        if op3 == sub:
                            o3 = "-"
                        if op1 == mul:
                            o1 = "*"
                        if op2 == mul:
                            o2 = "*"
                        if op3 == mul:
                            o3 = "*"
                        if op1 == div:
                            o1 = "/"
                        if op2 == div:
                            o2 = "/"
                        if op3 == div:
                            o3 = "/"
                        # print("4:  ", v, " = ", p[0], o1, "(", p[1], o2, "(", p[2], o3, p[3], "))")
                        app(v)

                    v = op1(op2(p[0], p[1]), op3(p[2], p[3]))  # (a 2 b) 1 (c 3 d)
                    if v is not None and v > 0 and v not in values and ((type(v) == float and v.is_integer()) or type(v) != float):
                        if op1 == add:
                            o1 = "+"
                        if op2 == add:
                            o2 = "+"
                        if op3 == add:
                            o3 = "+"
                        if op1 == sub:
                            o1 = "-"
                        if op2 == sub:
                            o2 = "-"
                        if op3 == sub:
                            o3 = "-"
                        if op1 == mul:
                            o1 = "*"
                        if op2 == mul:
                            o2 = "*"
                        if op3 == mul:
                            o3 = "*"
                        if op1 == div:
                            o1 = "/"
                        if op2 == div:
                            o2 = "/"
                        if op3 == div:
                            o3 = "/"
                        # print("5:  ", v, " = (", p[0], o2, p[1], ") ", o1, " (", p[2], o3, p[3], ")")
                        app(v)

    return values


def main():

    max_val = 0
    max_list = [1, 2, 3, 4]

    for a in range(1, 10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):

                    values = bruteforce(a, b, c, d)

                    streak = longest_streak(sorted(list(values)))
                    # print(sorted(list(values)))
                    if streak > max_val:
                        max_val = streak
                        max_list = [a, b, c, d]
                        print("MAX")
                        print(max_val, max_list)
                        print(sorted(list(values)))

    return max_list


print(main())
#print(bruteforce(1, 2, 5, 6))
#print(bruteforce(1, 2, 5, 8))

#print(div(1, 2))
#print(add(div(1, 2), 5))
#print(mul(add(div(1, 2), 5), 8))
