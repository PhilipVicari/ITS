# You are given two strings s and t.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Return the letter that was added to t.
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i in s:
                s=s.replace(i, "", 1)
            else:
                return i

es389= Solution()
print(es389.findTheDifference("""  """, """  """))