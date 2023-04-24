from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Build initial set of rotten oranges
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        queue.append((-1,-1))   # mark round/level i.e ticker of timestamp

        # start rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # finish one round of processing
                minutes_elapsed += 1
                if queue:   # avoid endless loops
                    queue.append((-1,-1))
            else:
                # rotten orange contaminating neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh -= 1
                            # this orange would then contaminate others
                            queue.append((neighbor_row, neighbor_col))
        # return elapsed minutes if no fresh oranges left
        return minutes_elapsed if not fresh else -1
