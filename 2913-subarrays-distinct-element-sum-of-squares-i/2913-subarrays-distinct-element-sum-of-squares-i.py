class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=0
        for i in range(n):
            arr=[]
            for j in range(i,n):
                if nums[j] not in arr:
                    arr.append(nums[j])
                sum1+=(len(arr)**2)
        return sum1
            
        