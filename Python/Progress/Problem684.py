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

    return (((n % 9) * 10 ** num_nines) + acc) % mod

# def s(n):
#     num_nines = n // 9
#     first_dig = n % 9
#     nines = 10 ** num_nines - 1
#     num = 10 ** num_nines * first_dig
#     return num + nines

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
        # print("s_n", n, s_n)
        # print("running_sum", running_sum)

    memo_max = k
    return running_sum

# print(S(20))

def sum_fibs(n):

    running_sum = 0
    for i in range(2, n):
        f = fibonacci(i)
        Sf = S(f) % mod
        running_sum += Sf
        print("i", i)
        print("f", f)
        print("running_sum", running_sum)


# print(sum_fibs(90))
