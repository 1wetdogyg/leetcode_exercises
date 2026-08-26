class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x 
        num_invertido = 0
        if num > 0:
            num_invertido = int(str(num)[::-1])
        return num == num_invertido
        