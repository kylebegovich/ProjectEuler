import itertools, Euler

def shuffle(deck):
    l = len(deck) // 2
    shuffled = []
    app = shuffled.append
    for i in range(l):
        app(deck[i])
        app(deck[i+l])

    return shuffled


def count_num_shuffles(deck_len):
    deck = [i for i in range(1, deck_len+1)]
    curr = shuffle(deck)
    count = 0

    while curr != deck:
        # print(curr)
        count += 1
        curr = shuffle(curr)

    return count


for i in range(2, 30, 2):
    print(count_num_shuffles(i))
    print()
