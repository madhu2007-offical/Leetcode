
class Solution:
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])

        rows = [sum(row) for row in grid]
        cols = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1

        return count
