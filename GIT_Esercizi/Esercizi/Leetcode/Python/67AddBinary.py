class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]

es67=Solution()
print(es67.addBinary("11", "1"))