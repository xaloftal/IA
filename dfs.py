from collections import deque
import time
from fixedMatrices import *

# verifica se coordenada é valida
def validCoordinates(x, y, matrix):
    rows, cols = len(matrix), len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 0

# algotitmo pesquisa em profundidade
def dfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    parents = {}  # dicionário para guardar os pais de cada ponto
    stackFrontier = deque([(start, None)])  # aqui a gente guarda o ponto e o pai dele

    while stackFrontier:
        (x, y), parent = stackFrontier.popleft()

        # se chegou ao objetivo
        if (x, y) == end:
            # aqui a gente monta o caminho a partir do dicionário de pais
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

if __name__ == "__main__":
    timerS = time.time()
    path = dfs(matrix, start, end)

    if path:
        timerE = time.time()
        print("Caminho encontrado em" + str(timerE - timerS) + ":")
        for point in path:
            print(point)
    else:
        print("Não foi possível encontrar um caminho.")