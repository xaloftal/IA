from fixedMatrices import *
from randomMatrices import *
import pygame

def create_menu():
    print("Quer gerar uma matriz aleatória ou fixa?")
    print("1. Aleatória")
    print("2. Fixa")
    choice = input("Opção:")
    
    if choice == '1':
        m_random = A
        return m_random
    elif choice == '2':
        m_fix = (matrix1030, matrix2530) ###resolver
        return m_fix
        pass
    else:
        print("Opção Inválida!")
    
        
def solve(start_row, start_col):
    q = []
    q.append((start_row, start_col))
    visited = [[False for i in range(cols)] for j in range(rows)]
    visited[start_row][start_col] = True

    prev = [[None for i in range(cols)] for j in range(rows)]
    while len(q) > 0:
        row, col = q.pop(0)
        if m[row][col] == 'E':
            return prev
        
        # Check adjacent cells
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row = row + dr
            next_col = col + dc
            if (
                next_row >= 0 and next_row < rows and
                next_col >= 0 and next_col < cols and
                not visited[next_row][next_col] and
                m[next_row][next_col] != '#'
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

def find_start_and_end(m):
    start_row, start_col, end_row, end_col = 0, 0, 0, 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 'S':
                start_row, start_col = i, j
            elif m[i][j] == 'E':
                end_row, end_col = i, j
    return start_row, start_col, end_row, end_col


def bfs(start_row, start_col, end_row, end_col):
    prev = solve(start_row, start_col)
    if prev is None:
        print("Caminho não encontrado.")
        return []
    return reconstructPath(start_row, start_col, end_row, end_col, prev)

m = [
    ['S', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '.', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['#', '#', '.', '.', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.', '.', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', 'E']
]

rows = len(m)
cols = len(m[0])
start_row = 0
start_col = 0
end_row = 0
end_col = 0

for i in range(rows):
    for j in range(cols):
        if m[i][j] == 'S':
            start_row = i
            start_col = j
        if m[i][j] == 'E':
            end_row = i
            end_col = j



print("Labirinto:")
for row in m:
    print(' '.join(row))

print("\nBuscando um caminho:")

path = bfs(start_row, start_col, end_row, end_col)

if len(path) > 0:
    print("Caminho encontrado:")
    for row, col in path:
        m[row][col] = 'P'
    for row in m:
        print(' '.join(row))
else:
    print("Caminho não encontrado.")
    
# Tamanho da janela e células do labirinto
cell_size = 30
window_width = cols * cell_size
window_height = rows * cell_size

# Inicialização do Pygame

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Labirinto')

# Cores
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def draw_maze(window, m):
    for y, row in enumerate(m):
        for x, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(window, RED, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif cell == 'S':
                pygame.draw.rect(window, GREEN, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif cell == 'E':
                pygame.draw.rect(window, BLUE, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif cell == '.':
                pygame.draw.rect(window, WHITE, (x * cell_size, y * cell_size, cell_size, cell_size))

def draw_path(path):
    for row, col in path:
        pygame.draw.rect(window, YELLOW, (col * cell_size, row * cell_size, cell_size, cell_size))

def main():
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Labirinto')

    # Escolha da matriz
    m = create_menu()
    if m is None:
        return  # Encerra o programa se nenhuma matriz for escolhida

    start_row, start_col, end_row, end_col = find_start_and_end(m)

    
    
    for event in pygame.event.get():
        running = True
        if event.type == pygame.QUIT:
            running = False

    window.fill(WHITE)
    draw_maze(window, m)
    
    path = bfs(start_row, start_col, end_row, end_col)
    if len(path) > 0:
        draw_path(window, path)
    
    pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    