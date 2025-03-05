class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        Parole=s.split()
        W_P={}
        for i in range(1, len(Parole)):
            if pattern[i] not in W_P:
                # values() is a set - fast membership testing - O(1) amortized search
                if Parole[i] not in W_P.values(): 
                    W_P[pattern[i]] = Parole[i]
                else:
                    return False
            else:
                if not W_P[pattern[i]] == Parole[i]:
                    return False
        return True

es_290=Solution()
print(es_290.wordPattern("aaa", "aa aa aa aa"))