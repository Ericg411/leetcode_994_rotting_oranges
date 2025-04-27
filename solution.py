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

            total = 0

            queue = deque()
            queue.append((r, c))
            
            while queue:
                row, col = queue.popleft()
                current = grid[row][col]
                print(current)
                directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
                rottable = False
                for (dr, dc) in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] != 0:
                        if grid[r][c] == 1:
                            fresh.add((r, c))
                            if len(rotten) > 0:
                                rottable = True
                        elif grid[r][c] == 2:
                            rotten.add((r, c))
                        visited.add((r, c))
                        queue.append((r, c))
                print(rottable, len(rotten))
                if rottable:
                    total += 1
            print(total, len(rotten), len(fresh))
            return total if len(rotten) > 0 else -1 
                
            if len(rotten) == 0:
                return -1
            return -1 if len(rotten) == 0 else len(rotten) - len(fresh)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] != 0:
                    res = bfs(r, c)
                    if res == -1 and grid[r][c] != 2:
                        return -1
                    else:
                        min_time = max(min_time, res)
                    
        
        return min_time
