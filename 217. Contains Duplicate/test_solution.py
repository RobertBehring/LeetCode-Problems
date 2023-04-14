from unittest import TestCase
import solution

testFunc = solution.Solution().containsDuplicate


class TestSolution(TestCase):
    def test_contains_duplicate(self):
        testCases = [
            [[1, 2, 3, 1], True],
            [[1, 2, 3, 4], False],
            [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True]
        ]
        for test in testCases:
            if testFunc(test[0]) != test[1]:
                self.fail()
