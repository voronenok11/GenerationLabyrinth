import pygame 
import sys
from Generate_with_DFS import *
from DRAW_BOARD import *
from Generate_with_SpanningTree import *
from Generate_with_Eller_Algorithm import *
Generations = ["DFS", "SpanningTree", "Eller Algorithm"]
positive_answers = ["yes", "y", "yeap", "maybe"]
negative_answers = ["no", "n"]
saved_labyrinths = []
file_with_names_of_saved_files = open("name_of_saved_files", "r")
for line in file_with_names_of_saved_files:
    saved_labyrinths.append(line[:len(line) - 1])
file_with_names_of_saved_files.close()
while True:
    want_to_open_labyrinth = input("Хотите открыть существующий лабиринт: ")
    want_to_open_labyrinth = want_to_open_labyrinth.lower()
    if want_to_open_labyrinth in positive_answers + negative_answers:
        break
    print("Недопустимый ответ. Ответ должен быть положительным:", end=' ')
    print(', '.join(positive_answers), end='')
    print(", или отрицательным:", end=' ')
    print(', '.join(negative_answers), end='')
    print(" в любом регистре")
    print()
if want_to_open_labyrinth in positive_answers:
    while True:
        name_of_file = input("Введите имя файла лабиринта, который хотите открыть: ")
        if name_of_file in saved_labyrinths:
            break
        print("Имя файла с таким лабиринтом не существует.")
        print()
    file_with_labyrinth = open(name_of_file, "r")
    line1 = file_with_labyrinth.readline().split(' ')
    row = int(line1[0])
    column = int(line1[1])
    delete_walls = []
    answer_path = []
    num_of_delete_walls = int(file_with_labyrinth.readline())
    for it in range(num_of_delete_walls):
        line2 = file_with_labyrinth.readline().split(' ')
        line2[3] = line2[3][:len(line2) - 2]
        cell1 = (int(line2[0]), int(line2[1]))
        cell2 = (int(line2[2]), int(line2[3]))
        delete_walls.append([cell1, cell2])
    num_of_cells_in_answer_path = int(file_with_labyrinth.readline())
    for it in range(num_of_cells_in_answer_path):
        line3 = file_with_labyrinth.readline().split(' ')
        cell = (int(line3[0]), int(line3[1]))
        answer_path.append(cell)
else:
    while True:
        row, column = map(int, input("Введите количество строк и столбцов лабиринта: ").split())
        if 1 <= row <= 30 and 1 <= column <= 50:
            break
        print("Недопустимый размер лабиринта. Количество строк лабиринта должно быть от 1 до 30 и количество столбцов от 1 до 50")
        print()
    while True:
        type_of_generate = input("Введите как сгенерировать лабиринт: ")
        if type_of_generate in Generations:
            break
        print("Недопустимый тип генерации. Допустимые типы генерации:", end=' ')
        print(', '.join(Generations))
        print()
    while True:
        want_to_save_labyrinth = input("Хотите сохранить лабиринт: ")
        want_to_save_labyrinth = want_to_save_labyrinth.lower()
        if want_to_save_labyrinth in positive_answers + negative_answers:
            break
        print("Недопустимый ответ. Ответ должен быть положительным:", end=' ')
        print(', '.join(positive_answers), end='')
        print(", или отрицательным:", end=' ')
        print(', '.join(negative_answers), end='')
        print(" в любом регистре")
        print()
    delete_walls = []
    answer_path = []
    if type_of_generate == "DFS":
        delete_walls, answer_path = Generate_with_DFS(row, column)
    elif type_of_generate == "SpanningTree":
        delete_walls, answer_path = Generate_with_SpanningTree(row, column)
    elif type_of_generate == "Eller Algorithm":
        delete_walls, answer_path = Generate_with_Eller_Algorithm(row, column)
    if want_to_save_labyrinth in positive_answers:
        name_of_save_file = input("Введите имя файла, куда сохранить лабиринт: ")
        file_with_names_of_saved_files = open("name_of_saved_files", "a")
        file_with_names_of_saved_files.write(name_of_save_file + "\n")
        file_with_names_of_saved_files.close()
        my_file = open(name_of_save_file, "w+")
        my_file.write(str(row) + ' ' + str(column) + '\n')
        my_file.write(str(len(delete_walls)) + '\n')
        for wall in delete_walls:
            my_file.write(str(wall[0][0]) + ' ' + str(wall[0][1]) + ' ' + str(wall[1][0]) + ' ' + str(wall[1][1]) + '\n')
        my_file.write(str(len(answer_path)) + '\n')
        for cell in answer_path:
            my_file.write(str(cell[0]) + ' ' + str(cell[1]) + '\n')
        my_file.close()

size_of_cell = 40
width_of_screen = size_of_cell * column
height_of_screen  = size_of_cell * row
pygame.init()
screen = pygame.display.set_mode((width_of_screen, height_of_screen))

DRAW_BOARD(screen, width_of_screen, height_of_screen, row, column, size_of_cell, delete_walls, answer_path)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
