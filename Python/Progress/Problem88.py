product_sum_nums = []


def product(lst):
    result = 1
    for num in lst:
        result *= num

    print("pro:", lst, result)
    return result


def increment(lst):
    l = len(lst)
    for k in range(l-1, -1, -1):
        if not lst[k] == 9:
            lst[k] += 1
            return lst
        else:
            lst[k] = 1


def find_min_p_s_num(k):
    curr_nums = []
    for j in range(k):
        curr_nums.append(1)

    minimum = 5**k
    escape = 4

    try:
        for i in range(0, 9**k):
            if curr_nums is None:
                print("something went wrong")
                return 0
            temp = product(curr_nums)
            temp2 = sum(curr_nums)
            print("sum:", curr_nums, sum(curr_nums))
            if temp == temp2:
                escape -= 1
                print(temp)
                if temp < minimum:
                    print("new min: ", temp)
                    minimum = temp

            if escape == 0:
                raise StopIteration

            curr_nums = increment(curr_nums)
    except StopIteration:
        return minimum
    return minimum


if __name__ == '__main__':

    answers = {}
    for i in range(2, 12001):
        temp = find_min_p_s_num(i)
        if temp not in answers:
            answers[temp] = 1

    print(answers)
    print(set(answers))
    print(sum(set(answers)))
