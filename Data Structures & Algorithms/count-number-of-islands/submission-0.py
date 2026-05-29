class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        def bfs(x, y):
            q = deque()
            grid[x][y] = '0'
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if (0 > ny or 0 > nx or rows <= nx or cols <= ny or grid[nx][ny] == '0'):
                        continue
                    q.append((nx, ny))
                    grid[nx][ny] = '0'
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    count += 1
        return count


        """
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr > rows or nc > cols):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r,c)
                    count += 1
        return count
        """