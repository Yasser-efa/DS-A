# stack = []
# stack.append("Minecraft")
# stack.append("Skyrim")
# stack.append("Doom")
# stack.append("Borderlands")
# stack.append("FFVII")

# def empty(x):
#   return False if x != [] else True

# print(empty(stack))
class Solution:
    def romanToInt(self, s: str) -> int:
        romanNb = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C":  100,
            "D":  500,
            "M":  1000
        }
        output = 0
        h = False
        for i, c in enumerate(s):
            if h:
                i+=1
            if i+1 < len(s):
                if romanNb[c] >= romanNb[s[i+1]]:
                    output+=romanNb[c]
                    h = False
                else:  
                    output+=(romanNb[s[i+1]]-romanNb[c])
                    h = True
        return output
                
sol = Solution()

print(sol.romanToInt("MCMXCIV"))