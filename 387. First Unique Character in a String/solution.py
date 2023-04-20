class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i in range(len(s)):
            ch = s[i]
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        for i in range(len(s)):
            ch = s[i]
            if d[ch] == 1:
                return i

        return -1
