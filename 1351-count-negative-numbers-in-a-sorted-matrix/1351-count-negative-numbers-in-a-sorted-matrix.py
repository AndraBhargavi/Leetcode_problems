class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        sum1=0
        for i in range(n):
            low=0
            high=m-1
            ans=m
            while(low<=high):
                mid=low+(high-low)//2
                if grid[i][mid]>=0:
                    low=mid+1
                else:
                    ans=mid
                    high=mid-1
            sum1+=(m-ans)
        return sum1


        
            