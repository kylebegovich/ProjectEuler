in_nums = 100


def square_sum(num):
    return sum(range(num+1))**2


def sum_squares(num):
    return sum([n**2 for n in range(num+1)])


def main(nums):
    first = sum_squares(nums)
    second = square_sum(nums)
    return abs(first - second)


print(main(in_nums))


# SOLVED : 25164150
