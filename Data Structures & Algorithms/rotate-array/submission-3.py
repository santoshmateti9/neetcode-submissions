class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        if k == 0:
            return

        steps = k
        right = len(nums) - 1

        while steps != 0:
            nums.insert(0,nums[right])
            steps -= 1
            
        del nums[-k:]
        return nums