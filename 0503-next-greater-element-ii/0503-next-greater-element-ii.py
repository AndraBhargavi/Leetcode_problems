class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    ans.append(nums[j])
                    break
            else:
                for j in range(0,i):
                    if nums[j]>nums[i]:
                        ans.append(nums[j])
                        break
                else:
                    ans.append(-1)

        return ans