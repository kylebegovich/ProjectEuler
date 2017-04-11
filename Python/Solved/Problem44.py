import math


def generate_pentagonal_nums(num):
    arr = []
    for i in range(1, num+1):
        curr = i*(3*i-1)/2
        arr.append(curr)

    return arr


if __name__ == '__main__':
    upper_bound = 3000
    minimum = 10000000000
    array = generate_pentagonal_nums(upper_bound)

    for j in array:
        for k in array:
            print (j, k)
            summ = j + k
            diff = abs(j - k)
            if summ in array and diff in array:
                print(diff)
                if diff < minimum:
                    minimum = diff
                    print("new minimum: ", minimum)

    print ("minimum: ", minimum)


# SOLVED : 5482660
