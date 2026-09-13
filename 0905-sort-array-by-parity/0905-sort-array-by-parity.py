class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        i=0
        j=len(nums)-1
        for num in nums:
            if num%2==0:
                ans[i]=num
                i+=1
            else:
                ans[j]=num
                j-=1
        return ans
        