class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # trouver la bonne longueur
        output = ""
        letters1 = list(word1)
        letters2 = list(word2)
        print(letters1)
        print(letters2)
        for i in range(max(len(word1), len(word2))):
            if letters1 != [] and len(letters1) > i:  
              output = output + letters1[i]
            if letters2 != [] and len(letters2) > i:         
              output = output + letters2[i]
        return output

test1 = "abc"
test2 = "pqr"

sol = Solution()
print(sol.mergeAlternately(test1, test2))