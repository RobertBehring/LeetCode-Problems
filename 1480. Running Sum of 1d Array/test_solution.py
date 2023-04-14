from unittest import TestCase
import solution

class TestSolution(TestCase):
    def test_running_sum(self):
        testCase = [1, 2, 3, 4]
        testResult = [1, 3, 6, 10]
        testFunc = solution.Solution()

        self.assertEqual(testFunc.runningSum(testCase), testResult)
