def is_weird_fraction(numerator, denominator):
    frac = numerator/(denominator * 1.0)
    num1 = numerator / 10
    num2 = numerator % 10
    den1 = denominator / 10
    den2 = denominator % 10

    if num1 == den1 and den2 != 0 and num2/(den2*1.0) == frac:
        print(frac, numerator, denominator, num1, num2, den1, den2)
        return True
    if num1 == den2 and den1 != 0 and num2/(den1*1.0) == frac:
        print(frac, numerator, denominator, num1, num2, den1, den2)
        return True
    if num2 == den1 and den2 != 0 and num1/(den2*1.0) == frac:
        print(frac, numerator, denominator, num1, num2, den1, den2)
        return True

    return False


if __name__ == '__main__':
    list_weirdos = []
    for i in range(10, 100):
        for j in range(i+1, 100):
            print(i,j)
            if i < j and is_weird_fraction(i, j):
                list_weirdos.append([i, j])

    print(list_weirdos)
    numerators = 1
    denominators = 1
    for x in list_weirdos:
        numerators *= x[0]
        denominators *= x[1]
    print (numerators, denominators, numerators/(denominators*1.0))


# SOLVED : 100
