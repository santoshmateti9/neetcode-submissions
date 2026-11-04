class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        left = 0
        count = 0
        while left <= len(heights) - 1:
            if heights[left] != expected[left]:
                count = count + 1 
                left = left + 1
            else:
                left = left + 1
        return count