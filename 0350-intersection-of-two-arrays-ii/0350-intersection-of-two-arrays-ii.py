class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       freq={}
       for i in nums1:
        freq[i]=freq.get(i,0)+1
       ans=[]
       for i in nums2:
        if freq.get(i,0)>0:
            ans.append(i)
            freq[i]-=1
       return ans

        