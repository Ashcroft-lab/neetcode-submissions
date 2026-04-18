class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #  count frequency and return max freq
        # time: linear, space linear
        res = count = 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res