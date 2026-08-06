class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n*t+1):
            digit_sum=self.sum1(i)
            if(digit_sum%t==0):
                return i


    def sum1(self,mid):
        d_sum=1
        while mid>0:
            n=mid%10
            d_sum*=n
            mid=mid//10
        return d_sum

        