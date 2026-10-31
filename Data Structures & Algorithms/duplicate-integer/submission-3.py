class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        result = False
        for i in nums:
            if i in seen:
                result = True
            else:
                seen.append(i)
        return result