class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum1=0
        n=len(nums)
        for i in range(n):
            mini=nums[i]
            maxi=nums[i]
            for j in range(i,n):
                mini=min(mini,nums[j])
                maxi=max(maxi,nums[j])
                sum1+=(maxi-mini)
        return sum1


        