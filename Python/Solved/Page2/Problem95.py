from Euler import d as sum_divisors


found = set()
app = found.add


def make_chain(num, chain, bound):
    #print(num, chain, bound)
    if num > bound or num == 1:
        return None

    app(num)

    if num in chain:
        cycle_start = chain.index(num)
        chain_len = len(chain) - cycle_start
        #print(chain_len, chain[cycle_start:])
        return chain_len, chain[cycle_start:]

    chain.append(num)
    return make_chain(int(sum_divisors(num)), chain, bound)


def main(bound):

    longest = 1
    chain = []

    for i in range(bound):
        if i in found:
            continue
        temp_tupe = make_chain(i, [], bound)
        if temp_tupe is not None and temp_tupe[0] > longest:
            print(temp_tupe, min(temp_tupe[1]))
            longest = temp_tupe[0]
            chain = temp_tupe[1]

    print(chain)
    return(min(chain))


print(main(1000000))


# SOLVED : 14316
    # I'll be honest, i didn't actually let my algorithm finish running, but it gave me the correct answer pretty quick
