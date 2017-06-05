lower_bound = 100000
upper_bound = int(1000000 / 6)


def condition(num):
    if num > upper_bound:
        print("something went wrong")
        return False
    else:
        list1 = sorted([int(d) for d in str(num*1)])
        list2 = sorted([int(d) for d in str(num*2)])
        list3 = sorted([int(d) for d in str(num*3)])
        list4 = sorted([int(d) for d in str(num*4)])
        list5 = sorted([int(d) for d in str(num*5)])
        list6 = sorted([int(d) for d in str(num*6)])

        if list1 == list2 == list3 == list4 == list5 == list6:
            return True



if __name__ == '__main__':

    for x in range(lower_bound, upper_bound):
        if condition(x):
            print(x)
            break

    print("done")


# SOLVED : 142857
