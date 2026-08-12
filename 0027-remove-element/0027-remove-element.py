class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=-1
        for i in range(len(nums)):
            if nums[i]==val:
                index=i
                break
        if index==-1:
            return len(nums)
        i=index+1
        while(i<len(nums)):
            if nums[i]!=val:
                nums[i],nums[index]=nums[index],nums[i]
                index+=1
                i+=1
            else:
                i+=1
        return index

        