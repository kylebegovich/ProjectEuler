n = 1
a = 3
b = 5
summation = 0
maximum = 1000

if __name__ == '__main__':
    while n < 1000:
        if (n % 3 == 0 or n % 5 == 0):
            summation += n
        n += 1

    print(summation)


# SOLVED : 233168
