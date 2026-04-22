class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = [0]*128
        for ch in t:
            need[ord(ch)] += 1
        ls = 0
        ctr = len(t)
        min_len = float("inf")
        start = 0
        for rs in range(len(s)):
            if need[ord(s[rs])] > 0:
                ctr -= 1
            need[ord(s[rs])] -= 1
            
            while ctr == 0:
                if rs - ls + 1 < min_len:
                    min_len = rs - ls +1
                    start = ls
                need[ord(s[ls])] += 1
                if need[ord(s[ls])] > 0:
                    ctr += 1
                ls += 1
        return "" if min_len == float("inf") else s[start: start+min_len]