# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
from collections import Counter
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_count= Counter(s)
        valori = []
        for l, v in s_count.items():
            valori.append(v)
        if len(s) == 1 or s[0] == s[-1]:
            return False
        
        if valori[0] != v:
            return False
        else:
            return True
        
        
        
        
es459= Solution()
print(es459.repeatedSubstringPattern("aaaa"))