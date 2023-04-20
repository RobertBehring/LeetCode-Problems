class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_length = len(grid)
        col_length = len(grid[0])
        m_area = 0
        for row in range(row_length):
            for col in range(col_length):
                if grid[row][col] == 1:
                    m_area = max(self.recBFS(grid, row, col), m_area)

        return m_area

    def recBFS(self, grid, r, c) -> int:
        cur_coord = grid[r][c]

        grid[r][c] = 0

        # recursively color all surrounding blocks
        above = r - 1
        below = r + 1
        left = c - 1
        right = c + 1
        # above
        if above >= 0 and grid[above][c] == 1:
            cur_coord += self.recBFS(grid, above, c)
        # below
        if below < len(grid) and grid[below][c] == 1:
            cur_coord += self.recBFS(grid, below, c)
        # left
        if left >= 0 and grid[r][left] == 1:
            cur_coord += self.recBFS(grid, r, left)
        # right
        if right < len(grid[0]) and grid[r][right] == 1:
            cur_coord += self.recBFS(grid, r, right)

        return cur_coord
