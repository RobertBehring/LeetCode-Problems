from unittest import TestCase
import solution

testFunc = solution.Solution().maxSubArray


class TestSolution(TestCase):
    def test(self):
        testCases = [
            [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
            [[-2, 1], 1],
            [[-1, 0, -2], 0],
            [[1], 1]
        ]
        for test in testCases:
            if testFunc(test[0]) != test[1]:
                self.fail(f"\nTest Case:\t\t\t{test[0]}\n"
                          f"Expected Output:\t{test[1]}")
