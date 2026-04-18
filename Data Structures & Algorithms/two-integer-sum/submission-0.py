class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {target-nums[0]: 0}
        for idx in range(1, len(nums)):
            if nums[idx] in di:
                return [di[nums[idx]], idx]
            di[target-nums[idx]] = idx
    