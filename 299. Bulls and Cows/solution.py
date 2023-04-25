class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # return self.mapGetHint(secret, guess)
        return self.editorialGetHint(secret, guess)

    def editorialGetHint(self, secret: str, guess: str) -> str:
        """Solution from LeetCode editorial, one pass map"""
        h = collections.defaultdict(int)
        bulls = cows = 0

        for idx, s in enumerate(secret):
            g = guess[idx]
            if s == g:
                bulls += 1
            else:
                cows += int(h[s] < 0) + int(h[g] > 0)
                h[s] += 1
                h[g] -= 1

        return "{}A{}B".format(bulls, cows)

    def mapGetHint(self, secret: str, guess: str) -> str:
        bulls, cows, = 0, 0
        g_map = dict()
        s_map = dict()

        for i in range(len(guess)):
            s = secret[i]
            g = guess[i]
            if g == s:
                bulls += 1
                continue
            if g in s_map and s_map[g] != 0:
                s_map[g] -= 1
                cows += 1
            elif g in g_map:
                g_map[g] += 1
            else:
                g_map[g] = 1
            if s in g_map and g_map[s] != 0:
                g_map[s] -= 1
                cows += 1
            elif s in s_map:
                s_map[s] += 1
            else:
                s_map[s] = 1

        return f"{bulls}A{cows}B"