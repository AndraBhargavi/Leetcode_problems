class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n=len(arr)
        sum1=0
        for i in range(0,n):
            for j in range(i,n):
                ans=[]
                for k in range(i,j+1):
                    ans.append(arr[k])
                print(ans)
                if len(ans)%2!=0:
                    sum1+=sum(ans)
        return sum1



        