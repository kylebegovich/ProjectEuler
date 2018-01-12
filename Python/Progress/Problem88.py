from Euler import factors


def increment(lst):
    l = len(lst)
    for k in range(l-1, -1, -1):
        if not lst[k] == 9:
            lst[k] += 1
            return lst
        else:
            lst[k] = 1


def find_min_p_s_num(k):
    facs = factors(k)
    print(max(facs))
    return -1


def main():
    answers = {}
    for i in range(2, 12001):
        print(i)
        temp = find_min_p_s_num(i)
        if temp not in answers:
            answers[temp] = 1

    print(answers)
    print(set(answers))
    print(sum(set(answers)))


main()
