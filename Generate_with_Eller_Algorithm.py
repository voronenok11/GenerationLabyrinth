import random
def Generate_with_Eller_Algorithm(row, column):
    delete_walls = []
    answer_path = []
    last_level = [-1] * column
    graph = []
    find_path = False
    start_cell = (0, 0)
    finish_cell = (row - 1, column - 1)
    for r in range(row):
        graph.append([])
        for c in range(column):
            graph[r].append([])
    for r in range(row):
        used = [False] * column
        for c in range(column):
            if last_level[c] != -1:
                used[last_level[c]] = True
        not_used = []
        for c in range(column):
            if not used[c]:
                not_used.append(c)
        for c in range(column):
            if last_level[c] == -1:
                last_level[c] = not_used[-1]
                not_used.pop()
        for c in range(column - 1):
            if last_level[c] == last_level[c + 1]:
                continue
            if random.randint(1, 2) == 2 or r == row - 1:
                delete_walls.append([(r, c), (r, c + 1)])
                old_set = last_level[c + 1]
                for c2 in range(column):
                    if last_level[c2] == old_set:
                        last_level[c2] = last_level[c]
        count_wall = [0] * column
        count_with_down_wall = [0] * column
        for c in range(column):
            count_wall[last_level[c]] += 1
        for c in range(column):
            if r == row - 1:
                continue
            if count_with_down_wall[last_level[c]] == count_wall[last_level[c]] - 1:
                delete_walls.append([(r, c), (r + 1, c)])
            elif random.randint(1, 2) == 1:
                count_with_down_wall[last_level[c]] += 1
                last_level[c] = -1
            else:
                delete_walls.append([(r, c), (r + 1, c)])
    for edge in delete_walls:
        cell1 = edge[0]
        cell2 = edge[1]
        graph[cell1[0]][cell1[1]].append(cell2)
        graph[cell2[0]][cell2[1]].append(cell1)
    def dfs(cell, pred):
        nonlocal find_path
        answer_path.append(cell)
        if cell == finish_cell:
            find_path = True
        else:
            bad_cell = True
            for next_cell in graph[cell[0]][cell[1]]:
                if next_cell == pred:
                    continue
                dfs(next_cell, cell)
                if find_path:
                    bad_cell = False
                    break
            if bad_cell:
                answer_path.pop()
    dfs(start_cell, start_cell)
    return delete_walls, answer_path
