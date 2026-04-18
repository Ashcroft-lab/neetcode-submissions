class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fs = 0
        for ls in range(len(nums)):
            if nums[ls] != val:
                nums[fs] = nums[ls]
                fs += 1
            ls += 1
        return fs  