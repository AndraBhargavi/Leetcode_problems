class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[0]*len(nums1)
        
        for i in range(len(nums1)):
            y=self.ls(nums2,nums1[i])
            ans[i]=y
    
        return ans
    def ls(self,nums2,target):
        index=-1
        for i in range(len(nums2)):
            if nums2[i]==target:
                index=i
                break
        for i in range(index+1,len(nums2)):
            if nums2[i]>target:
                return nums2[i]
        return -1
        

                
        