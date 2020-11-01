from math import log10, floor

# N = 12
N = 101
# N = 1000001

def n_squares(n):
    return [i**2 for i in range(2, n)]

# print(n_squares(11))
# print(n_squares(100))


##### This block from stackoverflow:
# https://stackoverflow.com/questions/37023774/all-ways-to-partition-a-string
import itertools

memo = {}

def multiSlice(s,cutpoints):
    k = len(cutpoints)
    if k == 0:
        return [s]
    else:
        multislices = [s[:cutpoints[0]]]
        multislices.extend(s[cutpoints[i]:cutpoints[i+1]] for i in range(k-1))
        multislices.append(s[cutpoints[k-1]:])
        return multislices

def allPartitions(s):
    n = len(s)
    cuts = list(range(1,n))
    for k in range(n):
        for cutpoints in itertools.combinations(cuts,k):
            yield multiSlice(s,cutpoints)

##### End block
print(list(allPartitions([int(i) for i in str(12345)])))

def list_sum(num_list):
    outer_sum = 0
    for sub_list in num_list:
        inner_sum = 0
        power = 1
        for digit in sub_list[::-1]:
            inner_sum += power * digit
            power *= 10
        outer_sum += inner_sum
    return outer_sum

# print(list_sum([[1, 2], [3, 4]]))
# print(list_sum([[1, 2, 3, 4]]))
# print(list_sum([[1], [2], [3], [4]]))

def is_s_num(num):
    sqrt = num**0.5
    for part in allPartitions([int(i) for i in str(num)]):
        if sqrt == list_sum(part):
            return True
    return False

# print(81, is_s_num(81))
# print(64, is_s_num(64))
# print(8281, is_s_num(8281))
# print(9801, is_s_num(9801))

def T(N):
    squares = n_squares(N)
    sum = 0
    for n in squares:
        if is_s_num(n):
            print(n, "is true")
            sum += n

    return sum

print(T(N))
