class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for num in nums:
            res.append(num* res[-1])
        pref_prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod = pref_prod * res[i]
            pref_prod *= nums[i]
            nums[i] = prod
        
        return nums
