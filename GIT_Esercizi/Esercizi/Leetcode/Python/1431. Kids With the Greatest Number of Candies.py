class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        maximum=max(candies)
        for i in candies:
            n= i + extraCandies
            if n >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
    
    
es_1431= Solution()
print(es_1431.kidsWithCandies([2,3,5,1,3], 3))