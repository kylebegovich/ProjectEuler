

memo_red = {0: 0, 1: 0, 2: 1, 3: 2}
memo_green = {0: 0, 1: 0, 2: 0, 3: 1, 4: 2}
memo_blue = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 2}

def red_tiles(num_squares):
    if num_squares in memo_red:
        return memo_red[num_squares]
    else:
        # print("solving red", num_squares)
        to_ret = 1 + red_tiles(num_squares - 1) + red_tiles(num_squares - 2)
        memo_red[num_squares] = to_ret
        return to_ret


def green_tiles(num_squares):
    if num_squares in memo_green:
        # print("green memo", num_squares, memo_green[num_squares])
        return memo_green[num_squares]
    else:
        # print("solving green", num_squares)
        to_ret = 1 + green_tiles(num_squares - 1) + green_tiles(num_squares - 3)
        memo_green[num_squares] = to_ret
        return to_ret


def blue_tiles(num_squares):
    if num_squares in memo_blue:
        # print("blue memo", num_squares, memo_blue[num_squares])
        return memo_blue[num_squares]
    else:
        # print("solving blue", num_squares)
        to_ret = 1 + blue_tiles(num_squares - 1) + blue_tiles(num_squares - 4)
        memo_blue[num_squares] = to_ret
        return to_ret


def num_tiles(num_squares):
    reds = red_tiles(num_squares)
    print("reds =", reds)
    greens = green_tiles(num_squares)
    print("greens =", greens)
    blues = blue_tiles(num_squares)
    print("blues =", blues)
    return reds + greens + blues


# print(red_tiles(5))
# print(green_tiles(5))
# print(blue_tiles(5))

# print(num_tiles(5))
# print(num_tiles(10))
print(num_tiles(50))



# SOLVED : 20492570929
