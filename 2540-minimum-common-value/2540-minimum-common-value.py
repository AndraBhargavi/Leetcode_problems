class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        for i in nums1:
            ans=self.b_s(nums2,i)
            if ans!=-1:
                return i
        else:
            return -1
    def b_s(self,nums2,num):
        low=0
        high=len(nums2)-1
        while(low<=high):
            mid=low+(high-low)//2
            if nums2[mid]==num:
                return num
            elif nums2[mid]>num:
                high=mid-1
            else:
                low=mid+1
        return -1
        
        