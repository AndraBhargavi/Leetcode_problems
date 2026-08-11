class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float(-inf)
        n=len(nums)
        sum1=0
        for i in range(n):
            sum1+=nums[i]
            maxi=max(sum1,maxi)
            if(sum1<=0):
                sum1=0
            
            
        return maxi
            
        