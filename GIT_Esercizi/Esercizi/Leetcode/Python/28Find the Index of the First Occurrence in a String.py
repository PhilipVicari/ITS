class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            needle_list= list(needle)
            haystack_list= list(haystack)
            for l in haystack_list:
                if l == needle_list[0]:
                    return haystack_list.index(l)
        else:
            return -1
es_28=Solution()
print(es_28.strStr("mississippi", "issip"))