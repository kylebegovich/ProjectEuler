import math


def list_to_int(my_list):
    my_list = my_list[::-1]
    length = len(my_list)
    out = 0
    for i in range(length):
        out += (my_list[i])* 10**i

    return out


def is_lychrel(num, iters):
    if iters > 50:
        return True
    else:
        lst = list(str(num))
        backward = lst[::-1]
        if lst == backward and iters != 0:
            print (num)
            return False
        else:
            print("not yet", num, iters)

            temp = map(int, lst)
            temp2 = map(int, backward)
            num = list_to_int(temp) + list_to_int(temp2)
            return is_lychrel(num, iters+1)


if __name__ == '__main__':

    upper_bound = 10000
    counter = 0
    for i in range(1, upper_bound):
        if is_lychrel(i, 0):
            counter += 1
        else:
            print(i, "is Lychrel")

    print(counter)


# SOLVED : 249
