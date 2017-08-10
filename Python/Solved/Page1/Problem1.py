a = 3
b = 5
maximum = 1000

print(sum(list(filter((lambda x: x % a == 0 or x % b == 0), range(1, 1000)))))

# SOLVED : 233168
