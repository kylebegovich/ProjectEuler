import math

if __name__ == '__main__':
    summation = 0
    for i in range(1, 1001):
        summation += i**i

    print(summation % 10000000000)


# SOLVED : 9110846700
