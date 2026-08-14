class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse=self.findNSE(arr)
        psee=self.findPSEE(arr)
        total=0
        MOD=10**9+7
        for i in range(len(arr)):
            left=i-psee[i]
            right=nse[i]-i
            total=(total+(left*right*arr[i]))%MOD
        return total
    def findNSE(self,arr):
        n=len(arr)
        nse=[n]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1]
            stack.append(i)
        return nse
    def findPSEE(self,arr):
        n=len(arr)
        psee=[-1]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                psee[i]=stack[-1]
            stack.append(i)
        return psee
       

        