class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ctr = [0]*26
        for i in range(len(s)):
            ctr[ord(s[i])- ord('a')] += 1
            ctr[ord(t[i]) - ord('a')] -= 1
        for x in ctr:
            if x != 0:
                return False
        return True