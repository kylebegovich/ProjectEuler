from Euler import is_prime


num_diag_primes = 3
step_length = 2
corner = 9


while float(num_diag_primes)/(2 * step_length + 1) > 0.1:
    step_length += 2
    for i in range(0, 3):
        corner += step_length
        if is_prime(corner):
            num_diag_primes += 1
    corner += step_length

print(step_length+1)


# SOLVED : 26241
