# HUGE shoutout to https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
# basically, I'm coding that algorithm

from math import floor, ceil, sqrt


def generate_squares(lim):

    out = []
    app = out.append
    for i in range(int(ceil(sqrt(lim)))):
        app(i**2)

    return set(out)


def get_seq_len(m, d, a0, S):
    a = a0
    count = 0
    while a != 2*a0:
        m = (d*a) - m
        d = (S - (m**2)) // d
        a = int(floor(((a0 + m) / d)))
        count += 1

    return count


def main(max_val):

    odd_cycles = 0
    squares = generate_squares(max_val)

    for S in range(2, max_val):
        if S in squares:
            continue
        if get_seq_len(0, 1, int(floor(sqrt(S))), S) % 2 == 1:
            odd_cycles += 1

    return odd_cycles


print(main(10000))


# SOLVED : 1322
