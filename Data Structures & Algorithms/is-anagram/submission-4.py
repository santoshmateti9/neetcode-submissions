class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        so = sorted(s)
        to = sorted(t)
        Flag = True
        if len(so) != len(to):
            return False
        for i in range(min(len(so),len(to))):
            if so[i] != to[i]:
                Flag = False
        return Flag