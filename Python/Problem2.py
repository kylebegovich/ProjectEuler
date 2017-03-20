a = 1
b = 2
c = 0
summation = 2
maximum = 4000000

if __name__ == '__main__':
    while True:
        c = a + b
        a = b + c
        b = c + a
        if b < maximum:
            summation += b
        else:
            break

    print summation


# SOLVED : 4613732