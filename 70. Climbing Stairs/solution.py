class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.bruteClimbStairs(0, n)
        return self.fibIterClimbStairs(n)

    def bruteClimbStairs(self, i: int, n: int) -> int:
        if i > n:
            return 0
        if i == n:
            return 1

        return self.bruteClimbStairs(i + 1, n) + self.bruteClimbStairs(i + 2,
                                                                       n)

    def fibIterClimbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        third = 0
        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second
