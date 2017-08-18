# the encryption key consists of three lower case characters
# the plain text must contain common English words

import itertools
import operator
from math import floor

from Euler import *

first_arr = []
second_arr = []
third_arr = []

# the encryption key consists of three lower case characters, these are ascii 'a' and 'z', respectively
key_min = 97
key_max = 122

def most_common(L):

    # get an iterable of (item, iterable) pairs
    sl = sorted((x, i) for i, x in enumerate(L))

    # print 'SL:', SL
    groups = itertools.groupby(sl, key=operator.itemgetter(0))

    # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)

        # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index

    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]


def split_into_three(arr):
    three_flag = 0
    for elem in arr:
        if three_flag == 0:
            first_arr.append(elem)
            three_flag = 1
        elif three_flag == 1:
            second_arr.append(elem)
            three_flag = 2
        elif three_flag == 2:
            third_arr.append(elem)
            three_flag = 0


def merge_three_arrs():
    output = []
    three_flag = 0
    for i in range(len(first_arr) + len(second_arr) + len(third_arr)):
        if three_flag == 0:
            output.append(first_arr[int(floor(i/3))])
            three_flag = 1
        elif three_flag == 1:
            output.append(second_arr[int(floor(i/3))])
            three_flag = 2
        elif three_flag == 2:
            output.append(third_arr[int(floor(i/3))])
            three_flag = 0

    return output


def test_suite(to_check):

    to_check_max = max(to_check)
    to_check_min = min(to_check)

    output = [sorted(to_check) for i in range(to_check_max-to_check_min)]

    for key in range(key_min, key_max + 1):
        col = key-key_min
        for check in range(len(to_check)):
            output[col][check] ^= key

    return output


def ascii_to_english(num_arr):
    return ''.join(chr(i) for i in num_arr)


def encrypt(string, key):
    encrypted_message = string

    for i in range(len(encrypted_message)):
        encrypted_message[i] ^= key[i % len(key)]

    return encrypted_message


def analysis(most_common_asciis, goal_char):
    to_ret = []

    for char in most_common_asciis:
        for key in range(key_min, key_max+1):
            if char ^ key == goal_char:
                to_ret.append(key)

    return to_ret


if __name__ == '__main__':

    # open that file
    message = open("p059_cipher.txt", 'r')

    text = ""
    for line in message:
        text = line[:-1].split(", ")

    text = strings_to_ints(text)

    # operations on the text
    split_into_three(text)
    most_commons = [most_common(first_arr), most_common(second_arr), most_common(third_arr)]
    print(most_commons)

    # 32 is the ascii value for ' ', which is presumed to be the most common char in the message
    potential_keys = analysis(most_commons, 32)
    print(ascii_to_english(potential_keys))

    answer = encrypt(text, potential_keys)
    print(ascii_to_english(answer), sum(answer))

    # close that file
    message.close()


# SOLVED : 107359
