# imma try doing this one by simulation
from random import random as rand
from math import floor
from itertools import product


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



def compress_ways(ways_to_get_val):
    ma = max(ways_to_get_val)
    to_ret = [0] * (ma+1)
    for v in ways_to_get_val:
        to_ret[v-1] += 1

    return to_ret


def make_distro(sides, num_dice):
    # to_ret = [0] * num_dice * sides
    # for i in range(num_dice * sides):
    #     for die in range(num_dice):
    #         for side in range(sides):
    dice = []
    for i in range(num_dice):
        dice.append(list(range(1, sides+1)))
    # print(dice)
    prod = product(*dice)
    ways = []
    app = ways.append
    for tupe in prod:
        app(sum(tupe))

    return compress_ways(ways)


# WRONG after compress ways structure
def better_sim_roll(distro1, distro1_len, distro2, distro2_len):
    return distro1[floor(rand() * distro1_len)] > distro2[floor(rand() * distro2_len)]

# WRONG after compress ways structure
def full_simulation(trials):
    p1_wins = 0
    count = 1
    distro1 = make_distro(4, 9)
    distro1_len = len(distro1)
    distro2 = make_distro(6, 6)
    distro2_len = len(distro2)
    for x in range(trials):
        for i in range(1000000):
            if better_sim_roll(distro1, distro1_len, distro2, distro2_len):
                p1_wins += 1
        print(p1_wins, p1_wins / (count * 1000000), count)
        count += 1


    print(p1_wins / trials)


def calc_wins(distro1, distro2):
    p1_wins = 0
    l1 = len(distro1)
    l2 = len(distro2)
    for i in range(l1):
        for j in range(l2):
            if i > j:
                p1_wins += distro1[i] * distro2[j]

    return p1_wins


distro1 = make_distro(4, 9)
distro2 = make_distro(6, 6)
# print(distro1)
# print(distro2)
wins = calc_wins(distro1, distro2)
ways = 4**9 * 6**6
print(wins, ways, wins/ways)
