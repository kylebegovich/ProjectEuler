from Euler import binomial

def B(n):
    prod = 1
    for k in range(1, n):
        prod *= binomial(n, k)

    return prod


def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def D(n):
    return sum(divisors(B(n)))


def S(n):
    s = 0
    for i in range(1, n+1):
        temp = D(i)
        s += temp
        print("D(", i, ") =", temp)
    print("S(", n, ") =", s)
    return s


# print(B(5))
# print(B(100))
# print()

# print(divisors(60))
# print(divisors(B(5)))
# print()

# print(D(5))
# print()

# print(S(5))
print(S(10))
