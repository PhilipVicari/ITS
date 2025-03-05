class Solution:
    def longestCommonPrefix(self, words: list[str]) -> str:
        list_word=[]
        strs=[]
        for w in words:
            new_w=list(w)
            list_word.append(new_w)
        for l in new_w:
            if l in list_word[1]:
                strs.append(l)
        return str(strs)
es_14=Solution()
print(es_14.longestCommonPrefix(["flower","flow","flight"]))
