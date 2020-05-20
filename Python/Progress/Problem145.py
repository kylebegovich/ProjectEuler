


def reverse(n_str):
    return n_str[::-1]


# the property we want, for non-carry sums, is for indices (i, n-i-1) to be opposite pairity
#   for carry-sums, (i, n-i-1) to the same pairty, with indices (i-1, n-i) > 10
def construction(limit):

    non_carry_pairs = []
    pair_temp = [1, 0]
    while pair_temp[0] + pair_temp[1] < 10:
        non_carry_pairs.append(pair_temp)
        next_pair = [pair_temp[0], pair_temp[1] + 2]

        # this line guarentees that the sum doesn't carry
        if next_pair[0] + next_pair[1] > 9:
            next_pair[0] += 2
            next_pair[1] = 0
        pair_temp = next_pair

    middle_factors = 2*len(non_carry_pairs)
    print("\nmiddle-pairs:", middle_factors)
    [print(p) for p in non_carry_pairs]

    non_carry_pairs = [p for p in non_carry_pairs if p[1] != 0]
    non_carry_factor = 2*len(non_carry_pairs)
    print("\nnon-carry:", non_carry_factor)
    [print(p) for p in non_carry_pairs]


    carry_pairs = []
    pair_temp = [3, 8]
    while pair_temp[0] < 10:
        carry_pairs.append(pair_temp)
        next_pair = [pair_temp[0], pair_temp[1] + 2]

        # this line guarentees that the second digit is a single digit
        if next_pair[1] > 9:
            next_pair[0] += 2
            next_pair[1] = 11 - next_pair[0]
        pair_temp = next_pair

    carry_factor = 2*len(carry_pairs)
    print("\ncarry:", carry_factor)
    [print(p) for p in carry_pairs]


    even_no_carry_pairs = []
    pair_temp = [0,0]
    while pair_temp[0] + pair_temp[1] < 10:
        even_no_carry_pairs.append(pair_temp)
        next_pair = [pair_temp[0], pair_temp[1] + 2]

        # this line guarentees that the second digit is a digit
        if next_pair[0] + next_pair[1] > 9:
            next_pair[0] += 2
            next_pair[1] = 0
        pair_temp = next_pair
    pair_temp = [1,1]
    while pair_temp[0] + pair_temp[1] < 10:
        even_no_carry_pairs.append(pair_temp)
        next_pair = [pair_temp[0], pair_temp[1] + 2]

        # this line guarentees that the second digit is a digit
        if next_pair[0] + next_pair[1] > 9:
            next_pair[0] += 2
            next_pair[1] = 1
        pair_temp = next_pair

    even_no_carry_factor = len(even_no_carry_pairs)
    print("\neven:", even_no_carry_factor)
    [print(p) for p in sorted(even_no_carry_pairs)]


    num_digits = len(str(limit))

    total = 0
    for digits in range(4, num_digits):

        # even number of digits
        if digits % 2 == 0:
            pairs = digits // 2
            temp = non_carry_factor * middle_factors**(pairs-1)
            print(digits, temp)
            total += temp

        if digits == 7:
            # kinda specific, analytic solution in this case:
            #   number of the form ABCDEFG, where D < 5, AG and CE carry, and BF even
            temp = 5 * carry_factor * carry_factor * even_no_carry_factor
            print(digits, temp)
            total += temp

    return total


def single_step(n, should_print):
    n_str = [int(d) for d in str(n)]  # this is one of the two slow lines
    if n_str[-1] == 0:
        return False

    n_rev = 0
    multiplier = 1
    for digit in n_str:
        n_rev += digit * multiplier
        multiplier *= 10

    flag = True
    n_sum = n + n_rev
    n_sum_str = [int(d) for d in str(n_sum)]  # this is the other slow line
    for i in range(len(n_sum_str)):
        if n_sum_str[i] % 2 == 0:
            flag = False
            break

    if flag:
        if should_print:
            print(n, n_sum, "true")
        return True
    else:
        if should_print:
            print(n, n_sum)
        return False


memo = set()

def main(start, limit):
    count = 0
    n = start

    while n < limit:
        if n in memo:
            count += 1
            # print("caught memo", n)
            n += 2
            continue

        if n == 100000:
            print(n, count)
        if n == 1000000:
            print(n, count)
        if n == 10000000:
            print(n, count)

        n_str = [int(d) for d in str(n)]  # this is one of the two slow lines
        if n_str[-1] == 0:
            n += 1
            continue

        n_rev = 0
        multiplier = 1
        for digit in n_str:
            n_rev += digit * multiplier
            multiplier *= 10

        flag = True
        n_sum = n + n_rev
        n_sum_str = [int(d) for d in str(n_sum)]  # this is the other slow line
        for i in range(len(n_sum_str)):
            if n_sum_str[i] % 2 == 0:
                flag = False
                break

        if flag:
            count += 1
            memo.add(n_rev)
            memo.add(n)
            print(n, n_sum, "true")
            n += 1
        else:
            # print(n, n_sum)
            n += 1

    print(sorted(memo))
    print(count)


def is_reversible(num):
    if num % 10 == 0:
        return False

    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10

    added = num + rev
    while added > 0:
        if (added % 10) % 2 == 0:
            return False
        added = added // 10

    memo.add(rev)
    return True

def optimized_brute(limit):
    count = 0
    n = 1
    while n < limit:
        if n % 10000 == 0:
            print(n, count)
        if n in memo or is_reversible(n):
            count += 1
            n += 1
        n += 1

    print(count)
    return count


# main(1, 30)
# main(1, 1000) # = 120
# main(1, 10000)
# main(1000, 10000)
# main(100000, 500000)
# main(10000, 100000)  # there are 0 of these... interesting
# main(1, 100000)
# main(100000, 120000)
# main(1000000, 1200000)  # there are 0 of these... interesting
# main(10000000, 10100000)
# print(10 ** 9)
# main(1, 10 ** 9)

# print(optimized_brute(10 ** 9))

print(120 + construction(10 ** 9))
