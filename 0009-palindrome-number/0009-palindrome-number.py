class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        copy_x=x
        ans=0
        while(x>0):
            n=x%10
            ans=(ans*10)+n
            x=x//10
        return copy_x==ans

        