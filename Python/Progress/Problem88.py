import math
product_sum_nums = []


def product(lst):
    result = 1
    for num in lst:
        result *= num

    return result


def increment(lst):
    l = len(lst)
    for i in range(l-1, -1, -1):
        if not lst[i] == 9:
            lst[i] += 1
            return lst


def find_min_p_s_num(k):
    curr_nums = []
    for i in range(k):
        curr_nums.append(1)

    while True:
        temp = product(curr_nums)
        if sum(curr_nums) == temp:
            return temp
        else:
            curr_nums = increment(curr_nums)


if __name__ == '__main__':
    print([0, 1, 2], product([0, 1, 2]))
    print([3, 1, 2], product([3, 1, 2]))
    print([7, 5, 2], product([7, 5, 2]))

    print()

    for i in range(10):
        print(find_min_p_s_num(i))
