class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi=nums[0]
        for i in range(len(nums)):
            if maxi<nums[i]:
                maxi=nums[i]
            mini=self.finding_min(i,nums)
            stability=maxi-mini
            if stability<=k:
                return i
        return -1
    def finding_min(self,i,nums):
        mini=nums[i]
        for j in range(i+1,len(nums)):
            mini=min(mini,nums[j])
        return mini
        