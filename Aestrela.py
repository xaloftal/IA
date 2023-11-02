import heapq

class Node:
    def __init__(self, x, y, parent=None, g=0, h=0):
        """
        Initialize a Node with its position, parent node, cost from the start, and heuristic cost.

        :param x: X-coordinate of the node.
        :param y: Y-coordinate of the node.
        :param parent: Parent node.
        :param g: Cost from the start node to this node.
        :param h: Heuristic (estimated) cost from this node to the goal.
        """
        self.x = x
        self.y = y
        self.parent = parent
        self.g = g  # Cost from the start node to this node
        self.h = h  # Heuristic (estimated) cost from this node to the goal

    def f(self):
        """
        Calculate the total cost f, which is the sum of g and h.

        :return: Total cost f.
        """
        return self.g + self.h

    def __lt__(self, other):
        """
        Compare two nodes based on their total costs (f values).

        :param other: Another node for comparison.
        :return: True if this node has a lower total cost (f value) than the other.
        """
        return self.f() < other.f()

def astar(matrix, start, goal):
    """
    Perform the A* search algorithm to find the shortest path in a matrix from the start point to the goal point.

    :param matrix: 2D grid representing the environment with 0 as walkable and 1 as obstacles.
    :param start: Start point (x, y) coordinates.
    :param goal: Goal point (x, y) coordinates.
    :return: A list of (x, y) coordinates representing the path from start to goal, or None if no path is found.
    """
    open_set = []   # Nodes to be evaluated
    closed_set = set()  # Already evaluated nodes

    start_node = Node(start[0], start[1], None, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if (current_node.x, current_node.y) == goal:
            return construct_path(current_node)  # If the goal is reached, return the path.

        closed_set.add((current_node.x, current_node.y))  # Mark the current node as evaluated.

        for neighbor in get_neighbors(matrix, current_node):
            if (neighbor.x, neighbor.y) in closed_set:
                continue  # Skip nodes already evaluated.

            tentative_g = current_node.g + 1  # Assuming a cost of 1 to move to a neighbor.

            if neighbor not in open_set or tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.h = heuristic((neighbor.x, neighbor.y), goal)
                neighbor.parent = current_node

                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    return None  # No path found

def heuristic(point, goal):
    """
    Calculate the heuristic (estimated) cost from a point to the goal using the Manhattan distance.

    :param point: Current point (x, y) coordinates.
    :param goal: Goal point (x, y) coordinates.
    :return: Heuristic cost.
    """
    return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

def get_neighbors(matrix, node):
    """
    Get neighboring nodes that can be reached from the current node.

    :param matrix: 2D grid representing the environment.
    :param node: Current node.
    :return: List of neighboring nodes.
    """
    neighbors = []
    x, y = node.x, node.y
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] != 1:
            neighbors.append(Node(new_x, new_y))
    return neighbors

def construct_path(node):
    """
    Reconstruct the path from the goal node to the start node.

    :param node: Goal node.
    :return: List of (x, y) coordinates representing the path from start to goal.
    """
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    return path[::-1]  # Reverse the path to get it from start to goal.

# Example usage
matrix = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(matrix, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")