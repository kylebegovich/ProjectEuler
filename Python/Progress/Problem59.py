# the encryption key consists of three lower case characters
# the plain text must contain common English words

from Euler import *
import itertools
import operator


first_arr = []
second_arr = []
third_arr = []


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


def test_suite(to_check):
    key_min = 97
    key_max = 122

    output = to_check

    for i in range(len(output)):
        output[i] = (output[i]^key_min, output[i] ^ key_max)

    return output


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


if __name__ == '__main__':
    message = open("p059_cipher.txt", 'r')

    text = ""
    for line in message:
        text = line[:-1].split(", ")

    text = strings_to_ints(text)

    # operations on the text
    split_into_three(text)
    print(first_arr)
    print(second_arr)
    print(third_arr)

    print(most_common([1, 2, 2, 2, 3, 4, 1]))
    print(most_common(first_arr), max(first_arr), min(first_arr))
    print(most_common(second_arr), max(second_arr), min(second_arr))
    print(most_common(third_arr), max(third_arr), min(third_arr))

    message.close()
