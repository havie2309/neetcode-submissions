class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            visited.add((row, col))
            q = collections.deque()
            q.append((row, col))
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(rows) and nc in range(cols)
                    and grid[nr][nc] == "1" and (nr, nc) not in visited):
                        visited.add((nr,nc))
                        q.append((nr, nc))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands

        