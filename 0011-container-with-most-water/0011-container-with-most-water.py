class Solution:
    def maxArea(self, nums: List[int]) -> int:
        maxi=0
        left=0
        right=len(nums)-1
        while(left<right):
            area=min(nums[left],nums[right])*(right-left)
            maxi=max(maxi,area)
            if(nums[left]<nums[right]):
                left+=1
            else:
                right-=1
        return maxi
        