class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ls = 0
        rs = len(nums)-1
        mid = ls + (rs - ls)//2
        while ls <= rs:
            if nums[mid] < target:
                ls = mid + 1
            elif nums[mid] > target:
                rs = mid -1
            else:
                return mid
            mid = ls + (rs - ls)//2
        return -1