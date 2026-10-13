class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def bfs(row, col, visited):
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))
            while q:
                r,c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and heights[r][c] <= heights[nr][nc]:
                        visited.add((nr, nc))
                        q.append((nr, nc))


        for row in range(rows):
            bfs(row, 0, pacific)
            bfs(row, cols - 1, atlantic)

        for col in range(cols):
            bfs(0, col, pacific)
            bfs(rows - 1, col, atlantic)
                
        res = []

        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])

        return res

