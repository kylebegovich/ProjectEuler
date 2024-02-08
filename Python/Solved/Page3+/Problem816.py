# vaguely implemented the following solution in code: https://www.cs.ubc.ca/~liorma/cpsc320/files/closest-points.pdf 

from itertools import combinations
from Euler import euclidean_dist

START = 290797
MOD = 50515093

def step(n):
    return (n ** 2) % MOD

def get_s_nums(count):
    curr = START
    s_nums = [START]
    for i in range(count):
        next = step(curr)
        s_nums.append(next)
        curr = next
    return s_nums

def get_points(count, s_nums):
    points = []
    for i in range(count):
        n = 2*i
        points.append((s_nums[n], s_nums[n+1]))
    return points

def brute(points):
    combos = combinations(points, 2)
    min_distance = None
    for c in combos:
        dist = euclidean_dist(c[0][0], c[1][0], c[0][1], c[1][1])
        if min_distance is None or dist < min_distance:
            min_distance = dist

    return min_distance

# returns the index, NOT the value (ends up not being used)
def bin_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    while start != end:
        print(start, mid, end)
        if start + 1 == end:
            s_val = arr[start]
            e_val = arr[end]
            if target - s_val < e_val - target:
                return start
            return end
        mid = (start + end) // 2
        val = arr[mid]
        if val == target:
            return mid
        if val < target:
            start = mid
        else:
            end = mid
    return start


def bin_search_tuples(arr, target):
    return bin_search([a[0] for a in arr], target)


def closest_points(points):
    l = len(points)
    if l < 10:
        return points, brute(points)
    
    partition = points[l//2]
    x_partition = partition[0]

    left_points, left_min = closest_points(points[:l//2])
    right_points, right_min = closest_points(points[l//2:])
    sorted_points = left_points + right_points
    min_min = min(left_min, right_min)

    left_window = []
    right_window = []
    for tupe in sorted_points:
        x = tupe[0]

        # left of the window
        if x < x_partition - min_min:
            continue
        
        # in the left half of the window
        if x < x_partition:
            left_window.append(tupe)

        # in the right half of the window
        elif x_partition <= x < x_partition + min_min:
            right_window.append(tupe)

        # right of the window
        elif x >= x_partition + min_min:
            break

    right_sorted = sorted(right_window, key=lambda x: x[1])
    min_distance = min_min
    for p_left in left_window:
        y_midpoint = p_left[1]
        y_max = y_midpoint + min_min
        y_min = y_midpoint - min_min
        vert_box = [p_right for p_right in right_sorted if y_min < p_right[1] < y_max]
        for p_right in vert_box:
            curr_dist = euclidean_dist(p_left[0], p_right[0], p_left[1], p_right[1])
            if curr_dist < min_distance:
                min_distance = curr_dist
    
    return points, min_distance


def main(iters):
    s_nums = get_s_nums(iters*2)
    print("done generating s_nums")
    points = get_points(iters, s_nums)
    print("done generating points")
    points = sorted(points)
    print("done sorting points")
    closest = closest_points(points)
    print(closest[1])  # round it yourself :)
    
# main(14)
# main(200)
main(2000000)
