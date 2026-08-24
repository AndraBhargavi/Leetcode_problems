class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        set1=set()
        for i in nums:
            set1.add(i)
        cnt=1
        maxi=1
        for i in set1:
            x=i
            if x-1 in set1:
                
                continue
            else:
                cnt=1
                while (x+1 in set1):
                    cnt+=1
                    x=x+1
                maxi=max(cnt,maxi)  
        maxi=max(maxi,cnt)
        return maxi

        

