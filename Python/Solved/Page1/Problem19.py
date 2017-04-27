thirty_day_months = [4, 6, 9, 11]


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def next_day(yr, mnth, dy, dow):
    dow = (dow + 1) % 7  # always

    if dy < 28:  # if all we need to increment is the day
        dy += 1
    elif mnth == 12 and dy == 31:   # if we need to roll over the year
        yr += 1
        mnth = 1
        dy = 1
    elif dy == 31:   # max days in a month, roll over month
        mnth += 1
        dy = 1
    elif mnth == 2 and ((dy == 28 and not is_leap_year(yr)) or (dy == 29 and is_leap_year(yr))):
        mnth += 1
        dy = 1
    elif dy == 30 and any(mnth == n for n in thirty_day_months):
        mnth += 1
        dy = 1
    else:
        dy += 1

    return [yr, mnth, dy, dow]


if __name__ == '__main__':
    num_first_sundays = 0

    year = 1901
    month = 1
    day = 1
    day_of_week = 2
    date = [year, month, day, day_of_week]

    while year < 2001:
        if day == 1 and day_of_week == 0:
            num_first_sundays += 1
            print(date)

        date = next_day(year, month, day, day_of_week)
        year = date[0]
        month = date[1]
        day = date[2]
        day_of_week = date[3]

    print(num_first_sundays)


# SOLVED : 171
