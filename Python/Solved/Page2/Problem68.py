# briefly, I'm going to humor doing this by hand
"""
Because we're looking for a solution with only 16 digits, we use the '10' exactly once, and thus it must be on the outside

We're looking for the maximum value of the concatenation, so we'll start trying to use the largest number on the outside
    9, 8, 7, 6, 10 (10 is forced, not maximum, as it's concatenation not another mathematical operation)

We have to work clockwise, and the numbers on the outside must be = total - (sum inner two).

A way (not necessarily maximal) to solve for this would be to step the outside upwards and step the inside downwards

    6   7   8   9   10
    |   |   |   |   |
    5   4   3   2   1
  / | / | / | / | / | /
    4   3   2   1   5

However, we see that the numbers don't get balanced so quickly, as the difference is not maintained in 5 that was evident in 3

After playing with this a little more, the total sum of the ring is 6+7+8+9+10 + 2*(1+2+3+4+5) = 70, so each line
    needs to be 70/5 = 14 total, which means we can make the rings better (correctly), starting with the minimal:
    let x be a unknown outer ring element, and y be an inner ring unknown, the only sum to 14 with 6 and y's is 6,5,3

    6   x   x   x   x
    |   |   |   |   |
    5   3   y   y   y
  / | / | / | / | / | /
    3   y   y   y   5

    now, sums to 14 with 3 and without 5 are 9,3,2; and 10,3,2

    6   9   x   x   x
    |   |   |   |   |
    5   3   2   y   y
  / | / | / | / | / | /
    3   2   y   y   5

    6   10  x   x   x
    |   |   |   |   |
    5   3   1   y   y
  / | / | / | / | / | /
    3   1   y   y   5

    continuing, the first has 8,2,4 as the next option. the second has 9,1,4

    6   9   8   x   x
    |   |   |   |   |
    5   3   2   4   y
  / | / | / | / | / | /
    3   2   4   y   5

    6   10  9   x   x
    |   |   |   |   |
    5   3   1   4   y
  / | / | / | / | / | /
    3   1   4   y   5

    continuing, the first has 9,4,1 as the next option. the second has 8,4,2

    6   9   8   9   x
    |   |   |   |   |
    5   3   2   4   1
  / | / | / | / | / | /
    3   2   4   1   5

    6   10  9   8   x
    |   |   |   |   |
    5   3   1   4   2
  / | / | / | / | / | /
    3   1   4   2   5

    continuing, the first has no valid options left, so it's not a valid arrangement. the second works, as it's last value is 7

    6   10  9   8   7
    |   |   |   |   |
    5   3   1   4   2
  / | / | / | / | / | /
    3   1   4   2   5

    working clockwise, the value is 6,5,3; 10,3,1; 9,1,4; 8,4,2; 7,2,5 = 6531031914842725, which is the answer

    I believe that this is a little lucky that I found the answer so quickly, but would suppose coding an
        intuitive solution would take longer; the brute force one though, follows:
"""


from itertools import permutations


# working in a space s.t. list[0:(n/2)-1] is the outer ring, in order, and list[n/2:n-1] is the inner ring
def generate_n_gons(n):
    if n < 3:
        return None

    return list(permutations(range(2*n, 0, -1)))


def is_magic(test_tuple):
    if test_tuple is None:
        return False

    return True  # would be an actual expression if we cared


def main(gon):
    magic_list = []
    app = magic_list.append
    for elem in generate_n_gons(gon):  # not sure why this is mad at me... oh well
        if is_magic(elem):
            print("is magic")
            app(elem)

    return sorted(magic_list)


print(main(3))  # would be 5 for our actual problem
print()
print("6531031914842725")


# SOLVED : 6531031914842725
