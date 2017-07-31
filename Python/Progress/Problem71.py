goal_numat = 3
goal_denom = 7
best_numat = 0
best_denom = 1
limit = 1000000

for curr_denom in range(limit, 2, -1):
    curr_numat = int((goal_numat * curr_denom - 1) / goal_denom)
    if curr_numat * best_denom > best_numat * curr_denom:
        best_denom = curr_denom
        best_numat = curr_numat

print (best_numat, best_denom)


# SOLVED : 428570
