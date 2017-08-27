
triag = lambda n: n * (n + 1) / 2
square = lambda n: n*n
pent = lambda n: n * (3*n - 1) / 2
hexa = lambda n: n * (2*n - 1)
hept = lambda n: n * (5*n - 5) / 2
octa = lambda n: n * (3*n - 2)


triag_4s = list()
square_4s = list()
pent_4s = list()
hexa_4s = list()
hept_4s = list()
octa_4s = list()


def fill_lists():
    # these bounds were hand-calculated for each set, to be the 4 digit nums in each figurate set
    for i in range(45, 141):
        triag_4s.append(int(triag(i)))

    for i in range(32, 100):
        square_4s.append(int(square(i)))

    for i in range(26, 82):
        pent_4s.append(int(pent(i)))

    for i in range(23, 71):
        hexa_4s.append(int(hexa(i)))

    for i in range(21, 64):
        hept_4s.append(int(hept(i)))


    for i in range(19, 59):
        octa_4s.append(int(octa(i)))


def test_pre_generated_lists():
    for elem in triag_4s:
        if len(str(elem)) != 4:
            print ("BAD!!!", elem, 1)
            return False

    for elem in square_4s:
        if len(str(elem)) != 4:
            print ("BAD!!!", elem, 2)
            return False

    for elem in pent_4s:
        if len(str(elem)) != 4:
            print ("BAD!!!", elem, 3)
            return False

    for elem in hexa_4s:
        if len(str(elem)) != 4:
            print ("BAD!!!", elem, 4)
            return False

    for elem in hept_4s:
        if len(str(elem)) != 4:
            print ("BAD!!!", elem, 5)
            return False

    for elem in octa_4s:
        if len(str(elem)) != 4:
            print ("BAD!!!", elem, 6)
            return False

    return True

fill_lists()
test_pre_generated_lists()

# make sure there's not a 0 in the ten's place, as you can't cycle with that property
temp = list()
for elem in triag_4s + square_4s + pent_4s + hexa_4s + hept_4s + octa_4s:
    if not (elem % 100) // 10 == 0 and not elem % 100 == elem // 100:
        temp.append(elem)

master_set = set(temp)
master_checker = [set(triag_4s), set(square_4s), set(pent_4s), set(hexa_4s), set(hept_4s), set(octa_4s)]


def find_candidates(current):
    return [n for n in master_set if n // 100 == current % 100 and n % 100 != current // 100]


def generate_chain(curr_num, curr_chain, curr_done):
    print(curr_num, curr_chain, curr_done)
    if curr_chain is not None and sorted(curr_chain) == [0, 1, 2, 3, 4, 5]:
        return curr_chain

    owf = False
    next = 0
    candidates = find_candidates(curr_num)
    for potent in candidates:
        for i in [n for n in range(6) if n not in curr_done]:
            if potent in master_checker[i]:
                next = potent
                curr_done.append(i)
                curr_chain.append(potent)
                owf = True
                break
        if owf:
            return generate_chain(next, curr_chain, curr_done)


def main():

    for elem in master_set:
        num = 0
        for i in range(6):
            if elem in master_checker[i]:
                num = i
                break

        chain = generate_chain(elem, [elem], [num])
        if type(chain) == list and len(chain) == 6 and chain[5] % 100 == chain[0] // 100:
            return chain
        else:
            print(elem, "did not work")


out = main()
print(sum(out), out)
