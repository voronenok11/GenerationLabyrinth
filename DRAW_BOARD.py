import pygame
def DRAW_BOARD(screen, width_of_screen, height_of_screen, row, column, size_of_cell, delete_walls, answer_path):
     for r in range(row):
         for c in range(column):
             now_rect = pygame.Rect(c * size_of_cell, r * size_of_cell, size_of_cell, size_of_cell)
             pygame.draw.rect(screen, (255, 255, 255), now_rect, 1)
     for walls in delete_walls:
         if walls[0][0] > walls[1][0] or walls[0][1] > walls[1][1]:
             walls[0], walls[1] = walls[1], walls[0]
         pygame.draw.line(screen, (0, 0, 0), (walls[0][1] * size_of_cell + size_of_cell, walls[0][0] * size_of_cell + size_of_cell), (walls[1][1] * size_of_cell, walls[1][0] * size_of_cell), width = 5)
     def centre_of_cell(r, c):
         return ((2 * r + 1) / 2 * size_of_cell, (2 * c + 1) / 2 * size_of_cell)
     for it in range(len(answer_path) - 1):
         pygame.draw.line(screen, (255, 0, 0), centre_of_cell(answer_path[it][1], answer_path[it][0]), centre_of_cell(answer_path[it + 1][1], answer_path[it + 1][0]), width = 5)
