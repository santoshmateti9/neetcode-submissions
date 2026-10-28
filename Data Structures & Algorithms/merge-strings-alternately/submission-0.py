class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        point = 0
        
        lowest = min(len(word1),len(word2))

        while point < lowest:
            result = result + word1[point] + word2[point]
            point = point + 1
        
        if len(word1) > len(word2):
            result = result + word1[point:]
        else:
            result = result + word2[point:]
        
        return result