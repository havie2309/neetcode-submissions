class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = collections.deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            r, c = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))


        