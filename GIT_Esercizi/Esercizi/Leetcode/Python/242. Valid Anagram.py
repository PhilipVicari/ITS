# Given two strings s and t, return true if t is an anagram
# of s, and false otherwise.
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_Divided= list(t)
        s_Divided= list(s)
        t_Count= Counter(t_Divided)
        s_Count= Counter(s_Divided)
        anagramma = []
        if t_Count != s_Count:
            return False
        if len(t_Divided) != len(s_Divided):
            return False
        for l in t_Divided:
            if l in s_Divided:
                anagramma.append(l)
            else:
                return False
        return True
    
es242= Solution()
print(es242.isAnagram("aacc", "ccac"))