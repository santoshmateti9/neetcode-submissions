class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        final = sorted(people)
        count = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if final[left] + final[right] <= limit:
                count = count + 1
                left = left + 1
                right = right - 1
            elif final[left] + final[right] > limit:
                right = right - 1
                count = count + 1
        return count