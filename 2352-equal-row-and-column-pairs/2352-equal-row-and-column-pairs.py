class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # Store frequency of each row
        rows = {}

        for row in grid:
            key = tuple(row)
            rows[key] = rows.get(key, 0) + 1

        # Check each column against the rows
        ans = 0

        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))

            if col in rows:
                ans += rows[col]

        return ans