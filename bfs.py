from fixedMatrices import *
from randomMatrices import *
import pygame
import sys
import time
 
 
class Node:
    def __init__(self, x, y, parent=None, g=0, h=0): # inicializa o no com as suas coordenadas, o no parente, o custo do inicio ate este no e o custo heuristico(custo do no ate ao objetivo)

        self.x = x # coordenada x do nó
        self.y = y # coordenada y do nó
        self.parent = parent # no parente
 
    
def draw_evaluated(node, screen):
    pygame.draw.rect(screen, RED, (node.y * CELL_SIZE, node.x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    pygame.time.delay(50)    
       
def bfs(matrix, start, goal, rows, cols, screen):
    q = []
    q.append((start))
    visited = set()
    start = True
    prev = [[None for _ in range(cols)] for _ in range(rows)]

    while q:
        row, col = q.pop(0)

        if (row, col) == (goal):
            return prev

        # Verificar vizinhos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = row + dr, col + dc

            if (
                0 <= next_row < rows and
                0 <= next_col < cols and
                not visited[next_row][next_col] and
                matrix[next_row][next_col] != '0'
            ):
                q.append((next_row, next_col))
                visited[next_row][next_col] = True
                draw_evaluated(visited, screen)
                prev[next_row][next_col] = (row, col)

    return None

def reconstructPath(start, goal, prev):
    path = []
    row, col = goal
    while (row, col) != (start[0], start[1]):
        path.append((row, col))
        row, col = prev[row][col]
    path.append(start)
    path.reverse()
    return path


def draw_grid(matrix, screen):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[row][col] == 0:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_path(screen, path_matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if path_matrix[i][j] == 'P':
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GREEN, rect)
                

if __name__ == "__main__":

    # Inicializar o Pygame
    pygame.init()

    # Cores
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    # Tamanho da tela e célula
    CELL_SIZE = 20

    matrix = A
    start = (0,0)
    goal = (4,4)

    # Define the start and goal positions

    # Create the Pygame screen
    width, height = len(matrix[0]) * CELL_SIZE, len(matrix) * CELL_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Breath-Search Pathfinding Visualization")

    # Main loop
    running = True
    draw_grid(matrix, screen)
    path, screen = bfs(matrix, start, goal, len(matrix[0]), len(matrix), screen)

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