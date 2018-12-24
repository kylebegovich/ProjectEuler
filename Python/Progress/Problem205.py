# imma try doing this one by simulation
from random import random as rand
from math import ceil


def sim_roll(p1_sides, p1_num_dice, p2_sides, p2_num_dice):
    p1_total = 0
    for i in range(p1_num_dice):
        p1_total += ceil(rand() * p1_sides)
        # roll = ceil(rand() * p1_sides)
        # print("p1", roll)
        # p1_total += roll

    p2_total = 0
    for i in range(p2_num_dice):
        p2_total += ceil(rand() * p2_sides)
        # roll = ceil(rand() * p2_sides)
        # print("p2", roll)
        # p2_total += roll

    # print(p1_total, p2_total)
    return p1_total > p2_total


def full_simulation(trials):
    p1_wins = 0
    count = 1
    for x in range(trials):
        for i in range(100000):
            if sim_roll(4, 9, 6, 6):
                p1_wins += 1
        print(p1_wins, p1_wins / (count * 100000), count)
        count += 1

    print(p1_wins / trials)


full_simulation(100000000)

# sim_roll(4, 9, 6, 6)
# print()
# sim_roll(4, 9, 6, 6)
# print()
# sim_roll(4, 9, 6, 6)
