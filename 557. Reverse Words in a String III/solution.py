class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split(' ')  # separate each word
        for i in range(len(split_s)):   # reverse the word
            split_s[i] = split_s[i][::-1]
        output = ' '.join(split_s)  # combine into 1 string separated by ' '
        return output
