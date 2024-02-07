def step(n):
    return (n + 1504170715041707) % 4503599627370517

def step2(n):
    return (n - 8912517754604) % 4503599627370517
        
def main():
    curr_min = 258162
    curr_num = 2776186651961100
    rolling_sum = 1517926517477964
    for i in range(16463000000, 5000000000001):
        if (i % 1000000 == 0):
            print(i, curr_num, curr_min)
        if curr_num < curr_min:
            print("({}) {} is a coin!".format(i, curr_num))
            rolling_sum += curr_num
            curr_min = curr_num
            print("current sum:", rolling_sum)
            
        curr_num += 1504170715041707
        curr_num %= 4503599627370517
        
# def main():
#     curr_min = 1504170715041707+1
#     curr_num = 1504170715041707
#     rolling_sum = 0
#     for i in range(1, 1000000):
#         # if (i % 1000000 == 0):
#         #     print(i, curr_num, curr_min)
#         if curr_num < curr_min:
#             print("({}) {} is a coin!".format(i, curr_num))
#             rolling_sum += curr_num
#             curr_min = curr_num
#             print("current sum:", rolling_sum)
            
#         curr_num += 1504170715041707
#         curr_num %= 4503599627370517


main()

# val = 1504170715041707
# for i in range(10):
#     print(val)
#     val = step(val)


