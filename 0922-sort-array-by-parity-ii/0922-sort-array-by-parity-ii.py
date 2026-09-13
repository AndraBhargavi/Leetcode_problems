class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        n=len(nums)
        ans=[0]*n
        for num in nums:
            if num%2==0:
                ans[i]=num
                i+=2
            else:
                ans[j]=num
                j+=2
        return ans

        