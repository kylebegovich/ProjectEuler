
def main():
    """brute forcing this was unsuccessful
    there's a fancy diophantine solution generator online (https://www.alpertron.com.ar/QUAD.HTM) that helped me out"""

    b = 15
    n = 21
    goal = 1000000000000

    while n < goal:
        next_b = 3 * b + 2 * n - 2
        next_n = 4 * b + 3 * n - 3

        b = next_b
        n = next_n

    print(b)

main()


# SOLVED : 756872327473
