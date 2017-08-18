from Euler import strings_to_ints


def contfrac_to_frac(seq):
    num, den = 1, 0
    for u in reversed(seq):
        num, den = den + num*u, num
    return num, den


seq = [2 * (i+1) // 3 if i%3 == 2 else 1 for i in range(100)]
seq[0] += 1
n, d = contfrac_to_frac(seq)

# sorry this looks gross, just type issues needing to be resolved
print( sum( strings_to_ints( list( str(n) ))))


# SOLVED : 272
