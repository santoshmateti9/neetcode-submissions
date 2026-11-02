class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip()
        last = len(new) - 1
        count = 0    
        while last >= 0 and new[last] != " ":
            last = last - 1
            count = count + 1
        return count