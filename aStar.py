
from fixedMatrices import *
import heapq
import pygame
import sys
import time
from randomMatrices import *

#CORES

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

class Node:
    def __init__(self, x, y, parent=None, g=0, h=0): # inicializa o no com as suas coordenadas, o no parente, o custo do inicio ate este no e o custo heuristico(custo do no ate ao objetivo)

        self.x = x # coordenada x do nó
        self.y = y # coordenada y do nó
        self.parent = parent # no parente
        self.g = g  # custo do inicio ate este no
        self.h = h  # heuristico (estimado) deste no ate ao objetivo

    def total_cost(self): # retorna a soma de g (custo do inicio ate este no) e h (heuristico (estimado) deste no ate ao objetivo)

        return self.g + self.h

    def __lt__(self, other): #compara dois nos baseados no seu custo total

        # o objeto other e o outro no
        # retorna TRUE se este no tiver um custo total inferior ao outro no

        return self.total_cost() < other.total_cost()

def heuristic(point, goal): # calcula e retorna o custo heuristico (estimado) de uma certa coordenada até ao objetivo (distância de Manhattan)

    # point representa as coordenadas atuais; goal representa as coordenadas do objetivo

    return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

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

def draw_evaluated(node, screen):
    pygame.draw.rect(screen, RED, (node.y * CELL_SIZE, node.x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    pygame.time.delay(50)

def get_neighbors(matrix, node): # retorna a lista de nos vizinhos que podem ser atingidos pelo no atual

    # matrix representa a matriz; node representa o no atual

    neighbors = []
    x, y = node.x, node.y

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy #vetor
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] != 1:
            neighbors.append(Node(new_x, new_y))
    return neighbors

def construct_path(node): # retorna o caminho encontrado

    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    return path[::-1]  # reverte o caminho, para listar as coordenadas do start ate ao goal

def astar(matrix, start, goal,screen): # realiza o algoritmo A* para encontrar o caminho mais curto; retorna a lista de coordenadas que representam o caminho ou nada se não houver caminho

    open_set = []   # numero de nos a serem avaliados
    closed_set = set()  # nos ja avaliados

    start_node = Node(start[0], start[1], None, 0, heuristic(start, goal)) 
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if (current_node.x, current_node.y) == goal:
            return construct_path(current_node), screen  # se o objetivo for atingido, retorna o caminho

        closed_set.add((current_node.x, current_node.y))  # marca o no atual como avaliado
        draw_evaluated(current_node, screen)

        for neighbor in get_neighbors(matrix, current_node):
            if (neighbor.x, neighbor.y) in closed_set:
                continue  # salta nos ja avaliados.

            tentative_g = current_node.g + 1  # assumo o custo de um a ir para um vizinho.

            if neighbor not in open_set or tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.h = heuristic((neighbor.x, neighbor.y), goal)
                neighbor.parent = current_node

                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    return None, screen  # nenhum caminho encontrado

#
#PYGAME
#
CELL_SIZE = 20

matrix = A

# Define the start and goal positions
start = (0, 0)
goal = (10,10)

# Create the Pygame screen
width, height = len(matrix[0]) * CELL_SIZE, len(matrix) * CELL_SIZE
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A* Pathfinding Visualization")

# Main loop
running = True
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