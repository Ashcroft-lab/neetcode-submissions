class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = defaultdict(int)
        for num in nums:
            di[num] += 1
        return [x for x,y in sorted(di.items(), key=lambda num:num[1])][-k:]