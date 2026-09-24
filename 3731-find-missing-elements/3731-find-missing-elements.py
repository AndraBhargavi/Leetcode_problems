class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        nums_set=set(nums)
        ans=[]
        for i in range(mini,maxi):
            if i not in nums_set:
                ans.append(i)
        return ans
        