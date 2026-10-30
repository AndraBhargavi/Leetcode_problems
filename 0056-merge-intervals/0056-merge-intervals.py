class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval:interval[0])
        print(intervals)
        ans=[]
        for interval in intervals:
            if not ans or ans[-1][1]<interval[0]:
                ans.append(interval)
            else:
                ans[-1][0]=min(ans[-1][0],interval[0])
                ans[-1][1]=max(ans[-1][1],interval[1])
        return ans
