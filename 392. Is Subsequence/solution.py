class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given two strings `s` and `t`, return `true` if `s` is a subsequence
        of `t`, or `false` otherwise.

        A subsequence of a string is a new string that is formed from the
        original string by deleting some (can be none) of the characters
        without disturbing the relative positions of the remaining
        characters. (i.e., `"ace"` is a subsequence of `"abcde"` while
        `"aec"` is not).
        :param s:
        :param t:
        :return:
        """
        lastFound = -1
        for char in s:
            lastFound = t.find(char, lastFound + 1, len(t))
            if lastFound == -1:
                return False
        return True
