# Title: 1926. Nearest Exit from Entrance in Maze
# Difficulty: Medium
# Problem: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

## Using sets and queues

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(entrance[0], entrance[1], 0)])  # Store (row, col, steps)
        visited = set()
        visited.add(tuple(entrance))  # Mark entrance as visited
        
        while queue:
            row, col, steps = queue.popleft()
            
            # Check if we have reached a valid exit point (excluding the entrance)
            if (row != entrance[0] or col != entrance[1]) and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
                return steps
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                
                # Check if the next cell is within bounds and not a wall, and if it's not visited
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.' and (r, c) not in visited:
                    queue.append((r, c, steps + 1))
                    visited.add((r, c))
