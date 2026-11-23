class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0 
        right = len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            else:
                mid += 1
        return nums