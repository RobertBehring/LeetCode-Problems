class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s: str):
            stack = []
            for i in range(len(s)):
                ch = s[i]
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack

        s_stack = backspace(s)
        t_stack = backspace(t)
        if s_stack == t_stack:
            return True
        return False
