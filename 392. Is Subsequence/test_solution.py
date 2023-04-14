from unittest import TestCase
import solution

testFunc = solution.Solution().isSubsequence
class TestSolution(TestCase):
    def test_is_subsequence(self):
        testCases = [
            ["abc", "ahbgdc", True],
            ["axc", "ahbgdc", False],
            ["aaaaaa", "bbaaaa", False],
            ["aaaaa", "aaa", False]
        ]
        for test in testCases:
            if testFunc(test[0], test[1]) != test[2]:
                self.fail()
