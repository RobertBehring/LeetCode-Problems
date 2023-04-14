from unittest import TestCase
import solution

testFunc = solution.Solution().INSERT_FUNCTION_HERE

class TestSolution(TestCase):
    def test_contains_duplicate(self):
        testCases = [
            # INSERT_TEST_CASES_HERE
        ]
        for test in testCases:
            if testFunc(INSERT_ARGS_HERE) != test[INSERT_ANS_IDX_HERE]:
                self.fail()
