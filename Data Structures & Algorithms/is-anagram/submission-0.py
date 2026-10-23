class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1=s.split()
        str2=t.split()
        if len(str1)!=len(str2):
            return False
        return Counter(s) == Counter(t)
        return str1.__eq__(str2)
