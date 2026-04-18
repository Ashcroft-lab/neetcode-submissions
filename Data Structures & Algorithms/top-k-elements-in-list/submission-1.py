class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # di = defaultdict(int)
        # for num in nums:
        #     di[num] += 1
        # return [x for x,y in sorted(di.items(), key=lambda num:num[1])][-k:]

        ctr = {}
        for num in nums:
            ctr[num] = ctr.get(num, 0) +1
        pq = []
        for num in ctr.keys():
            heapq.heappush(pq, (ctr[num], num))

            if len(pq) > k:
                heapq.heappop(pq)
        
        res  = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
