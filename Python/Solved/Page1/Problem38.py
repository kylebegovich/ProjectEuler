import math

lower_bound = 123456789
upper_bound = 987654321


def is_pandigital(n):
    if n < lower_bound or n > upper_bound:
        return False
    else:
        to_cover = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(1, 10):
            curr = n % 10
            print(curr, n)
            if curr in to_cover:
                to_cover.remove(curr)
                n /= 10
            else:
                return False

    return True


def foo(arr):
    str_temp = ""
    for i in arr:
        str_temp += str(i)
    print ("i did a foo " + str_temp)
    return len(str_temp)


def get_first_digit(num):
    digits = len(str(num))
    return num / (10**(digits-1))


def increment(n):
    num = n
    print ("im gonna get bigger! " + str(num))
    if str(num+1)[0] != 9:
        num += 1
        while get_first_digit(num) != 9:
            num += 1
        return num
    else:
        return num+1


if __name__ == '__main__':
    n = 1
    d = 9
    arr = []

    #provided example that satisfies conditions
    maximum = 918273645

    while d < 10000:
        while foo(arr) < 9:
            arr.append(n*d)
            n += 1
        if foo(arr) == 9:
            str_temp = ""
            for i in arr:
                str_temp += str(i)
            curr = int(str_temp)
            if is_pandigital(curr):
                print(maximum, curr)
                if curr > maximum:
                    maximum = curr
                    print("NEW MAX!!!")
        d = increment(d)
        n = 1
        arr = []

    print (maximum)
