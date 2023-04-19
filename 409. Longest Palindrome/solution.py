class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        num_odd = 0
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                num_odd += 1
            else:
                num_odd -= 1
        if num_odd:
            return len(s) - num_odd + 1
        return len(s)