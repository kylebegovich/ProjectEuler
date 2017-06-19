product_sum_nums = []


def product(lst):
    result = 1
    for num in lst:
        result *= num

    return result


def increment(lst):
    l = len(lst)
    for k in range(l-1, -1, -1):
        if not lst[k] == 9:
            lst[k] += 1
            return lst


def find_min_p_s_num(k):
    curr_nums = []
    for j in range(k):
        curr_nums.append(1)

    while True:
        temp = 1
        if curr_nums is None:
            return 0
        temp = product(curr_nums)
        if sum(curr_nums) == temp:
            return temp
        else:
            curr_nums = increment(curr_nums)


if __name__ == '__main__':

    for i in range(2, 10):
        print(find_min_p_s_num(i))
