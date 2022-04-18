import pygame 
import sys
from Generate_with_DFS import *
from DRAW_BOARD import *
from Generate_with_SpanningTree import *
row, column = map(int, input("Введите количество строк и столбцов лабиринта: ").split())
type_of_generate = input("Введите как сгенерировать лабиринт: ")
size_of_cell = 40
width_of_screen = size_of_cell * column
height_of_screen  = size_of_cell * row
delete_walls = []
answer_path = []
pygame.init()
screen = pygame.display.set_mode((width_of_screen, height_of_screen))

if type_of_generate == "DFS":
    delete_walls, answer_path = Generate_with_DFS(row, column)
elif type_of_generate == "SpanningTree":
    delete_walls, answer_path = Generate_with_SpanningTree(row, column)
DRAW_BOARD(screen, width_of_screen, height_of_screen, row, column, size_of_cell, delete_walls, answer_path)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
