import math


in_num_digits = 3


is_palindrome = lambda num: str(num) == str(num)[::-1]


def main(num_digits):
    max_val = 10**num_digits - 1
    min_val = 10**(num_digits - 1)
    a = b = max_val
    curr_max = 0
    while a >= min_val:
        while b >= min_val:
            if a*b > curr_max and is_palindrome(a * b):
                curr_max = a*b
            b -= 1
        a -= 1
        b = max_val

    return curr_max


print(main(in_num_digits))


# SOLVED : 906609
