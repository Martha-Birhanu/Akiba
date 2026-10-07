class Solution:
    def isPalindrome(self, x: int) -> bool:
        num= str(x)
        is_palindrome = True
        for i in range(0, len(num)):
            if num[i] != num[len(num)-(i +1)]:
                is_palindrome = False
                break
        if is_palindrome:
            return True
        else:
            return False