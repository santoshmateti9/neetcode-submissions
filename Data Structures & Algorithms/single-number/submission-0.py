class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        
        for i in range(0,len(nums2) - 1, 2):
            if nums2[i] != nums2[i + 1]:
                return nums2[i]

        return nums2[-1]