class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in dict1:
                return i,dict1[compliment]
            else:
                dict1[nums[i]]=i
        
        