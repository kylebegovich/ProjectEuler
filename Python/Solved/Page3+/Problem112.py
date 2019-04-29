

def is_decreasing(list_num):
    if len(list_num) == 0 or len(list_num) == 1:
        return True

    if list_num[0] >= list_num[1]:
        return is_decreasing(list_num[1:])


def is_increasing(list_num):
    if len(list_num) == 0 or len(list_num) == 1:
        return True

    if list_num[0] <= list_num[1]:
        return is_increasing(list_num[1:])


def is_bouncy(list_num):
    if not is_increasing(list_num) and not is_decreasing(list_num):
        return True
    return False


def test_vals():
    print(123, is_bouncy([1, 2, 3]))
    print(121, is_bouncy([1, 2, 1]))
    print(123456789, is_bouncy([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(1234567899999, is_bouncy([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9]))
    print(12345678994, is_bouncy([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 4]))


def inc_num(num):
    if num == []:
        return [1]

    if num[-1] != 9:
        num[-1] += 1
        return num

    return inc_num(num[:-1]) + [0]


def test_inc_num():
    print([], inc_num([]))
    print([9], inc_num([9]))
    print([1,2,3], inc_num([1,2,3]))
    print([1,2,9], inc_num([1,2,9]))


def num_proportion_above(bound):
    if bound < 0 or bound >= 1:
        return -1

    bouncy_count = 0
    total_count = 0
    num = [0]
    proportion = 0

    while proportion < bound:
        if is_bouncy(num):
            bouncy_count += 1
            proportion = bouncy_count / total_count
        total_count += 1
        num = inc_num(num)

    return total_count-1


print(num_proportion_above(0.99))


# SOLVED : 1587000
