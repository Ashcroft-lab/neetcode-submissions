class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        ls = rs = 0
        while rs < len(nums):
            while q and nums[q[-1]] < nums[rs]:
                q.pop()
            q.append(rs)

            if ls > q[0]:
                q.popleft()
            
            if (rs+1) >= k:
                res.append(nums[q[0]])
                ls += 1
            rs += 1
        return res