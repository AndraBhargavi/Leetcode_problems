class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(i==self.sum1(nums[i])):
                return i
        return -1
    def sum1(self,num):
        sum1=0
        while num>0:
            sum1+=num%10
            num=num//10
        return sum1
        