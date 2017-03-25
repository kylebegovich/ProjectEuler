import math
import numpy


def generate_spiral(length):
    spiral = numpy.zeros((length, length))
    print spiral
    row_index = int(math.ceil(length/2))
    col_index = int(math.ceil(length/2))
    step_length = 1
    steps_left = 1
    code = 1  # 1 = right, 2 = down, 3 = left, 4 = up
    curr = 1

    while 0 <= row_index < 1001 and 0 <= col_index < 1001:

        spiral[row_index][col_index] = curr
        curr += 1

        if code == 1:
            col_index += 1
            steps_left -= 1
            if steps_left == 0:
                code += 1
                steps_left = step_length

        elif code == 2:
            row_index -= 1
            steps_left -= 1
            if steps_left == 0:
                code += 1
                step_length += 1
                steps_left = step_length

        elif code == 3:
            col_index -= 1
            steps_left -= 1
            if steps_left == 0:
                code += 1
                steps_left = step_length

        else:
            row_index += 1
            steps_left -= 1
            if steps_left == 0:
                code = 1
                step_length += 1
                steps_left = step_length

    return spiral


if __name__ == '__main__':
    spiral = generate_spiral(1001)
    print spiral

    summation = 0

    for i in xrange(1001):
        summation += spiral[i][i]

    for i in xrange(1001):
        summation += spiral[1000 - i][i]

    summation -= spiral[500][500]

    print summation


# SOLVED : 669171001
