class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]

            self.sortArray(left)
            self.sortArray(right)

            i = j = k = 0
            while len(left) > i and len(right) > j:
                if left[i] > right[j]:
                    nums[k] = right[j]
                    j += 1
                else:
                    nums[k] = left[i]
                    i += 1
                k += 1
            while len(left) > i:
                nums[k] = left[i]
                i += 1
                k += 1
            while len(right) > j:
                nums[k] = right[j]
                j += 1
                k += 1
        return nums