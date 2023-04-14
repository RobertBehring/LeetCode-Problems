from unittest import TestCase
import solution

testFunc = solution.Solution().search

class TestSolution(TestCase):
    def test(self):
        testCases = [
            # INSERT_TEST_CASES_HERE
        ]
        for test in testCases:
            if testFunc(INSERT_ARGS_HERE) != test[INSERT_ANS_IDX_HERE]:
                self.fail()
