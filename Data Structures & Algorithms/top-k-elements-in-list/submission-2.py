class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort type
        freq = {}
        buck = [[] for _ in range(len(nums)+1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for n, c in freq.items():
            buck[c].append(n)
        
        res = []
        for i in range(len(buck)-1, -1, -1):
            for num in buck[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res