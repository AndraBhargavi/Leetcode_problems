class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hashmap={}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if not stack:
                hashmap[nums2[i]]=-1
            else:
                hashmap[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        print(hashmap)
        ans=[]
        for i in nums1:
            ans.append(hashmap[i])
        return ans
            
