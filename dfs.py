import time
from bfs import validCoordinates
from collections import deque
from fixedMatrices import *
from pygame_test import *

# algotitmo pesquisa em profundidade
def dfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    parents = {}  # dicionário para guardar os pais de cada ponto
    stackFrontier = deque([(start, None)])  # guardar o ponto e o pai dele

    while stackFrontier:
        (x, y), parent = stackFrontier.pop() # elimina o ultimo elemento, o mais recente

        # se chegou ao objetivo
        if (x, y) == end:
            # montar o caminho a partir do dicionário de pais
            path = []
            while (x, y) is not None:
                path.insert(0, (x, y))
                if (x, y) in parents:
                    (x, y) = parents[(x, y)]
                else:
                    break
            return path

        
        if not visited[x][y]:
            visited[x][y] = True

            # aqui a gente gera os movimentos possíveis
            moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for move in moves:
                new_x, new_y = move
                if validCoordinates(new_x, new_y, matrix) and not visited[new_x][new_y]:
                    stackFrontier.append(((new_x, new_y), (x, y)))  # Atualiza o pai
                    parents[(new_x, new_y)] = (x, y)

    # Se não for possível atingir o objetivo
    return None

# matriz 
matrix = matrix2530
start = (0, 0)
end = (9, 2)

def dfs_path(matrix, start, end):
    timerS = time.time()
    path = dfs(matrix, start, end)

    if path:
        timerE = time.time()
        print("Caminho encontrado em " + str(timerE - timerS)+" ms" + ":")
        for point in path:
            print(point)
    else:
        print("Não foi possível encontrar um caminho.")

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