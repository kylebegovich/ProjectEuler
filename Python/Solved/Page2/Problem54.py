import math


def has_flush(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_flush")
        return False
    else:
        last = len(a_hand[0])-1
        temp = a_hand[0][last]
        for card in a_hand:
            if not card[len(card)-1] == temp:
                return False
        else:
            return int(a_hand[4][0:2])


def has_straight(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_straight")
        return False
    else:
        ranks = []
        for card in a_hand:
            ranks.append(card[0:2])

        ranks = list(map(int, ranks))
        ranks = sorted(ranks)
        temp = ranks[0]
        for i in range(1, 5):
            if not ranks[i] == temp + 1:
                return False
            else:
                temp += 1
        return int(ranks[4])  # also return highest card


def has_four_of_kind(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_four_of_kind")
        return False
    else:
        # get the ranks only from the hand
        for i in range(0, 5):
            a_hand[i] = a_hand[i][0:2]
        temp1 = a_hand[0]
        temp2 = a_hand[1]
        if all(rank == temp1 for rank in a_hand[2:5]) or all(rank == temp2 for rank in a_hand[2:5]):
            return int(a_hand[3])  # also return rank of card
        elif temp1 == temp2:
            c = 2
            for i in range(2, 5):
                if a_hand[i] == temp1:
                    c += 1
            if c == 4:
                return int(a_hand[0])  # also return rank of card
        return False


def has_three_of_kind(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_three_of_kind")
        return False
    else:
        for i in range(0, 5):
            a_hand[i] = a_hand[i][0:2]

        if a_hand[0] == a_hand[1] == a_hand[2]:
            return int(a_hand[0])  # also return rank of card
        elif a_hand[0] == a_hand[1] or a_hand[0] == a_hand[2]:
            for i in range(3, 5):
                if a_hand[i] == a_hand[0]:
                    return int(a_hand[0])  # also return rank of card
        elif a_hand[1] == a_hand[2]:
            for i in range(3, 5):
                if a_hand[i] == a_hand[1]:
                    return int(a_hand[1])  # also return rank of card
        elif a_hand[3] == a_hand[4]:
            for i in range(0, 3):
                if a_hand[i] == a_hand[3]:
                    return int(a_hand[3])  # also return rank of card
        else:
            return False


def has_a_pair(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_a_pair")
        return False
    else:
        for i in range(0, 5):
            a_hand[i] = a_hand[i][0:2]

        to_ret = -1
        one_way_flag = False
        a_hand = sorted(a_hand)
        for i in range(1, 4):
            curr = a_hand[i]
            if curr == a_hand[i-1] and curr == a_hand[i+1]:
                do_nothing = 0
            elif curr == a_hand[i-1] and i == 1:
                return int(a_hand[i])
            elif curr == a_hand[i+1]:
                if i == 3 or (i == 2 and not a_hand[2] == a_hand[4]) or (i == 1 and not a_hand[1] == a_hand[3]):
                    return int(a_hand[i])

        return False


def has_two_pair(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_two_pair")
        return False
    else:
        for i in range(0, 5):
            a_hand[i] = a_hand[i][0:2]

        to_ret = -1
        one_way_flag = False
        for i in range(1, 4):
            curr = a_hand[i]
            if a_hand[i-1] == curr or a_hand[i+1] == curr and not one_way_flag:
                one_way_flag = True
                to_ret = curr
            elif a_hand[i-1] == curr or a_hand[i+1] == curr:
                return max(int(curr), int(to_ret))  # also return rank of cards
        return False


def my_sort(hand):
    if not len(hand) == 5:
        print("Issue, my sort")
        return 0
    else:
        for i in range(len(hand)):
            if hand[i][0] == "T":
                hand[i] = "10" + hand[i][1]
            elif hand[i][0] == "J":
                hand[i] = "11" + hand[i][1]
            elif hand[i][0] == "Q":
                hand[i] = "12" + hand[i][1]
            elif hand[i][0] == "K":
                hand[i] = "13" + hand[i][1]
            elif hand[i][0] == "A":
                hand[i] = "14" + hand[i][1]
            else:
                hand[i] = "0" + hand[i]

    return sorted(hand)


def determine_hand_strength(hand):
    if not len(hand) == 5:
        print("Issue, determine best hand")
        return 0
    else:
        hand = my_sort(hand)
        print(hand)

        flush = has_flush(hand)
        straight = has_straight(hand)
        pow = 8
        if flush > 0 and straight > 0:
            print("straight flush")
            return 100**pow + straight

        pow -= 1
        four = has_four_of_kind(hand)
        if four > 0:
            print("four of a kind")
            return 100**pow + four

        three = has_three_of_kind(hand)
        pair = has_a_pair(hand)
        pow -= 1
        if three > 0 and pair > 0:
            print("full house")
            return 100 ** pow + three
        pow -= 1
        if flush > 0:
            print("flush")
            return 100 ** pow + flush
        pow -= 1
        if straight > 0:
            print("straight")
            return 100 ** pow + straight
        pow -= 1
        if three > 0:
            print ("three of a kind")
            return 100 ** pow + three

        two_pair = has_two_pair(hand)
        pow -= 1
        if two_pair > 0:
            print("two pair")
            return 100 ** pow + two_pair
        pow -= 1
        if pair > 0:
            print("pair")
            return 100 ** pow + pair
        else:
            print("high card")
            return int(hand[4][0:2])


def does_first_win(curr_hand):
    if not (len(curr_hand) == 29):
        print("Issue, does first win")
    else:
        first_hand = curr_hand[0:14].split(' ')

        second_hand = curr_hand[15:29].split(' ')

        print(first_hand, second_hand)

        f = determine_hand_strength(first_hand)
        s = determine_hand_strength(second_hand)
        print(f, s)
        if f > s:
            print("first wins")
            return True
        else:
            print("second wins")
            return False


if __name__ == '__main__':
    hands = open("p054_poker.txt", 'r')
    count = 0

    for line in hands:
        if does_first_win(line[0:29]):
            count += 1

    print(count)

    hands.close()


# SOLVED : 376
