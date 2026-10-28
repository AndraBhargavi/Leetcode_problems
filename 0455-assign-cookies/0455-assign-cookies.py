class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
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
                i+=1
        return count


        