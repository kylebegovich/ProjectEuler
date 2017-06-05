upper_bound = (1000000 / 6) + 1


def condition(x):
    if x > upper_bound:
        print("something went wrong")
        return False


def increment(x):
    if not len(x) is 6:
        print("some kinda issue")
        return
    else:
        if x[5] is 9:
            if x[4] is 9:
                if x[3] is 9:
                    x[2] += 1
                    x[3] = 0
                else:
                    x[3] += 1
                    x[4] = 0
            else:
                x[4] += 1
                x[5] = 0
        else:
            x[5] += 1

if __name__ == '__main__':

    x = [1, 2, 3, 4, 5, 6]

    while True:
        if condition(x):
            break
        increment(x)

    print("done", x)
