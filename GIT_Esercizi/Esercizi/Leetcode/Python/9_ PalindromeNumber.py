class Solution:
    def isPalindrome(self, x: int) -> bool:
        New_x = list(str(x))
        New_N = New_x[::-1]
        if New_x == New_N:
            return True
        else: 
            return False
        
es9 = Solution()
print(es9.isPalindrome(121))
print(es9.isPalindrome(-121))
print(es9.isPalindrome(10))