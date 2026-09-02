class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*2*n
        j=0
        for i in range(n):
            ans[j]=nums[i]
            j+=1
        for i in range(n-1,-1,-1):
            ans[j]=nums[i]
            j+=1
        return ans