class Solution:
    def romanToInt(self, s: str) -> int:
        Roman={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans=0
        
        for i in range(len(s)):
            if i < len(s) - 1 and Roman[s[i]] < Roman[s[i+1]]:
                ans -= Roman[s[i]]
            else:
                ans += Roman[s[i]]
        
        return ans
numero=Solution()
print(numero.romanToInt("MCMXCIV"))
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        listed= list(str(s))
        var= 0
        i = 0
        while listed != "" and i < len(listed):
            if listed[0] == "I":
                var+=1
                listed.remove(listed[0])
            elif listed[0] == "V":
                var+= 5
                listed.remove(listed[0])
            elif listed[0] == "X":
                var+= 10
                listed.remove(listed[0])
            elif listed[0] == "L":
                var+= 50
                listed.remove(listed[0])
            elif listed[0] == "C":
                var+= 100
                listed.remove(listed[0])
            elif listed[0] == "D":
                var+= 500
                listed.remove(listed[0])
            elif listed[0] == "M":
                var+= 1000
                listed.remove(listed[0])
        return var

numero=Solution()
print(numero.romanToInt("MV"))
"""