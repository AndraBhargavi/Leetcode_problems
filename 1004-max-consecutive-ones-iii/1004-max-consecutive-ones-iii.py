class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        count=0
        left=0
        right=0
        maxi=0
        n=len(nums)
        while(right<n):
            if nums[right]==0:
                count+=1
            if count<=k:
                maxi=max(maxi,right-left+1)
                
            else:
                while count>k:
                    if nums[left]==0:
                        count-=1
                    left+=1
            right+=1
        return maxi
        