class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (
                    self.isPalindrome(s, left + 1, right)
                    or
                    self.isPalindrome(s, left, right - 1)
                )
            else:
                left = left + 1
                right = right - 1
        return True

    def isPalindrome(self,s,left,right):
        while left < right:
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
            else :
                return False
        return True