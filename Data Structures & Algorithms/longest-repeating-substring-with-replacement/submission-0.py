class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res =0
        ls  = 0
        max_freq = 0
        for rs in range(len(s)):
            count[s[rs]] = count.get(s[rs],0) +1
            max_freq = max(max_freq, count[s[rs]])
            
            while (rs - ls +1) - max_freq > k:
                count[s[ls]] -= 1
                ls += 1
            res = max(res, rs-ls +1)
        return res
