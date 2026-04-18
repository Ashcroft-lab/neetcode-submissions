class Solution:

    def match_chars(self, s, t):
        if len(s) != len(t):
            return False

        di = {}
        for idx in range(len(s)):
            di[s[idx]] = di.get(s[idx], 0) + 1
            di[t[idx]] = di.get(t[idx], 0) - 1

        for ch in di.values():
            if ch != 0:
                return False
        return True
            

    def isAnagram(self, s: str, t: str) -> bool:
        return self.match_chars(s, t)