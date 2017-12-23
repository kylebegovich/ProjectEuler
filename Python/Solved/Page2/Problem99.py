import math


def get_num_size(base, pow):
    return base ** pow


if __name__ == '__main__':
    pair_file = open("text_files/p099_base_exp.txt", 'r').read().split('\n')

    print(len(pair_file), pair_file[577], pair_file[708])

    maximum = (0, 0)
    for i in range(len(pair_file)):

        line = pair_file[i]
        comma = line.find(',')
        base = math.log(float(line[:comma]))
        power = int(line[comma+1:])
        value = base * power
        # print(base, power, value, i)
        if value > maximum[0]:
            maximum = (value, i+1)

    print(maximum)


# SOLVED : 709
