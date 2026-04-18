class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for idx in range(len(nums)):
            if nums[idx] in di:
                return [di[nums[idx]], idx]
            di[target-nums[idx]] = idx
    