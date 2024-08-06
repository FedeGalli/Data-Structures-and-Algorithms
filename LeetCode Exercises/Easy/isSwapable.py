def is_swapable(start, goal):
    if len(start) != len(goal):
        return False
        
    start_map = {}
    goal_map = {}
    for i in range(len(start)):
        start_map[start[i]] = start_map[start[i]] + 1 if start[i] in start_map else 1
        goal_map[goal[i]] = goal_map[goal[i]] + 1 if goal[i] in goal_map else 1

    dif = 0
    for elem in start_map:
        if elem not in goal_map:
            dif += start_map[elem]
        else:
            dif += abs(start_map[elem] - goal_map[elem])

        print(dif)

    return dif <= 2



print(is_swapable("hello", "lolle"))