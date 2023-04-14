class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Given two strings `s` and `t`, determine if they are isomorphic.

        Two strings `s` and `t` are isomorphic if the characters in `s` can
        be replaced to get `t`.

        All occurrences of a character must be replaced with another
        character while preserving the order of characters. No two
        characters may map to the same character, but a character may map to
        itself.

        :param s:
        :param t:
        :return:
        """
        characters = dict()     # Store previously observed character pairs
        for x in range(len(s)):
            if s[x] not in characters:  # New char in s
                if t[x] in t[0:x]:      # Must be new char in t also
                    return False
                characters[s[x]] = t[x]
            elif characters[s[x]] != t[x]:
                return False
        return True