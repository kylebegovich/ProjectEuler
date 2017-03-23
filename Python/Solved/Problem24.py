import math

curr = 0
goal = 1000000
potential_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output_num = []

if __name__ == '__main__':

    for i in xrange(10, 0, -1):
        print (curr, i, "outer loop")
        for j in xrange(i + 1):
            print (curr, j, "inner loop")
            temp = math.factorial(i - 1) * j + curr
            if temp >= goal:
                print (temp)
                curr += (math.factorial(i - 1) * (j-1))
                print (curr, goal, i, j)
                output_num.append(potential_nums[j-1])
                potential_nums.remove(potential_nums[j-1])
                break

    print output_num


# SOLVED : 2783915460
