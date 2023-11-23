from fixedMatrices import *

def dfs(start_row, start_col, end_row, end_col, maze, rows, cols):
    stackFrontier = [(start_row, start_col)]
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start_row][start_col] = True

    prev = [[None for _ in range(cols)] for _ in range(rows)]

    while stackFrontier:
        row, col = stackFrontier.pop()

        if (row, col) == (end_row, end_col):
            return prev

        # Verificar vizinhos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = row + dr, col + dc

            if (
                0 <= next_row < rows and
                0 <= next_col < cols and
                not visited[next_row][next_col] and
                maze[next_row][next_col] != '0'
            ):
                stackFrontier.append((next_row, next_col))
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
    return path[::-1]

# matriz a utilizar neste exemplo
maze = matrix2530

# onde o robot inicia
start_row, start_col = 0, 0

# onde esta o objeto
end_row, end_col = 2, 2

rows = len(maze)
cols = len(maze[0])

for i in range(rows):
    for j in range(cols):
        # robot
        if maze[i][j] == 'R':
            start_row, start_col = i, j
        # produto
        if maze[i][j] == 'P':
            end_row, end_col = i, j
            
path = dfs(start_row, start_col, end_row, end_col, maze, rows, cols)

def find_path(start_row, start_col, end_row, end_col, maze, rows, cols):
    prev = dfs(start_row, start_col, end_row, end_col, maze, rows, cols)
    if prev is None:
        print("Caminho não encontrado.")
        return []
    return reconstructPath(start_row, start_col, end_row, end_col, prev)

if __name__ == "__main__":
    path = find_path(start_row, start_col, end_row, end_col, maze, rows, cols)
    
    print(path)
    