one_to_nine = 36  # one two three four five six seven eight nine
ten = 3
eleven_to_nineteen = 67  # eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
tens_places = 46  # those above this one
hundred = 7
one_thousand = 11


if __name__ == '__main__':
    less_than_hundred = one_to_nine + ten + eleven_to_nineteen + tens_places + tens_places * one_to_nine
    summation = one_to_nine * hundred + one_to_nine * hundred * less_than_hundred
    print summation
