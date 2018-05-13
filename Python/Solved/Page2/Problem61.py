
def triag(n):
    return (n * (n + 1)) / 2

def square(n):
    return n * n

def pent(n):
    return (n * (3*n - 1)) / 2

def hexa(n):
    return n * (2*n - 1)

def hept(n):
    return (n * (5*n - 3)) / 2

def octa(n):
    return n * (3*n - 2)


def generate_chain(curr_chain, curr_groups, master_list):
    if curr_chain is None or curr_groups is None or master_list is None:
        return 0
    if len(curr_chain) == 6 and (curr_chain[0] // 100 == curr_chain[5] % 100):
        # this is the correct chain
        return sum(curr_chain)
    if len(curr_chain) > 6:
        return 0

    for i in range(1, 6):
        print(curr_chain, "\n", curr_groups, "\n", master_list[i], "\n\n")
        if 0 == curr_groups[i]:
            for elem in master_list[i]:
                if elem // 100 == curr_chain[-1] % 100:
                    next_chain = [] + curr_chain + [elem]
                    next_groups = [] + curr_groups
                    next_groups[i] = 1
                    possible = generate_chain(next_chain, next_groups, master_list)
                    if possible != 0:
                        return possible
                #else:
                    #print(elem, last)
    return 0


def main():
    triag_4s = set()
    square_4s = set()
    pent_4s = set()
    hexa_4s = set()
    hept_4s = set()
    octa_4s = set()

    for i in range(200):
        t = triag(i)
        if 999 < t < 10000:
            triag_4s.add(int(t))

    for i in range(175):
        t = square(i)
        if 999 < t < 10000:
            square_4s.add(int(t))

    for i in range(150):
        t = pent(i)
        if 999 < t < 10000:
            pent_4s.add(int(t))

    for i in range(120):
        t = hexa(i)
        if 999 < t < 10000:
            hexa_4s.add(int(t))

    for i in range(120):
        t = hept(i)
        if 999 < t < 10000:
            hept_4s.add(int(t))

    for i in range(100):
        t = octa(i)
        if 999 < t < 10000:
            octa_4s.add(int(t))

    print(triag_4s, len(triag_4s), "\n")
    print(square_4s, len(square_4s), "\n")
    print(pent_4s, len(pent_4s), "\n")
    print(hexa_4s, len(hexa_4s), "\n")
    print(hept_4s, len(hept_4s), "\n")
    print(octa_4s, len(octa_4s), "\n")

    master_list = list()
    master_list.append(list(triag_4s))
    master_list.append(list(square_4s))
    master_list.append(list(pent_4s))
    master_list.append(list(hexa_4s))
    master_list.append(list(hept_4s))
    master_list.append(list(octa_4s))
    print(master_list, len(master_list), "\n\n")


    # can do only traig because one of the elems would be a triag
    for elem in triag_4s:
        answer = generate_chain([elem], [1, 0, 0, 0, 0, 0], master_list)
        if answer is not None and answer != 0:
            return answer
        print(elem, "is not in the chain")


print(main())
