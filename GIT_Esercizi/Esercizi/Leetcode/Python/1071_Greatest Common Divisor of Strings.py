class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        letters=[]
        for l in str1:
            if l in str2:
                letters.append(l)
                count= letters.count(l)
                if count > 1:
                    letters.remove(l)
            else:
                return ""
        result= ''.join(letters)
        return result
        
                    
            

# tent1=Solution()
# print(tent1.gcdOfStrings("ABCABC", "ABC"))


# tent2=Solution()
# print(tent2.gcdOfStrings("ABABAB", "ABAB"))


# tent3=Solution()
# print(tent3.gcdOfStrings("LEET", "CODE"))

tent3=Solution()
print(tent3.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))