class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_length = len(grid)
        col_length = len(grid[0])
        num_islands = 0
        for row in range(row_length):
            for col in range(col_length):
                if grid[row][col] == "1":
                    num_islands += 1
                    self.recBFS(grid, row, col)

        return num_islands

    def recBFS(self, grid, r, c):
        grid[r][c] = "0"

        # recursively color all surrounding blocks
        above = r - 1
        below = r + 1
        left = c - 1
        right = c + 1
        # above
        if above >= 0 and grid[above][c] == "1":
            self.recBFS(grid, above, c)
        # below
        if below < len(grid) and grid[below][c] == "1":
            self.recBFS(grid, below, c)
        # left
        if left >= 0 and grid[r][left] == "1":
            self.recBFS(grid, r, left)
        # right
        if right < len(grid[0]) and grid[r][right] == "1":
            self.recBFS(grid, r, right)

        return
