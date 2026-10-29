class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k = k + 1
                i = i + 1
            else:
                i = i + 1
        return k