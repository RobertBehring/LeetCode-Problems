class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
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
