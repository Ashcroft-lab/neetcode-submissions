class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if i step 1 char there will be at max 1 repeating char at a time
        if not s:
            return 0

        res = 1
        ls = 0
        avail = set()
        avail.add(s[0])
        for rs in range(1, len(s)):
            while s[rs] in avail:
                avail.remove(s[ls])
                ls += 1
            avail.add(s[rs])
            res = max(res, rs-ls +1)
        return res