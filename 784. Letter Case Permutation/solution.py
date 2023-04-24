class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Solution from LeetCode user DenysCoder
        Date: 4/24/2023
        Source: "https://leetcode.com/problems/letter-case-permutation/solutions/379928/python-clear-solution/"
        """

        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)

        res = []
        backtrack()
        return res
