import math

# x**2 = 1 + D*y**2


def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


def solve_for_d(d):
    if is_square(d):
        return -1


if __name__ == '__main__':
    for i in range(3, 68):
        print(i, is_square(i))
