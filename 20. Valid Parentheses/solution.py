from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = deque()
        for ch in s:
            if ch in bracket_map:
                top = stack.pop() if stack else '#'

                if bracket_map[ch] != top:
                    return False
            else:
                stack.append(ch)

        return not stack
