class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        m=len(g)
        n=len(s)
        count=0
        i=0
        j=0
        while i<m and j<n:
            if g[i]<=s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count


        