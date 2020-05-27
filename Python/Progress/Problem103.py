from itertools import combinations


# function described in the problem
def near_optimum(n, prev_A):
    mid_index = len(prev_A) // 2
    mid_elem = prev_A[mid_index]

    return [mid_elem + v for v in ([0] + prev_A)]

# Testing near_optimum function
# A = [1]
# for i in range(2, 7):
#     A = near_optimum(i, A)
#     print(i, A)


def wiggle_solutions(arr, wiggle):
    potential_arrays = []
    for i in range(len(arr)):
        potential_arrays.append([j + arr[i] for j in range(-1 * wiggle, wiggle + 1)])

    return potential_arrays



# can prob parameterize sB, sC, lB, lC, if needed
def check_special_condition(B, C):
    sB = sum(B)
    sC = sum(C)
    if sB == sC:
        return False

    return True


def check_all_subsets(A):
    # print("check_all_subsets")
    subsets = set()

    for i in range(2, 7):
        subsets = subsets.union(set(combinations(A, i)))

    for pair in combinations(subsets, 2):
        if not check_special_condition(pair[0], pair[1]):
            # print(False, pair[0], pair[1])
            return False

    A = sorted(A)
    sum1 = A[0]
    sum2 = 0

    for i in range(0, 4):
        sum1 += A[i + 1]
        sum2 += A[6 - i]

        if sum1 <= sum2:
            return False

    return True


n6 = [11, 18, 19, 20, 22, 25]

def main():
    arrs = wiggle_solutions(near_optimum(7, n6), 3)

    min_sum = 1000
    min_arr = []
    curr_sum_set = 0
    for v0 in arrs[0]:
        curr_sum_set += v0
        for v1 in arrs[1]:
            curr_sum_set += v1
            for v2 in arrs[2]:
                curr_sum_set += v2
                for v3 in arrs[3]:
                    curr_sum_set += v3
                    for v4 in arrs[4]:
                        curr_sum_set += v4
                        for v5 in arrs[5]:
                            curr_sum_set += v5
                            for v6 in arrs[6]:
                                curr_sum_set += v6
                                if curr_sum_set < min_sum:
                                    arr = [v0, v1, v2, v3, v4, v5, v6]
                                    # print(curr_sum_set, arr)
                                    if check_all_subsets(arr):
                                        min_sum = curr_sum_set
                                        min_arr = arr
                                        print("new min:", min_sum)

                                curr_sum_set -= v6
                            curr_sum_set -= v5
                        curr_sum_set -= v4
                    curr_sum_set -= v3
                curr_sum_set -= v2
            curr_sum_set -= v1
        curr_sum_set -= v0

    # print("oof")
    #
    # print(check_all_subsets(near_optimum(7, n6)))

    return sorted(list(min_arr))

print(main())
