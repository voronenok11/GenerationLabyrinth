import random
def Generate_with_SpanningTree(row, column):
    delete_walls = []
    answer_path = []
    parent = []
    rang = []
    edges = []
    start_cell = (0, 0)
    finish_cell = (row - 1, column - 1)
    graph = []
    find_path = False
    for r in range(row):
        parent.append([])
        rang.append([])
        graph.append([])
        for c in range(column):
            parent[r].append((r, c))
            rang[r].append(1)
            graph[r].append([])
    for r in range(row):
        for c in range(column):
            if r + 1 < row:
                edges.append([(r, c), (r + 1, c)])
            if c + 1 < column:
                edges.append([(r, c), (r, c + 1)])
    random.shuffle(edges)
    def find_parent(v):
        if parent[v[0]][v[1]] == v:
            return v
        parent[v[0]][v[1]] = find_parent(parent[v[0]][v[1]])
        return parent[v[0]][v[1]]
    def union(cell1, cell2):
        if rang[cell1[0]][cell1[1]] > rang[cell2[0]][cell2[1]]:
            rang[cell1[0]][cell1[1]] += rang[cell2[0]][cell2[1]]
            parent[cell2[0]][cell2[1]] = cell1
        else:
            rang[cell2[0]][cell2[1]] += rang[cell1[0]][cell1[1]]
            parent[cell1[0]][cell1[1]] = cell2
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
    for edge in edges:
        first_cell = edge[0]
        second_cell = edge[1]
        parent_first_cell = find_parent(first_cell)
        parent_second_cell = find_parent(second_cell)
        if parent_first_cell == parent_second_cell:
            continue
        graph[first_cell[0]][first_cell[1]].append(second_cell)
        graph[second_cell[0]][second_cell[1]].append(first_cell)
        delete_walls.append((first_cell, second_cell))
        union(parent_first_cell, parent_second_cell)
    dfs(start_cell, start_cell)
    return delete_walls, answer_path
