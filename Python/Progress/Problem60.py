from Euler import prime_sieve, is_prime


result = int(100000000)
primes = prime_sieve(30000)
pairs = () * len(primes)


def concat(first, second):
    return int( str(first) + str(second) )


def make_pairs(list_of_primes):
    pairs = list()
    if list_of_primes is None:
        return
    for elem in list_of_primes:
        for other_elem in list_of_primes:
            if elem is other_elem:
                continue
            pairs.append(concat(elem, other_elem))

    return pairs


def main():
    answers = list()
    for index_a in range(0, len(primes)):
        answers = [primes[index_a]]

        for index_b in range(index_a, len(primes)):
            if all([is_prime(n) for n in iter(make_pairs(answers + [primes[index_b]]))]):
                answers.append(primes[index_b])

                for index_c in range(index_b, len(primes)):
                    if all([is_prime(n) for n in iter(make_pairs(answers + [primes[index_c]]))]):
                        answers.append(primes[index_c])

                        for index_d in range(index_c, len(primes)):
                            if all([is_prime(n) for n in iter(make_pairs(answers + [primes[index_d]]))]):
                                answers.append(primes[index_d])

                                for index_e in range(index_d, len(primes)):
                                    if all([is_prime(n) for n in iter(make_pairs(answers + [primes[index_e]]))]):
                                        answers.append(primes[index_e])
                                        return answers

    return "Failed", answers


def test_concat():
    print(concat(5, 5))
    print(concat(1512, 4))
    print(concat(9, 0))


def test_make_pairs():
    print(make_pairs([1, 3, 5]))
    print(make_pairs([7, 9]))
    print(make_pairs([75, 23, 18]))

    test = make_pairs([3, 7, 109, 673])
    for elem in iter(test):
        print(elem, is_prime(elem))


test_concat()
test_make_pairs()
print(main())
