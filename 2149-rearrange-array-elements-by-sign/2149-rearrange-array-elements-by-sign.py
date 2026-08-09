class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        pos_index=0
        neg_index=1
        for i in nums:
            if i>0:
                ans[pos_index]=i
                pos_index+=2
            if i<0:
                ans[neg_index]=i
                neg_index+=2
        return ans
        

        