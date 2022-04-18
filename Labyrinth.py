import pygame 
import sys
import random

row, column = map(int, input("Введите количество строк и столбцов лабиринта: ").split())
type_of_generate = input("Введите как сгенерировать лабиринт: ")
size_of_cell = 40
width_of_screen = size_of_cell * column
height_of_screen  = size_of_cell * row
delete_walls = []
def Generate_with_DFS(row, column):
    delete_walls = []
    queue = []
    queue.append((0, 0))
    used = []
    for i in range(row):
        used.append([])
        for j in range(column):
            used[i].append(False)
    used[0][0] = True
    neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while len(queue) > 0:
        random.shuffle(neighbours)
        now_cell = queue[-1]
        queue.pop()
        for delta in neighbours:
            new_cell = (now_cell[0] + delta[0], now_cell[1] + delta[1])
            if not 0 <= new_cell[0] < row or not 0 <= new_cell[1] < column:
                continue
            if used[new_cell[0]][new_cell[1]]:
                continue
            delete_walls.append([now_cell, new_cell])
            queue.append(new_cell)
            used[new_cell[0]][new_cell[1]] = True
    return delete_walls


def DRAW_BOARD(delete_walls):
    for i in range(row):
        for j in range(column):
            now_rect = pygame.Rect(j * size_of_cell, i * size_of_cell, size_of_cell, size_of_cell)
            pygame.draw.rect(screen, (255, 255, 255), now_rect, 1)
    for walls in delete_walls:
        if walls[0][0] > walls[1][0] or walls[0][1] > walls[1][1]:
            walls[0], walls[1] = walls[1], walls[0]
        pygame.draw.line(screen, (0, 0, 0), (walls[0][1] * size_of_cell + size_of_cell, walls[0][0] * size_of_cell + size_of_cell), (walls[1][1] * size_of_cell, walls[1][0] * size_of_cell), width = 5)


pygame.init()
screen = pygame.display.set_mode((width_of_screen, height_of_screen))

if type_of_generate == "DFS":
    delete_walls = Generate_with_DFS(row, column)
DRAW_BOARD(delete_walls)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
