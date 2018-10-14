from Euler import binomial


total_choices = binomial(70, 20)
print(total_choices)

def funct1():
    sum = 0
    for i in range(6):
        print()
        num_colors = 7 - i
        print(num_colors)
        color_choices = 10 ** num_colors
        print(color_choices)
        n = 63+i-(10*i)
        r = 20 - num_colors
        extra_choices = binomial(n, r)
        print(extra_choices, n, r)

        print(color_choices * extra_choices)

        print(num_colors * color_choices * extra_choices)
        sum += num_colors * color_choices * extra_choices
    return sum

def funct2():
    map = {}
    for i in range(5, -1, -1):
        print()
        num_colors = 7 - i
        print(num_colors)
        # ways_to_pick_colors = 10 ** num_colors
        # print(ways_to_pick_colors)

        n = 70 - (10 * i)
        r = 20
        extra_choices = binomial(n, r)
        print(extra_choices, n, r)

        # print(num_colors * extra_choices)

        mini_sum = 0
        for j in range(i, 5):
            print(binomial(num_colors, j+1))
            extra_choices -= (map[j+1] * binomial(num_colors, j+1))

        print(extra_choices)
        map[i] = extra_choices

    sum = 0
    for key in map.keys():
        sum += key * map[key]

    return sum

# print()
ways = funct2()
print(ways)
print(total_choices)
print(ways / total_choices)
