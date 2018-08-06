
# cite: https://blog.dreamshire.com/project-euler-88-solution/
#   DP solution that absolutely destroys mine:
def prodsum(product, sum, num_factors, start):

    k = product - sum + num_factors
    # print('product =', product, '  sum =', sum, '  num_factors =',num_factors, '  start =', start, '   k = ', k)
    if k < kmax:
        if product < n[k]: n[k] = product
        for i in range(start, kmax // product * 2 + 1):
            prodsum(product * i, sum + i, num_factors + 1, i)

kmax = 12000
n = [2*kmax] * kmax
prodsum(1, 1, 1, 2)

print(sum(set(n[2:])))


# SOLVED : 7587457
