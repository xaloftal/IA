import time
import timeit
from bfs import validCoordinates
from collections import deque
from matriz30 import *
from matriz50 import *
from pygame_test import *
from aStar import get_direction

# algoritmo pesquisa em profundidade
def dfs(matrix, start, end, screen, choice):
    rows, cols = len(matrix), len(matrix[0]) # tamanho da matriz
    visited = [[False] * cols for _ in range(rows)] # pontos visitados
    parents = {}  # dicionário para guardar os pais de cada ponto
    stackFrontier = deque([(start, None, 0, 0)])  # guardar o ponto e o pai dele
    evaluatedNodes = [] # nos avaliados
    total_cost = 0

    while stackFrontier:
        (x, y), parent, move_cost, rotation_cost = stackFrontier.pop() # elimina o ultimo elemento, o mais recente

        # se chegou ao objetivo
        if (x, y) == end:
            # montar o caminho a partir do dicionário de pais
            path = []
            while (x, y) is not None:
                path.insert(0, (x, y))
                if (x, y) in parents:
                    (x, y, move_cost, rotation_cost) = parents[(x, y)]
                    total_cost += move_cost + rotation_cost  # Atualiza o custo total
                else:
                    break
            return path, total_cost, screen
        
        if not visited[x][y]:
            visited[x][y] = True
            evaluatedNodes.append((x, y))
            
            # caso seja a visualização
            if choice == '2':
                draw_evaluated(evaluatedNodes, screen)

            # aqui a gente gera os movimentos possíveis
            moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for move in moves:
                new_x, new_y = move
                if validCoordinates(new_x, new_y, matrix) and not visited[new_x][new_y]:
                    new_move_cost = 1  # custo do movimento
                    new_rotation_cost = 0  # custo da rotacao se nao houver mudanca de direcao

                    if parent is not None:
                        current_direction = get_direction(parent, (x, y))
                        next_direction = get_direction((x, y), (new_x, new_y))
                        if current_direction != next_direction:
                            new_rotation_cost = 1  # custo da rotacao se houver mudanca de direcao
                    stackFrontier.append(((new_x, new_y), (x, y, new_move_cost, new_rotation_cost), new_move_cost, new_rotation_cost)) # atualiza o pai
                    parents[(new_x, new_y)] = (x, y, new_move_cost, new_rotation_cost)


    # Se não for possível atingir o objetivo
    return None, 0, screen


# versao sem pygame
def dfs_path(matrix, start, end):
    timerS = time.time()
    path, total_cost, screen = dfs(matrix, start, end, screen=0, choice=0)

    if path:
        time.sleep(1)
        timerE = time.time()
        timer = timerE - timerS
            
        with open('outputDFS.txt', 'w') as f:
            sys.stdout = f            
            print("Caminho encontrado em " + f"{timer:.8f}" + "s:")
                # execTime = timeit.timeit(dfs_path, )
            n = 0
            for point in path:
                print(point)
                n += 1
            print("Steps: " + str(n-1))
            print("Custo total do caminho:", total_cost)
            sys.stdout = sys.__stdout__
    else:
        print("Não foi possível encontrar um caminho.")


# pygame
def dfs_visualization(matrix, start, end, choice):
    pygame.init()
    running = True
    screen = draw_screen(matrix)
    draw_grid(matrix, screen, start, end)

    path, total_cost, screen = dfs(matrix, start, end, screen, choice)
    
    if path:
        print("Caminho encontrado:", path)
        print("Custo total do caminho:", total_cost)
        draw_path(path, screen)
    else:
        print("Caminho não encontrado")

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()