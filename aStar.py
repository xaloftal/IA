from fixedMatrices import *
import heapq
import pygame
import sys
import time

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

def get_neighbors(matrix, node): # retorna a lista de nos vizinhos que podem ser atingidos pelo no atual

    # matrix representa a matriz; node representa o no atual

    neighbors = []
    x, y = node.x, node.y

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] != 1:
            neighbors.append(Node(new_x, new_y))
    return neighbors

def construct_path(goal): # retorna o caminho encontrado

    path = []
    while goal:
        path.append((goal.x, goal.y))
        goal = goal.parent
    return path[::-1]  # reverte o caminho, para listar as coordenadas do start ate ao goal

def astar(matrix, start, goal): # realiza o algoritmo A* para encontrar o caminho mais curto; retorna a lista de coordenadas que representam o caminho ou nada se não houver caminho

    open_set = []   # numero de nos a serem avaliados
    closed_set = set()  # nos ja avaliados

    start_node = Node(start[0], start[1], None, 0, heuristic(start, goal)) 
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if (current_node.x, current_node.y) == goal:
            return construct_path(current_node)  # se o objetivo for atingido, retorna o caminho

        closed_set.add((current_node.x, current_node.y))  # marca o no atual como avaliado

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

    return None  # nenhum caminho encontrado

# Pygame initialization
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Cell size
CELL_SIZE = 20
def main():

    screen_size = (len(matrix[0]) * CELL_SIZE, len(matrix) * CELL_SIZE)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Algoritmo A*")

    running = True

    # A* algorithm
    path = astar(matrix, start, goal)
    if path:
        print("Caminho encontrado:", path)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(WHITE)
            draw_grid(matrix, screen)
            draw_path(path, screen)

            pygame.display.flip()  # Update the display

        pygame.quit()
        sys.exit()
    else:
        print("Caminho não encontrado")

if __name__ == "__main__":
    main()