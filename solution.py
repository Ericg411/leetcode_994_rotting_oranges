from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        min_time = 0

        def bfs(r, c) -> int:
            fresh = set()
            rotten = set()

            queue = deque()
            queue.append((r, c))
            
            while queue:
                row, col = queue.popleft()
                current = grid[r][c]
                directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
                for (dr, dc) in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] != 0:
                        if grid[r][c] == 1:
                            fresh.add((r, c))
                        elif grid[r][c] == 2:
                            rotten.add((r, c))
                        visited.add((r, c))
                        queue.append((r, c))
            

            print(fresh, rotten)
            if len(rotten) == 0:
                return -1
            return -1 if len(rotten) == 0 else len(rotten) - len(fresh)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] != 0:
                    min_time = max(0, bfs(r, c))
                    
        
        return min_time
