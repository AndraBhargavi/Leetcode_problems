class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval:interval[1])
        end_time=float(-inf)
        count=0
        for start,end in intervals:
            if start>=end_time:
                end_time=end
            else:
                count+=1
        return count