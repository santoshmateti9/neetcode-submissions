class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=s
        str2 = "".join(reversed(str1))
        str1 = "".join([char for char in str1 if char.isalnum()])
        str2 = "".join([char for char in str2 if char.isalnum()])
        if str1.lower()==str2.lower():
            return True
        else:
            return False