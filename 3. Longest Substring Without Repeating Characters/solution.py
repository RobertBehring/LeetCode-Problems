class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        output = 0
        left = 0
        for right in range(len(s)):
            ch = s[right]
            window = right - left + 1
            if ch not in seen:
                output = max(output, window)
            elif seen[ch] < left:
                output = max(output, window)
            else:
                left = seen[ch] + 1
            seen[ch] = right

        return output
