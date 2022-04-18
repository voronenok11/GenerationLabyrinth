import random
def Generate_with_DFS(row, column):
    delete_walls = []
    queue = []
    queue.append((0, 0))
    used = []
    pred = []
    for i in range(row):
        used.append([])
        pred.append([])
        for j in range(column):
            used[i].append(False)
            pred[i].append((-1, -1))
    start_cell = (0, 0)
    finish_cell = (row - 1, column - 1)
    used[start_cell[0]][start_cell[1]] = True
    neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while len(queue) > 0:
        random.shuffle(neighbours)
        now_cell = queue[-1]
        find_new_cell = False
        for delta in neighbours:
            new_cell = (now_cell[0] + delta[0], now_cell[1] + delta[1])
            if not 0 <= new_cell[0] < row or not 0 <= new_cell[1] < column:
                continue
            if used[new_cell[0]][new_cell[1]]:
                continue
            if now_cell == finish_cell:
                continue
            find_new_cell = True
            pred[new_cell[0]][new_cell[1]] = now_cell
            delete_walls.append([now_cell, new_cell])
            queue.append(new_cell)
            used[new_cell[0]][new_cell[1]] = True
            break
        if not find_new_cell:
            queue.pop()
    answer_path = []
    last_cell = finish_cell
    while last_cell != start_cell:
        answer_path.append(last_cell)
        last_cell = pred[last_cell[0]][last_cell[1]]
    answer_path.append(start_cell)
    answer_path.reverse()
    return delete_walls, answer_path



