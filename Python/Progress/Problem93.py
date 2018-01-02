from itertools import permutations


add = lambda a, b: a + b

sub = lambda a, b: a - b

mul = lambda a, b: a * b

div = lambda a, b: a / b


ops = [add, sub, mul, div]


def all_ops(vals_and_parens):
    # this should be 4^3, as we select any combination of operators to calculate the total
    return []


def all_paren_combinations(vals):
    # this should be only 5 ways to place parens around 4 operations that would be done in order otherwise
    return []


def all_vals():
    # this should be 9 choose 4 for which values, and 4! ways to arrange them, for a total of 9!/5! = 3024 iterations
    return []


def max_chain(targets):
    return 0


def main():
    best = 28
    for targets in all_vals():
        temp = max_chain(targets)
        if temp > best:
            print(targets)
            best = temp

    return best


print(main())