class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
    
        ctr = [0]*26
        ctr2 = [0]*26
        for ch in s1:
            ctr[ord(ch)-ord("a")] += 1
        for i in range(len(s2)):
            if i >= n:
                ctr2[ord(s2[i - n])-ord("a")] -= 1
            ctr2[ord(s2[i])-ord("a")] += 1

            if all([ctr[i] == ctr2[i] for i in range(26)]):
                return True
        return False
