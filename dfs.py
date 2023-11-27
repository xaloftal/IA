from fixedMatrices import *

class Frontier:
    def __init__(self):
        self.frontier = []

    def add(self, node, parent):
        self.frontier.append((node, parent))

    def contains_state(self, state):
        return any(node == state for node, _ in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node, parent = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node, parent

def solve_maze_dfs(maze, start, end):
    frontier = Frontier()  # Use the Frontier class instead of a stack
    visited = set()  # Use a set to keep track of visited nodes.
    search_tree = {}  # A dictionary to represent the search tree.

    # Initialize the frontier with the start node.
    frontier.add(start, None)

    while not frontier.empty():
        current_node, parent = frontier.remove()

        if current_node == end:
            return reconstruct_path(search_tree, start, end)

        if current_node in visited:
            continue

        visited.add(current_node)
        search_tree[current_node] = parent  # Update search tree with the parent of the current node

        neighbors = get_neighbors(maze, current_node)

        for neighbor in neighbors:
            if neighbor not in visited and not frontier.contains_state(neighbor):
                frontier.add(neighbor, current_node)

    return None  # If no path is found.


# ir buscar os vizinhos
def get_neighbors(maze, node):
    neighbors = []
    x, y = node

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '1':
            neighbors.append((new_x, new_y))

    return neighbors


#reconstruir o caminho
def reconstruct_path(search_tree, start, end):
    path = [end]
    current_node = end

    while current_node != start:
        current_node = search_tree[current_node]
        path.append(current_node)

    return list(path)


# matriz a utilizar neste exemplo
maze = matrix2530

# onde o robot inicia
start = (0, 0)

# onde esta o objeto
end = (1, 2)

def dfs_path():
    path = solve_maze_dfs(maze, start, end)
    if path:
        print("Maze solved! Path:")
        for node in path:
            print(node)
    else:
        print("Maze cannot be solved.")
