

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
