from math import log10

def digits(n):
    return int(log10(n))+1

def is_pandigital(n, s=9): n = str(n); return len(n) == s and not '123456789'[:s].strip(n)

def is_pandigital_prefix(n):
    num_digits = digits(n)
    if num_digits < 9:
        return
    prefix = n // (10 ** (num_digits - 9))
    # print(prefix)
    return is_pandigital(prefix)

def is_pandigital_suffix(n):
    suffix = n % 1000000000
    # print(suffix)
    return is_pandigital(suffix)

def is_both_pandigital(n):

    suf = is_pandigital_suffix(n)
    if (suf):
        print("\n\nSUFFIX IS PAN!\n\n")
    else:
        return False
    
    pre = is_pandigital_prefix(n)
    # print(n, "pre", pre, "suf", suf)
    if (pre):
        print("\n\nPREFIX IS PAN!\n\n")

    return pre and suf



def main():
    Fa = 1
    Fb = 1
    for i in range(1,1000000):
        is_both = is_both_pandigital(Fa)
        print(i, is_both)
        if (is_both):
            print("🎉🎉🎉\nFOUND IT: {}\n🎉🎉🎉".format(i))
            return
        new = Fa + Fb
        Fa = Fb
        Fb = new


# 17.283 seconds execution time
main()