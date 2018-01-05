

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


def fill_lists():
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
            triag_4s.add(int(t))

    for i in range(150):
        t = pent(i)
        if 999 < t < 10000:
            triag_4s.add(int(t))

    for i in range(120):
        t = hexa(i)
        if 999 < t < 10000:
            triag_4s.add(int(t))

    for i in range(120):
        t = hept(i)
        if 999 < t < 10000:
            triag_4s.add(int(t))

    for i in range(100):
        t = octa(i)
        if 999 < t < 10000:
            triag_4s.add(int(t))

    return triag_4s, square_4s, pent_4s, hexa_4s, hept_4s, octa_4s


def generate_chain(curr_list, curr_markers, master_set, master_list):
    if len(curr_list) == 6 and (curr_list[0] // 100) == (curr_list[-1] % 100):
        return curr_list
    canidates = [n for n in master_set if (n // 100) == (curr_list[-1] % 100) and n not in curr_list]

    # the check for
    for cand in canidates:
        cand_marker = find_marker(cand, master_list)
        if cand_marker not in curr_markers:
            curr_list.append(cand)
            curr_markers.append(cand_marker)
            #print(curr_list)
            #print(curr_markers)
            return generate_chain(curr_list, curr_markers, master_set, master_list)

    return []


def find_marker(num, master_list):
    for i in range(len(master_list)):
        if num in master_list[i]:
            return i

    print("SOMETHING BROKE, SEND HELP")
    return -1


def main():

    sets = fill_lists()
    master_set = sets[0] | sets[1] | sets[2] | sets[3] | sets[4] | sets[5]
    master_list = [sets[0], sets[1], sets[2], sets[3], sets[4], sets[5]]

    print(master_set)

    for elem in master_set:
        if len(str(elem)) != 4:
            print(elem)
            return
        chain = generate_chain([elem], [find_marker(elem, master_list)], master_set, master_list)
        if len(chain) == 6:
            print("FOUND A CHAIN")
            return chain


print(main())
