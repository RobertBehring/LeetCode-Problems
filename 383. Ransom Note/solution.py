class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        d = dict()
        for i in range(len(magazine)):
            ch = magazine[i]
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        ransomChars = set(ransomNote)
        for char in ransomChars:
            if char not in d or (d[char] < ransomNote.count(char)):
                return False

        return True