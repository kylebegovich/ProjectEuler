from itertools import permutations
from math import floor, ceil


add = lambda a, b: int(a + b)

sub = lambda a, b: int(a - b)

mul = lambda a, b: int(a * b)

div = lambda a, b: a / b if b != 0 else 0


ops = [add, sub, mul, div]


def calc(inpt):
    # a full combo is a 2-tuple containing the numbers in the order they should be calculated and the operations
    # ...sorry that these look disgusting, the paren setup is as follows:
    """
     0:  a ~ b ~ c ~ d     ((a~b)~c)~d
     1:  a ~ b ~(c ~ d)    (c~d)!a~b
     2:  a ~(b ~ c)~ d     ((b~c)!a)~d
     3:  a ~(b ~ c ~ d)    ((b~c)~d)!a
     4: (a ~ b)~(c ~ d)    (a~b)~(c~d)
    """

    i = inpt[0]
    paren_setup = inpt[1]

    num = -1

    if paren_setup == 0:
        num = i[1][2](i[1][1](i[1][0](i[0][0], i[0][1]), i[0][2]), i[0][3])
    elif paren_setup == 1:
        num = i[1][1](i[1][0](i[0][0], i[0][1]), i[1][2](i[0][2], i[0][3]))  # I think this is the same as 4...
    elif paren_setup == 2:
        num = i[1][2](i[1][0](i[0][0], i[1][1](i[0][1], i[0][2])), i[0][3])
    elif paren_setup == 3:
        num = i[1][0](i[0][0], i[1][2](i[1][1](i[0][1], i[0][2]), i[0][3]))
    elif paren_setup == 4:
        num = i[1][1](i[1][0](i[0][0], i[0][1]), i[1][2](i[0][2], i[0][3]))

    if ceil(num) == floor(num):
        return int(num)

    return -1


def all_ops_and_parens(vals):
    # this should be 4^3 = 64  * 5 = 320, as we select any combination of operators to calculate the total, and pick a paren_setup
    l = (5 * (4 ** 3))
    out_list = []
    app = out_list.append

    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(5):
                    o = (ops[i], ops[j], ops[k])
                    app(((vals, o), l))

    print(out_list)
    return out_list


def all_vals():
    # this should be 9 choose 4 for which values, and 4! ways to arrange them, for a total of 9!/5! = 3024 values
    return list(permutations(range(1, 10), 4))  # easier than I expected thx to itertools


def max_chain(targets):

    targets = sorted(targets)

    if targets is None or len(targets) == 0:
        return -1

    longest = 0
    curr = 0
    prev = targets[0]
    for elem in targets:
        #print(longest, curr, prev, elem)
        if elem == (prev + 1):
            curr += 1
        elif curr > longest:
            longest = curr
            curr = 0

        prev = elem

    return max([longest, curr])


def main():
    best = 28
    for tupe in all_vals():
        targets = [calc(op_combo) for op_combo in all_ops_and_parens(tupe)]
        temp = max_chain(targets)
        print(temp, tupe)
        if temp > best:
            print("New Best: ", targets)
            best = temp

    return best


"""
test = list(range(4, 24))
test.append(1)
for i in range(28, 58):
    test.append(i)
print(sorted(test))
print(max_chain(test))
"""


"""
 a ~ b ~ c ~ d     : 0
 a ~ b ~(c ~ d)    : 1
 a ~(b ~ c)~ d     : 2
 a ~(b ~ c ~ d)    : 3
(a ~ b)~(c ~ d)    : 4
"""


print(main())
