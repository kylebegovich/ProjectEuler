import math


triangle = []


def bottom_up_step(row):

    # iterate over all but the last element in the current row
    for index in range(row):
        if triangle[row][index] > triangle[row][index+1]:
            triangle[row-1][index] += triangle[row][index]
        else:
            triangle[row-1][index] += triangle[row][index+1]
        triangle[row][index] = 0



if __name__ == '__main__':

    # read the data from the file, put it into triangle
    text = open("text_files/p067_triangle.txt", 'r')

    i = 0
    for line in text:
        fixed = [int(numeric_string) for numeric_string in line.split(' ')]
        triangle.append(fixed)
        i += 1

    text.close()
    print("Done transferring file, there are %i rows" % i)

    # actually start doing stuff
    for row in range(99, 0, -1):
        bottom_up_step(row)
        print(triangle[row])

    print(triangle[0][0])


# SOLVED : 7273
