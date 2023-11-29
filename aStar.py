import heapq
import time
from pygame_test import *
from bfs import validCoordinates

def heuristic(node, end):
    return abs(node[0] - end[0]) + abs(node[1] - end[1])

def astar(matrix, start, end, screen, choice):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    parents = {}
    cost_so_far = {}
    frontier = [(0, start)]
    evaluated_nodes = []
    
    while frontier:
        current_cost, (x,y) = heapq.heappop(frontier)

        if (x,y) == end:
            path = []
            while (x,y) is not None:
                path.insert(0, (x,y))
                if (x, y) in parents:
                    (x, y) = parents[(x, y)]
            return path, screen

        if not visited[x][y]:
            visited[x][y] = True
            evaluated_nodes.append((x, y))
            if choice == '2':
                draw_evaluated(evaluated_nodes, screen)

            moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for move in moves:
                new_x, new_y = move
                if validCoordinates(new_x, new_y, matrix) and not visited[new_x][new_y]:
                    new_cost = cost_so_far.get((x, y), 0) + 1  # Assuming a cost of 1 for each step
                    if (new_x, new_y) not in cost_so_far or new_cost < cost_so_far.get((new_x, new_y), float('inf')):
                        cost_so_far[(new_x, new_y)] = new_cost
                        priority = new_cost + heuristic((new_x, new_y), end)
                        heapq.heappush(frontier, (priority, (new_x, new_y)))
                        parents[(new_x, new_y)] = (x, y)

    return None, screen

def astar_path(matrix, start, end):
    timerS = time.time()
    path = astar(matrix, start, end, screen=0, choice=0)

    if path:
        timerE = time.time()
        print("Caminho encontrado em " + str(timerE - timerS)+" ms:")
        for point in path:
            print(point)
    else:
        print("Não foi possível encontrar um caminho.")


def astar_visualization(matrix, start, end, choice):
    pygame.init()
    running = True
    screen = draw_screen(matrix)
    draw_grid(matrix, screen)

    path, screen = astar(matrix, start, end, screen, choice)
    
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