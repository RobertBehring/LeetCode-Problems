class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo = 1
        hi = len(s) + 1
        while lo + 1 < hi:
            mid = lo + (hi-lo) // 2
            if self.__can_make_valid_substring(s, mid, k):
                lo = mid
            else:
                hi = mid

        return lo


    def __can_make_valid_substring(self, s: str, substring_length: int, k: int):
        freq_map = {}
        max_frequency = 0
        start = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1

            if end + 1 - start > substring_length:
                freq_map[s[start]] -= 1
                start += 1

            max_frequency = max(max_frequency, freq_map[s[end]])
            if substring_length - max_frequency <= k:
                return True

        return False
