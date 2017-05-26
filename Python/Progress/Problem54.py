import math

def determine_best_hand(a_hand):
    if not len(a_hand) == 5:
        print("o dere")
    else:
        print("we good for now")
        #  do the hand comparison logic here
        

def does_first_win(curr_hand):
    if not (len(curr_hand) == 29):
        print("wut")
    else:
        first_hand = curr_hand[0:14]
        first_hand = first_hand.split(' ')

        second_hand = curr_hand[15:29]
        second_hand = second_hand.split(' ')

        print(first_hand, second_hand)

        determine_best_hand(first_hand)


if __name__ == '__main__':
    hands = open("poker.txt", 'r')
    count = 0

    for line in hands:
        if (does_first_win(line[0:29])):
            count += 1

    hands.close()
