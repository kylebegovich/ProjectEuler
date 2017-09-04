from Progress.Euler import gcd


a = 3
b = 2
upper_bound = 12000
count = 0


# very naive... but it works in just a few seconds so it's cool
for d in range(2, 12001):
    for n in range((d // a) + 1, ((d - 1) // b) + 1):
        if gcd(n, d) == 1:
            print("added ", n, "/", d)
            count += 1


print(count)


# SOLVED : 7295372
