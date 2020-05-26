


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


# can prob parameterize sB, sC, lB, lC, if need be
def check_special_condition(B, C):
    sB = sum(B)
    sC = sum(C)
    if sB == sC:
        return False

    lB = len(B)
    lC = len(C)

    if lB > lC and sB < sC:
        return False

    if lB < lC and sB > sC:
        return False


n6 = [11, 18, 19, 20, 22, 25]

def wiggle_solutions(arr, wiggle):
    potential_arrays = []
    for i in range(len(arr)):
        for j in range(-1 * wiggle, wiggle + 1):
            print("oof")
