import Euler

lim = 10 ** 14
primes = Euler.prime_sieve(lim)


def digit_sum(num):
    if num < 10:
        return num
    first = num % 10
    return first + digit_sum(num // 10)


def is_harshad(num):
    # print("is_harshad", num)
    return num % digit_sum(num) == 0


def is_right_harshad(num):
    # print("is_right_harshad", num)
    if num <= 10:
        return True
    return is_harshad(num) and is_right_harshad(num // 10)


def is_strong_harshad(num):
    # print("is_strong_harshad", num)
    if not is_harshad(num):
        return False
    # if not Euler.is_prime(num // digit_sum(num)):
    #     return False
    if not num // digit_sum(num) in primes:
        return False
    return True


def is_strong_right_harshad(num):
    # print("is_strong_right_harshad", num)
    return is_right_harshad(num) and is_strong_harshad(num)


def is_strong_right_harshad_prime(num):
    # print("is_strong_right_harshad_prime", num)
    return is_strong_right_harshad(num // 10)


def main():
    s = 0
    for p in primes:
        if p > 10 and is_strong_right_harshad_prime(p):
            s += p

    return s


# print(main(10 ** 14))
# print(main(10 ** 7))
print(main())

# print(digit_sum(1234))
# print(digit_sum(1000))
# print(digit_sum(72148))

# print(is_right_harshad(10000000000000000000001))
# print(is_right_harshad(18))
# print(is_right_harshad(201))
# print(is_right_harshad(2011))
# print(is_right_harshad(1000000000))

# print(is_strong_harshad(10000000000000000000001))
# print(is_strong_harshad(18))
# print(is_strong_harshad(201))
# print(is_strong_harshad(2011))
# print(is_strong_harshad(1000000000))

# print(is_strong_right_harshad(10000000000000000000001))
# print(is_strong_right_harshad(18))
# print(is_strong_right_harshad(201))
# print(is_strong_right_harshad(2011))
# print(is_strong_right_harshad(1000000000))

# print(is_strong_right_harshad_prime(10000000000000000000001))
# print(is_strong_right_harshad_prime(18))
# print(is_strong_right_harshad_prime(201))
# print(is_strong_right_harshad_prime(2011))
# print(is_strong_right_harshad_prime(1000000000))
