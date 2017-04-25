hundred = 7
hundred_and = 10
one_thousand = 11

single_digits = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
teens = {0:0, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
tens_places = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}


def letters_in(num):
    if num < 10:
        return single_digits[num]
    elif num < 20:
        return teens[num]
    elif num < 100:
        return tens_places[num/10] + single_digits[num%10]
    elif num == 1000:
        return 11
    else:
        # this is numbers between 100-999
        if num%100 > 0:
            return single_digits[num/100] + hundred_and + letters_in(num%100)
        else:
            return single_digits[num/100] + hundred


if __name__ == '__main__':

    count = 0
    for i in range(1, 1001):
        temp = letters_in(i)
        count += temp
        print(temp, i)

    print (count)


# SOLVED : 21124
