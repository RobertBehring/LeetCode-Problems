class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = self.counter(s1)
        windowSize = len(s1)

        for i in range(len(s2)):
            if s2[i] in s1Count:  # inc match
                s1Count[s2[i]] -= 1
            if i >= windowSize and s2[
                i - windowSize] in s1Count:  # dec match leaving window
                s1Count[s2[i - windowSize]] += 1
            if all([s1Count[i] == 0 for i in
                    s1Count]):  # check if all freq == 0
                return True

        return False

    def counter(self, s: str) -> dict:
        d = dict()
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        return d
