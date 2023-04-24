class Solution:
    cache = {
        0: 0,
        1: 1
    }

    def fib(self, n: int) -> int:
        return self.goldenRatioFib(n)

    def goldenRatioFib(self, n: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** n) / (5 ** 0.5)))

    def matrixExponentiationFib(self, n: int) -> int:
        if n <= 1:
            return n

        a = [[1, 1], [1, 0]]
        self.matrix_power(a, n - 1)

        return a[0][0]

    def matrix_power(self, a: list[list[int]], n: int):
        if n <= 1:
            return a

        self.matrix_power(a, n // 2)
        self.matrix_multiply(a, a)
        b = [[1, 1], [1, 0]]

        if n % 2 != 0:
            self.matrix_multiply(a, b)

    def matrix_multiply(self, a: list[list[int]], b: list[list[int]]) -> None:
        x = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        y = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        z = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        w = a[1][0] * b[0][1] + a[1][1] * b[1][1]

        a[0][0] = x
        a[0][1] = y
        a[1][0] = z
        a[1][1] = w

    def iterativeFibMinSpace(self, n: int) -> int:
        if n <= 1:
            return n

        current = 0
        prev1 = 1
        prev2 = 0

        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current

    def memoizationFib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]

    def tabulationFib(self, n: int) -> int:
        if n <= 1:
            return n

        # bottom-up tabulation
        cache = [0] * (n + 1)
        cache[1] = 1
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]

    def recursiveFib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
