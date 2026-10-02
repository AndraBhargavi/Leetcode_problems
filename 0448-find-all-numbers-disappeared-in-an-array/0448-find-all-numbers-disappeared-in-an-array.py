class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n=len(nums)
        nums=set(nums)
        ans=[]
        for i in range(1,n+1):
            if i not in nums:
                ans.append(i)
        return ans

        