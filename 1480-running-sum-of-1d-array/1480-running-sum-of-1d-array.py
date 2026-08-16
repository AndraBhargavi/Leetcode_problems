class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum=[0]*len(nums)
        index=0
        sum1=0
        for i in nums:
            sum1+=i
            running_sum[index]=sum1
            index+=1
        return running_sum
        