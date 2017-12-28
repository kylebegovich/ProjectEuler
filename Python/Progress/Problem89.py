input_strs = open("p083_matrix.txt", 'r')

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

only_once = {'D', 'L', 'V'}
no_exceed = {'M', 'C', 'X'}

single_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
double_values = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


def roman_to_dec(in_str):
    value = 0

    for key in double_values:
        if key in in_str:
            in_str = in_str.replace(key, '')
            value += double_values[key]

    for char in in_str:
        value += single_values[char]

    return value


def dec_to_roman(in_num):
    listed = [int(d) for d in str(in_num)]
    output = ""
    add_I = False
    add_X = False
    add_C = False

    if listed[-1] == 4 or listed[-1] == 9:
        add_I = True
    if in_num > 10 and (listed[-2] == 4 or listed[-2] == 9):
        add_X = True
    if in_num > 100 and (listed[-3] == 4 or listed[-3] == 9):
        add_C = True



    return output


def compress(roman):
    new = dec_to_roman(roman_to_dec(roman))
    return len(roman) - len(new)


def main():
    saved = 0

    for line in input_strs:
        saved += compress(line)

    print(saved)

    input_strs.close()


main()
#print(roman_to_dec("MMDCCXLII"))
