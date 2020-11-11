# Old, lame version:
#
# def get_repeater_length(blank, num):
#     for t in range(1, num):
#         if 1 == 10 ** t % num:
#             return t
#     return 0
#
#
# if __name__ == '__main__':
#     longest = max(get_repeater_length(1, i) for i in range(2, 1001))
#     print([i for i in range(2, 1001) if get_repeater_length(1, i) == longest][0])




def rep_length(N):
    seq = []
    length = 0
    curr = 1
    found = {}
    while curr not in found:
        found[curr] = length
        digit, curr = divmod(curr, N)
        seq.append(digit)
        curr *= 10
        length += 1

    # print(seq)
    return length - found[curr]



def main(N):
    max_len = 0
    max_index = 0
    for i in range(2, N):
        length = rep_length(i)
        if length > max_len:
            max_len = length
            max_index = i
            # print(i, "with a length of", length, "is the new max_len")

    return max_index

print(main(1000))


# SOLVED : 983
