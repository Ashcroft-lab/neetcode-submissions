class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max_pile = max(piles)
        # n = len(piles)

        ls, rs = 1, max(piles)
        res = rs

        while ls <= rs:
            k = (ls+rs) // 2
            tt = 0
            for p in piles:
                tt += math.ceil(float(p) / k)
            if tt <= h:
                res = k
                rs = k-1
            else :
                ls = k+1
                
        return res
