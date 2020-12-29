```class Solution:
    def isPalindrome(self, x: int) -> bool:
        abs_x, REV = abs(x), 0
        while abs_x !=0:
            REV = REV * 10 + (abs_x % 10)
            abs_x //= 10
        return True if x == REV else False