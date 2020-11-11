from math import ceil, sqrt

N = 600851475143

def main(N):
    largest = 1
    for i in range(2, ceil(sqrt(N))):
        while N % i == 0:
            largest = i
            N /= i
    return largest

print(main(N))


# SOLVED : 6857
