class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        avg=nums[n//2]
        ans=0
        for i in nums:
            ans+=abs(i-avg)
        return ans
        