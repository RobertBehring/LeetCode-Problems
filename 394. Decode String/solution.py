class Solution:
    def decodeString(self, s: str) -> str:
        """
        Solution from LeetCode user simkieu
        Date Retrieved: 4/26/23
        Source: https://leetcode.com/problems/decode-string/solutions/87662/python-solution-using-stack/
        """
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
