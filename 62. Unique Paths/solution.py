class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.recUniquePaths(m, n)
        return self.tabulationUniquePaths(m, n)

    def tabulationUniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]

    def recUniquePaths(self, m: int, n: int) -> int:
        # too slow!!!
        if m == 1 or n == 1:
            return 1

        return self.recUniquePaths(m - 1, n) + self.recUniquePaths(m, n - 1)
