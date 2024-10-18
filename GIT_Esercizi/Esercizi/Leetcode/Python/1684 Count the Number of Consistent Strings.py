class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        
        return len(words) - count
es_1684= Solution()
print(es_1684.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))