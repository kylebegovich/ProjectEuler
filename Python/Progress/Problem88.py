import math
product_sum_nums = []


def product(lst):
    result = 1
    for num in lst:
        result *= num

    return result


def find_min_p_s_num(k):
    sum_nums = []
    product_nums = []
    for i in range(k):
        sum_nums.append(1)
        product_nums.append(1)

    while True:
        temp = product(product_nums)
        if sum(sum_nums) == temp:
            return temp
        else:
            do = 1  # no-op
            # increment


if __name__ == '__main__':
    print("answer")
