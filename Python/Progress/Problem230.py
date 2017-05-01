import math

a = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
b = 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196
fab = {1: str(a), 2: str(b)}


def fibonacci_words(n, index):
    if index in fab:
        if n > len(fab[index]):
            return fibonacci_words(n, index+1)
        else:
            print(fab[index][n-1])
            return int(fab[index][n-1])
    else:
        temp = len(fab) + 1
        # concatenation
        fab[temp] = fab[temp-2] + fab[temp-1]
        return fibonacci_words(n, index)


if __name__ == '__main__':
    summation = 0

    print(math.floor(math.log10(1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679))+1)
    int(math.floor(math.log10(a)) + 1)

    for i in range(0, 18):
        summation += 10**i * fibonacci_words((127+(19*i))*(7**i), len(fab))
        print(summation)

    print(summation)
