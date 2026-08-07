class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        map1={}
        ans=[]
        for i in nums:
            map1[i]=map1.get(i,0)+1
        for key,value in map1.items():
            if value>n/3:
                ans.append(key)
        return ans
        