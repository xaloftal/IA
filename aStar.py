import heapq
import time
from pygame_test import *
from bfs import validCoordinates
from collections import deque

class Node:
    def __init__(self, x, y, parent=None, g=0, h=0, ):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = g  # Custo do no inicial ate ao no atual
        self.h = h  # Custo heuristico do no atual ate ao objetivo
        self.move_cost = 1 # Custo do movimento
        self.rotation_cost = 1 # Custo da rotacao

    def total_cost(self): # Custo total do no atual
        return self.g + self.h 

    def __lt__(self, other): # Comparacao do custo total entre dois nos
        return self.total_cost() < other.total_cost()


def heuristic(current_node, goal): # Calculo da heuristica utilizando a distancia de Manhattan
    return abs(current_node[0] - goal[0]) + abs(current_node[1] - goal[1])

def get_neighbors(matrix, node): # Funcao para encontrar nos vizinos
    neighbors = [] 
    x, y = node.x, node.y

    # Check if the potential neighboring node is within the matrix bounds 
    # and is not an obstacle (matrix[new_x][new_y] != 1)

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] != 1:
            neighbors.append(Node(new_x, new_y))

    return neighbors

def construct_path(node):
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
        
    return path[::-1]

def get_direction(current_position, next_position):
    dx = next_position[0] - current_position[0]
    dy = next_position[1] - current_position[1]
    
    if dx == 1:     #(x+1, y)
        return 'right'
    elif dx == -1:  #(x-1, y)
        return 'left'
    elif dy == 1:   #(x, y+1)
        return 'down'
    elif dy == -1:  #(x, y-1)
        return 'up'

def astar(matrix, start, end, screen, choice):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    parents = {}
    cost_so_far = {}
    start_node = Node(start[0], start[1], g=0, h=heuristic(start, end))
    frontier = [(0, start_node)]
    evaluated_nodes = []

    # Imprime a heuristica entre o inicio e o fim
    print("Heuristica entre o inicio {} e o objetivo {}: {}".format(start, end, start_node.h))
    print("\n")

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)
        x, y = current_node.x, current_node.y

        print("Coordenada escolhida:", (x, y))
        print("\n")

        if (x, y) == end:
            path = construct_path(current_node)
            total_cost = cost_so_far.get((x, y), 0)  # Custo total do caminho
            return path, total_cost, screen

        if not visited[x][y]:
            visited[x][y] = True
            evaluated_nodes.append((x, y))

            if choice == '2':
                draw_evaluated(evaluated_nodes, screen)

            for neighbor in get_neighbors(matrix, current_node):
                new_x, new_y = neighbor.x, neighbor.y
                new_cost = cost_so_far.get((x, y), 0) + current_node.move_cost

                if (new_x, new_y) not in cost_so_far or new_cost < cost_so_far.get((new_x, new_y), float('inf')):
                    if (x, y) in parents:
                        current_direction = get_direction(parents[(x, y)], (x, y))
                        new_direction = get_direction((x, y), (new_x, new_y))

                        if current_direction != new_direction:
                            new_cost += current_node.rotation_cost

                    cost_so_far[(new_x, new_y)] = new_cost
                    priority = new_cost + heuristic((new_x, new_y), end)

                    print("Heuristica nas coordenadas ({}, {}): {}".format(new_x, new_y, heuristic((new_x, new_y), end)))
                    
                    heapq.heappush(frontier, (priority, Node(new_x, new_y, current_node)))
                    parents[(new_x, new_y)] = (x, y)
        

    return None, 0, screen

def astar_path(matrix, start, end):
    timerS = time.time()
    path, total_cost, screen = astar(matrix, start, end, screen=0, choice=0)

    if path:
        time.sleep(1)
        timerE = time.time()
        timer = timerE - timerS
        print("Caminho encontrado em " + f"{timer:.8f}" + "s:")
        n = 0
        for point in path:
            print(point)
            n += 1
        print("Steps: " + str(n-1))

        print("Custo total do caminho:", total_cost)

    else:
        print("Não foi possível encontrar um caminho.")

def astar_visualization(matrix, start, end, choice):
    pygame.init()
    running = True
    screen = draw_screen(matrix)
    draw_grid(matrix, screen, start, end)

    path, total_cost, screen = astar(matrix, start, end, screen, choice)
    
    if path:
        print("Caminho encontrado:")
        n = 0
        for point in path:
            print(point)
            n += 1
        print("Steps: " + str(n-1))
        print("Custo total do caminho:", total_cost)
        draw_path(path, screen)
    else:
        print("Caminho não encontrado")

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()