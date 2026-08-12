class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        n=len(nums)
        maxi=0
        if n==0:
            return 0
        last_smallest=nums[0]
        count=1
        i=1
        while(i<n):
            if nums[i]==last_smallest:
                i+=1
            elif nums[i]==last_smallest+1:
                count+=1
                last_smallest=nums[i]
                i+=1
            else:
                maxi=max(maxi,count)
                count=1
                last_smallest=nums[i]
                i+=1
        maxi=max(maxi,count)
            
              
        return maxi


