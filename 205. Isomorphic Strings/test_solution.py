from unittest import TestCase
import solution

testFunc = solution.Solution().isIsomorphic


class TestSolution(TestCase):
    def test_is_isomorphic(self):
        testCases = [
            ["egg", "add", True],
            ["foo", "bar", False],
            ["paper", "title", True],
            ["a", "a", True],
            ["a", "z", True],
            ["flute", "moliu", True],
            ["fooooo", "barroo", False],
            ["badc", "baba", False]
        ]
        for test in testCases:
            if testFunc(test[0], test[1]) != test[2]:
                self.fail()

        # self.assertEqual(testFunc(s, t), result)
