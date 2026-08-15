class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        psee=self.findPSEE(nums)
        nse=self.findNSE(nums)
        pgee=self.findPGEE(nums)
        nge=self.findNGE(nums)
        min_sum=0
        max_sum=0
        for i in range(len(nums)):
            min_left=i-psee[i]
            min_right=nse[i]-i
            min_sum=min_sum+(min_left*min_right*nums[i])
            max_left=i-pgee[i]
            max_right=nge[i]-i
            max_sum=max_sum+(max_left*max_right*nums[i])
        return max_sum-min_sum

    def findPSEE(self,arr):
        pse=[-1]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                pse[i]=stack[-1]
            stack.append(i)
        return pse
    def findPGEE(self,arr):
        pge=[-1]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            if stack:
                pge[i]=stack[-1]
            stack.append(i)
        return pge
    def findNGE(self,arr):
        nge=[len(arr)]*len(arr)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if stack:
                nge[i]=stack[-1]
            stack.append(i)
        return nge
    def findNSE(self,arr):
        nse=[len(arr)]*len(arr)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1]
            stack.append(i)
        return nse



