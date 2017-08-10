a = 3
b = 5
maximum = 1000

print(sum(list(filter((lambda x: x % 3 == 0 or x % 5 == 0), range(1, 1000)))))

# SOLVED : 233168
