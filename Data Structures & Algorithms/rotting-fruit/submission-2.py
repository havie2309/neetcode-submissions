class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions: 
                    nr = r + dr
                    nc = c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            if len(q) > 0:
                minutes += 1
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return minutes
        
