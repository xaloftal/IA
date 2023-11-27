import pygame
import sys
import time
import heapq
from dfs import *
from bfs import *
from aStar import *

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

CELL_SIZE = 20

def draw_evaluated(node, screen): #para colorir os pontos já avaliados
    pygame.draw.rect(screen, RED, (node.y * CELL_SIZE, node.x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    pygame.time.delay(50)

def draw_screen (matrix):

    width, height = len(matrix[0]) * CELL_SIZE, len(matrix) * CELL_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Algoritmo A*")

    return screen

def draw_grid(matrix, screen):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[row][col] == 0:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_path(path, screen):
    for x, y in path:
        pygame.draw.rect(screen, GREEN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        pygame.time.delay(10)

# Main loop

def astar_visualization(matrix, start, goal):
    running = True
    draw_screen(matrix)
    draw_grid(matrix, screen)

    path, screen = astar(matrix, start, goal, screen)
    
    if path:
        print("Caminho encontrado:", path)
        draw_path(path, screen)
    else:
        print("Caminho não encontrado")

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

def bfs_visualization(matrix, start, goal):
    running = True
    draw_screen(matrix)
    draw_grid(matrix, screen)

    path, screen = bfs(matrix, start, goal, screen)
    
    if path:
        print("Caminho encontrado:", path)
        draw_path(path, screen)
    else:
        print("Caminho não encontrado")

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

def dfs_visualization(matrix, start, goal):
    running = True
    draw_screen(matrix)
    draw_grid(matrix, screen)

    path, screen = solve_maze_dfs(matrix, start, goal, screen)
    
    if path:
        print("Caminho encontrado:", path)
        draw_path(path, screen)
    else:
        print("Caminho não encontrado")

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()