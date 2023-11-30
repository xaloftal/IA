from collections import deque
import time
from fixedMatrices import *
from pygame_test import *

# verifica se coordenada é valida
def validCoordinates(x, y, matrix):
    rows, cols = len(matrix), len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 0

# algoritmo pesquisa em largura (BFS)
def bfs(matrix, start, end, screen, choice):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    parents = {}  # dicionário para guardar os pais de cada ponto
    queueFrontier = deque([(start, None)])  # aqui guarda o ponto e o pai dele
    evaluated_nodes = []

    while queueFrontier:
        (x, y), parent = queueFrontier.popleft()

        # se chegou ao objetivo
        if (x, y) == end:
            # aqui monta o caminho a partir do dicionário de pais
            path = []
            while (x, y) is not None:
                path.insert(0, (x, y))
                if (x, y) in parents:
                    (x, y) = parents[(x, y)]
                else:
                    break
            return path, screen 

        if not visited[x][y]:
            visited[x][y] = True
            evaluated_nodes.append((x, y))  # Armazenar o nó visitado
            if choice == '2':
                draw_evaluated(evaluated_nodes, screen)  # desenha os nós visitados

            # gera os movimentos possíveis
            moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for move in moves:
                new_x, new_y = move
                if validCoordinates(new_x, new_y, matrix) and not visited[new_x][new_y]:
                    queueFrontier.append(((new_x, new_y), (x, y)))  # Atualiza o pai
                    parents[(new_x, new_y)] = (x, y)

    # Se não for possível atingir o objetivo
    return None, screen


# versão sem o pygame
def bfs_path(matrix, start, end):

    timerS = time.time()
    path, screen = bfs(matrix, start, end, screen=0, choice=0)

    if path:
        timerE = time.time()
        print("Caminho encontrado em", str(timerE - timerS) + "s:")
        n = 0
        for point in path:
            n += 1
            print(point)
            print("\nSteps: " + n)
    else:
        print("Não foi possível encontrar um caminho.")


# versão com o pygame
def bfs_visualization(matrix, start, end, choice):
    pygame.init()
    running = True
    screen = draw_screen(matrix)
    draw_grid(matrix, screen, start, end)

    path, screen = bfs(matrix, start, end, screen, choice)
    
    if path:
        print(path)
        draw_path(path, screen)
    else:
        print("Caminho não encontrado")

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
