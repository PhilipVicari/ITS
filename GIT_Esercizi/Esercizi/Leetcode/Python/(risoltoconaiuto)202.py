class Solution:
    def isHappy(self, n: int) -> bool:
        digits= list(map(int, str(n)))
        quadrati=[]
        while True:
            for N in digits:
                square= N**2
                quadrati.append(square)
                n=sum(quadrati)
            if n == 1:
                return True
            else:
                return False
es_202=Solution()
print(es_202.isHappy(7))