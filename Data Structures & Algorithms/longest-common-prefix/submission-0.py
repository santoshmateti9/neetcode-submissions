class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)

        right = strs[-1]
        left = strs[0]

        count = ""

        for i in range(min(len(left),len(right))):
                if left[i] == right[i]:
                    count += left[i]
                else:
                    break
                    
        return count