import pygame
import sys
import time
from fixedMatrices import *

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

# Define directions (up, down, left, right)
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class MazeVisualizer:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.cell_width = WIDTH // self.cols
        self.cell_height = HEIGHT // self.rows

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Depth-First Search Visualization")

    def draw_maze(self, current_cell=None, path=None, verified_path=None, end_cell=None):
      self.screen.fill(WHITE)

      for row in range(self.rows):
          for col in range(self.cols):
              color = WHITE
              if self.maze[row][col] == 1:
                  color = BLACK
              elif (row, col) == current_cell:
                  color = RED
              elif (row, col) == end_cell:
                  color = PURPLE
              elif (row, col) in verified_path:
                  color = RED
              elif path and (row, col) in path:
                  if (row, col) != start_cell and (row, col) != end_cell:
                      color = GREEN
              pygame.draw.rect(self.screen, color, (col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height))

      pygame.display.flip()
        

    def visualize_dfs(self, start_cell, end_cell):
        stack = [start_cell]
        visited = set()
        verified_path = set()

        while stack:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            current_cell = stack.pop()
            visited.add(current_cell)

            self.draw_maze(current_cell, path=stack, verified_path=verified_path)

            if current_cell == end_cell:
                verified_path.add(current_cell)
                pygame.time.wait(5000)  # Pause for 5 seconds after reaching the end
                pygame.quit()
                sys.exit()

            for dir in DIRS:
                new_row, new_col = current_cell[0] + dir[0], current_cell[1] + dir[1]

                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and (new_row, new_col) not in visited and self.maze[new_row][new_col] == 0:
                    stack.append((new_row, new_col))
                    visited.add((new_row, new_col))

            pygame.time.delay(100)  # Control the speed of the visualization

            verified_path.add(current_cell)

        print("No path found")
        pygame.quit()
        sys.exit()

# Your existing maze
maze = matrix2530

WIDTH, HEIGHT = 500, 500

# Create maze visualizer
visualizer = MazeVisualizer(maze)

# Define start and end cells
start_cell = (0, 0)
end_cell = (20,20)

# Visualize DFS
visualizer.visualize_dfs(start_cell, end_cell)