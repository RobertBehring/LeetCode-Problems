class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def F(s):
            """From editorial, two pointer"""
            skip = 0
            for x in reversed(s):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))

        # def build(s):
        #     """From editorial, build string"""
        #     ans = []
        #     for c in s:
        #         if c != "#":
        #             ans.append(c)
        #         elif ans:
        #             ans.pop()
        #     return "".join(ans)
        # return build(s) == build(t)

        # def backspace(s: str):
        #     stack = []
        #     for i in range(len(s)):
        #         ch = s[i]
        #         if ch == "#":
        #             if stack:
        #                 stack.pop()
        #         else:
        #             stack.append(ch)
        #     return stack

        # s_stack = backspace(s)
        # t_stack = backspace(t)
        # if s_stack == t_stack:
        #     return True
        # return False
