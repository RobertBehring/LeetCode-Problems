from unittest import TestCase
import solution

testFunc = solution.Solution().pivotIndex


class TestSolution(TestCase):
    def test_pivot_index(self):
        testCase = [1, 7, 3, 6, 5, 6]
        testSolution = 3

        self.assertEqual(testFunc(testCase), testSolution)
