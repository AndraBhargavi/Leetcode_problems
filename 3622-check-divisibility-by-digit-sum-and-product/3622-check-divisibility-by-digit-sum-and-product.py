class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum=0
        digit_product=1
        original=n
        while n>0:
            digit_sum+=n%10
            digit_product*=n%10
            n=n//10
        sum1=digit_sum+digit_product
        if original<sum1:
            return False
        return original%sum1==0
        