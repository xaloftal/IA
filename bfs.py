from fixedMatrices import *
from randomMatrices import *
import pygame
import sys
       
def bfs(start_row, start_col, end_row, end_col, m, rows, cols):
    q = []
    q.append((start_row, start_col))
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start_row][start_col] = True

    prev = [[None for _ in range(cols)] for _ in range(rows)]

    while q:
        row, col = q.pop(0)

        if (row, col) == (end_row, end_col):
            return prev

        # Verificar vizinhos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = row + dr, col + dc

            if (
                0 <= next_row < rows and
                0 <= next_col < cols and
                not visited[next_row][next_col] and
                m[next_row][next_col] != '0'
            ):
                q.append((next_row, next_col))
                visited[next_row][next_col] = True
                prev[next_row][next_col] = (row, col)

    return None

def reconstructPath(start_row, start_col, end_row, end_col, prev):
    path = []
    row, col = end_row, end_col
    while (row, col) != (start_row, start_col):
        path.append((row, col))
        row, col = prev[row][col]
    path.append((start_row, start_col))
    path.reverse()
    return path

m = matrix2530

rows = len(m)
cols = len(m[0])
start_row, start_col, end_row, end_col = 0, 0, 0, 0

for i in range(rows):
    for j in range(cols):
        if m[i][j] == 'R':
            start_row, start_col = i, j
        if m[i][j] == 'P':
            end_row, end_col = i, j

print("Labirinto:")
for row in m:
    print('0'.join(map(str, row)))


print("\nBuscando um caminho:")

# Exemplo de uso
path = bfs(start_row, start_col, end_row, end_col, m, rows, cols)

def find_path(start_row, start_col, end_row, end_col, m, rows, cols):
    prev = bfs(start_row, start_col, end_row, end_col, m, rows, cols)
    if prev is None:
        print("Caminho não encontrado.")
        return []
    return reconstructPath(start_row, start_col, end_row, end_col, prev)

def draw_maze(screen, m, rows, cols):
    for i in range(rows):
        for j in range(cols):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if m[i][j] == '0':
                pygame.draw.rect(screen, BLACK, rect)
            elif m[i][j] == 'R':
                pygame.draw.rect(screen, BLUE, rect)
            elif m[i][j] == 'P':
                pygame.draw.rect(screen, YELLOW, rect)
            elif m[i][j] == 'E':
                pygame.draw.rect(screen, GREEN, rect)

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
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    # Tamanho da tela e célula
    CELL_SIZE = 30
    WINDOW_SIZE = (cols * CELL_SIZE, rows * CELL_SIZE)

    # Configuração da tela
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Labirinto com Pygame')

    # Criar uma matriz para representar o caminho sem modificar a matriz original
    path_matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpar a tela
        screen.fill(WHITE)

        # Encontrar o caminho
        path = find_path(start_row, start_col, end_row, end_col, m, rows, cols)

        # Desenhar o labirinto
        draw_maze(screen, m, rows, cols)

        # Se o caminho foi encontrado, desenhar o caminho sem modificar a matriz original
        if path:
            for row, col in path:
                path_matrix[row][col] = 'P'  # 'P' represents the path step
            draw_path(screen, path_matrix, rows, cols)

        # Atualizar a tela
        pygame.display.flip()

        # Aguardar um curto período para visualização
        pygame.time.delay(200)  # Delay in milliseconds

pygame.quit()