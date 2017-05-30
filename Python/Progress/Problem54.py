import math


def has_flush(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_flush")
        return False
    else:
        temp = a_hand[0][1]
        if all(card[1] == temp for card in a_hand):
            return True  # also return highest card
        else:
            return False


def has_straight(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_straight")
        return False
    else:
        ranks = []
        for card in a_hand:
            ranks.append(card[0])
        for i in range(0, 5):
            r = ranks[i]
            if r == "T":
                ranks[i] = "10"
            elif r == "J":
                ranks[i] = "11"
            elif r == "Q":
                ranks[i] = "12"
            elif r == "K":
                ranks[i] = "13"
            elif r == "A":
                ranks[i] = "14"
        ranks = list(map(int, ranks))
        ranks = sorted(ranks)
        temp = ranks[0]
        for i in range(1, 5):
            if not ranks[i] == temp + 1:
                return False
            else:
                temp += 1
        return True  # also return highest card


def has_four_of_kind(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_four_of_kind")
        return False
    else:
        for i in range(0, 5):
            a_hand[i] = a_hand[i][0]
        temp1 = a_hand[0]
        temp2 = a_hand[1]
        if all(rank == temp1 for rank in a_hand[2:5]) or all(rank == temp2 for rank in a_hand[2:5]):
            return True  # also return rank of card
        elif temp1 == temp2:
            c = 2
            for i in range(2, 5):
                if a_hand[i] == temp1:
                    c += 1
            if c == 4:
                return True  # also return rank of card
        return False


def has_three_of_kind(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_three_of_kind")
        return False
    else:
        for i in range(0, 5):
            a_hand[i] = a_hand[i][0]

        if a_hand[0] == a_hand[1] == a_hand[2]:
            return True  # also return rank of card
        elif a_hand[0] == a_hand[1] or a_hand[0] == a_hand[2]:
            for i in range(3, 5):
                if a_hand[i] == a_hand[0]:
                    return True  # also return rank of card
        elif a_hand[1] == a_hand[2]:
            for i in range(3, 5):
                if a_hand[i] == a_hand[1]:
                    return True  # also return rank of card
        elif a_hand[3] == a_hand[4]:
            for i in range(0, 3):
                if a_hand[i] == a_hand[3]:
                    return True  # also return rank of card
        else:
            return False


def has_a_pair(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_a_pair")
        return False
    else:
        for i in range(0, 5):
            a_hand[i] = a_hand[i][0]

        for i in range(0, 5):
            r = a_hand[i]
            if r == "T":
                a_hand[i] = "10"
            elif r == "J":
                a_hand[i] = "11"
            elif r == "Q":
                a_hand[i] = "12"
            elif r == "K":
                a_hand[i] = "13"
            elif r == "A":
                a_hand[i] = "14"
        ranks = list(map(int, a_hand))
        ranks = sorted(ranks)
        one_way_flag = False
        for i in range(1, 4):
            curr = a_hand[i]
            if a_hand[i-1] == curr or a_hand[i+1] == curr and not one_way_flag:
                one_way_flag = True
            elif a_hand[i-1] == curr or a_hand[i+1] == curr:
                return False  # This is a two-pair
        return one_way_flag  # also return rank of card


def has_two_pair(a_hand):
    if not len(a_hand) == 5:
        print("Issue, has_two_pair")
        return False
    else:
        for i in range(0, 5):
            a_hand[i] = a_hand[i][0]

        for i in range(0, 5):
            r = a_hand[i]
            if r == "T":
                a_hand[i] = "10"
            elif r == "J":
                a_hand[i] = "11"
            elif r == "Q":
                a_hand[i] = "12"
            elif r == "K":
                a_hand[i] = "13"
            elif r == "A":
                a_hand[i] = "14"
        ranks = list(map(int, a_hand))
        ranks = sorted(ranks)
        one_way_flag = False
        for i in range(1, 4):
            curr = a_hand[i]
            if a_hand[i-1] == curr or a_hand[i+1] == curr and not one_way_flag:
                one_way_flag = True
            elif a_hand[i-1] == curr or a_hand[i+1] == curr:
                return True  # also return rank of cards
        return False


def determine_hand_strength(hand):
    if not len(hand) == 5:
        print("Issue, determine best hand")
        return 0
    else:
        hand = sorted(hand)

        flush = has_flush(hand)
        straight = has_straight(hand)

        if flush and straight:
            print("straight flush")

        four = has_four_of_kind(hand)

        if four:
            print("four of a kind")

        three = has_three_of_kind(hand)
        pair = has_a_pair(hand)

        if three and pair:
            print("full house")
        elif flush:
            print("flush")
        elif straight:
            print("straight")
        elif three:
            print ("three of a kind")

        two_pair = has_two_pair(hand)

        if two_pair:
            print("two pair")
        elif pair:
            print("pair")
        else:
            print("high card")



def does_first_win(curr_hand):
    if not (len(curr_hand) == 29):
        print("Issue, does first win")
    else:
        first_hand = curr_hand[0:14].split(' ')

        second_hand = curr_hand[15:29].split(' ')

        print(first_hand, second_hand)

        if determine_hand_strength(first_hand) > determine_hand_strength(second_hand):
            return True
        else:
            return False


if __name__ == '__main__':
    hands = open("poker.txt", 'r')
    count = 0

    for line in hands:
        if does_first_win(line[0:29]):
            count += 1
            print(line)

    print(count)

    hands.close()
