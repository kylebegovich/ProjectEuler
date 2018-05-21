# let's simulate monopoly...
import random


chance_spaces = {7, 22, 36}
community_chest_spaces = {2, 17, 33}


def roll_die(num_sides):
    return random.randint(1, num_sides)


def draw_card(deck):
    #print(deck)
    card = deck[0]
    deck.append(card)
    deck.remove(card)
    #print(deck, card)
    return card


def do_turn(curr_space, num_sides, chance_deck, cc_deck, doubles_count):
    roll1 = roll_die(num_sides)
    roll2 = roll_die(num_sides)

    if roll1 == roll2:
        doubles_count += 1
    else:
        doubles_count = 0

    if doubles_count == 3:
        return 10, 0

    roll = roll1 + roll2

    curr_space += roll
    if curr_space >= 40:
        curr_space -= 40

    if curr_space in chance_spaces:
        r = draw_card(chance_deck)
        if r > 10:
            no_op = 1
        elif r == 1:
            curr_space = 0
        elif r == 2:
            curr_space = 10
        elif r == 3:
            curr_space = 11
        elif r == 4:
            curr_space = 24
        elif r == 5:
            curr_space = 39
        elif r == 6:
            curr_space = 5
        elif r == 7 or r == 8:
            if curr_space == 7:
                curr_space = 15
            elif curr_space == 22:
                curr_space = 25
            elif curr_space == 36:
                curr_space = 5
            else:
                print("SOMETHING WENT WRONG (chance rr's)")
        elif r == 9:
            curr_space = 0
        elif r == 10:
            curr_space -= 3
        else:
            print("SOMETHING WENT WRONG (bad r in chance)")

    elif curr_space in community_chest_spaces:
        r = draw_card(cc_deck)
        if r == 1:
            curr_space = 0
        elif r == 2:
            curr_space = 10
        else:
            no_op = 1

    if curr_space == 30:
        curr_space = 10

    return curr_space, doubles_count


def answer_from_map(spaces_visited):
    first = -1, 0
    second = -1, 0
    third = -1, 0
    for k in spaces_visited.keys():
        val = spaces_visited[k]
        if val > first[1]:
            third = second
            second = first
            first = k, val
        elif val > second[1]:
            third = second
            second = k, val
        elif val > third[1]:
            third = k, val

    return first[0] * 10000 + second[0] * 100 + third[0]


def main(num_sides, turns):
    spaces_visited = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                      15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0,
                      29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0}

    curr_space = 0
    chance_deck = list(range(1, 17))
    cc_deck = list(range(1, 17))
    random.shuffle(chance_deck)
    random.shuffle(cc_deck)
    doubles_count = 0

    for i in range(turns):
        turn = do_turn(curr_space, num_sides, chance_deck, cc_deck, doubles_count)
        curr_space = turn[0]
        spaces_visited[curr_space] += 1
        doubles_count = turn[1]

    #print(spaces_visited)
    return answer_from_map(spaces_visited)


print(main(4, 1000000))


# SOLVED : 101524
