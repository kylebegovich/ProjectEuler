from Euler import gcd


def next_numerator(prev_numerator, prev_denominator):
    return prev_numerator + (2*prev_denominator)


def next_denominator(next_numerator, prev_denominator):
    """Yes, the numerator is purposefully next, not curr"""
    return next_numerator - prev_denominator


if __name__ == '__main__':

    curr_numerator = 3
    curr_denominator = 2
    count = 0

    for i in range(1000):
        if len(str(curr_numerator)) > len(str(curr_denominator)):
            count += 1

        curr_numerator = next_numerator(curr_numerator, curr_denominator)
        curr_denominator = next_denominator(curr_numerator, curr_denominator)

    print(count)


# SOLVED : 153
