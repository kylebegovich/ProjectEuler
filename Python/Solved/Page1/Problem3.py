import math

a = 600851475143
b = 3

if __name__ == '__main__':
    while a > math.pow(b, 2):
        if a % b == 0:
            a = a / b
            print (a)
            print (b)
        else:
            b += 2
            print (b)
    print(a)


# SOLVED : 6857
