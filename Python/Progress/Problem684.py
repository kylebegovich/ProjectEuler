from Euler import fibonacci

memo = {1: 0}
memo_max = 1
mod = 1000000007

# def s(n):
#     if n < 10:
#         return n
#     return (10 * s(n-9)) + 9

def s(n):
    acc = 0
    num_nines = n // 9
    for i in range(num_nines):
        acc *= 10
        acc += 9
        acc %= mod
        # print(acc)

    return (((n % 9) * ((10 ** num_nines) % mod)) + acc) % mod

# def s(n):
#     num_nines = n // 9
#     first_dig = n % 9
#     nines = 10 ** num_nines - 1
#     num = 10 ** num_nines * first_dig
#     return num + nines
#
# print(s(1), s2(1))
# print(s(10), s2(10))
# print(s(11), s2(11))
# print(s(2000) % mod, s2(2000))

def S(k):
    if k in memo:
        return memo[k]

    global memo_max
    running_sum = memo[memo_max]
    for n in range(memo_max, k+1):
        s_n = s(n) % mod
        running_sum += s_n
        memo[n] = running_sum
        print("s_n", n, s_n)
        print("running_sum", running_sum)

    memo_max = k
    return running_sum

# print(S(20))


# CITE: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# CITE: https://github.com/trizen/project-euler/blob/master/Sidef/684%20Inverse%20Digit%20Sum%20--%20v2.sf
# Was stuck trying to make a closed form for s(), found this closed form for S() instead...
def S2(k):
    n = k // 9
    r = k % 9 + 2

    return ((((r-1)*r + 10) * pow(10, n, mod) - 2*(r + 9*n + 4)) * modinv(2, mod)) % mod

print(S2(20))

def sum_fibs(n):
    running_sum = 0
    for i in range(2, n+1):
        f = fibonacci(i)
        Sf = S2(f) % mod
        running_sum = (running_sum + Sf) % mod
        print("i", i)
        print("f", f)
        print("running_sum", running_sum)

    return running_sum


# print(sum_fibs(10))
print(sum_fibs(90))


# SOLVED: 922058210
