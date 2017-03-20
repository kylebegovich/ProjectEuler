def square_sum(num):
    i = 1
    sum = 0
    while i <= num:
        sum += i
        i += 1
    return sum*sum

def sum_square(num):
    i = 1
    sum = 0
    while i <= num:
        sum += i*i
        i += 1
    return sum

if __name__ == '__main__':
    first = sum_square(100)
    second = square_sum(100)
    print abs(first - second)


# SOLVED : 25164150