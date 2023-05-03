rom_to_int = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

class Solution:
    def romanToInt(self, s: str) -> int:
        # return self.homebrew(s)
        # return self.leftToRight(s)
        # return self.leftToRightImproved(s)
        return self.rightToLeft(s)


    def rightToLeft(self, s: str) -> int:
        total = rom_to_int.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if rom_to_int[s[i]] < rom_to_int[s[i + 1]]:
                total -= rom_to_int[s[i]]
            else:
                total += rom_to_int[s[i]]
        return total


    def leftToRightImproved(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in rom_to_int:
                total += rom_to_int[s[i:i+2]]
                i += 2
            else:
                total += rom_to_int[s[i]]
                i += 1
        return total


    def leftToRight(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and rom_to_int[s[i]] < rom_to_int[s[i + 1]]:
                total += rom_to_int[s[i + 1]] - rom_to_int[s[i]]
                i += 2
            else:
                total += rom_to_int[s[i]]
                i += 1
        return total


    def homebrew(self, s: str) -> int:
        prev = s[-1]
        output = rom_to_int[prev]
        for i in range(len(s)-2, -1, -1):
            cur = s[i]
            if (cur == "I" and prev in ["V","X"]) or \
               (cur == "X" and prev in ["L","C"]) or \
               (cur == "C" and prev in ["D","M"]):
               output -= rom_to_int[cur]
            else:
                output += rom_to_int[cur]
            prev = s[i]

        return output
