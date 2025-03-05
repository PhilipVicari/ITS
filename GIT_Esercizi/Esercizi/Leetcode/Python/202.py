class Solution:
    def isHappy(self, n: int) -> bool:
        # Funzione per calcolare la somma dei quadrati delle cifre
        def sum_of_squares(num):
            total = 0
            for digit in str(num):
                total += int(digit) ** 2
            return total

        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)

        return n == 1
es_202=Solution()
print(es_202.isHappy(7))