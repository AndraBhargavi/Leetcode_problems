class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini=nums[0]
        for i in nums:
            mini=min(mini,i)
        ans=0
        for i in nums:
            ans+=abs(mini-i)
        return ans
        