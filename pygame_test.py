import pygame
import sys
import time
import heapq

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

CELL_SIZE = 20

def draw_evaluated(evaluated_nodes, screen): #para colorir os pontos já avaliados
    for x,y in evaluated_nodes:
        pygame.draw.rect(screen, RED, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        pygame.time.delay(50)

def draw_screen (matrix):
    width, height = len(matrix[0]) * CELL_SIZE, len(matrix) * CELL_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Algoritmo A*")

    return screen

def draw_grid(matrix, screen, start, end):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[row][col] == 0:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                
            if (row, col) == start:
                pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif (row, col) == end:
                pygame.draw.rect(screen, YELLOW, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            

def draw_path(path, screen):
    for point in path:
        pygame.draw.rect(screen, GREEN, (point[1] * CELL_SIZE, point[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        pygame.time.delay(10)




