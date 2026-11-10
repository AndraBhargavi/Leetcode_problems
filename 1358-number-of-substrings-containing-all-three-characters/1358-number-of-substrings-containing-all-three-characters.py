class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        n=len(s)
        lastseen=[-1]*3
        for i in range(n):
            lastseen[ord(s[i])-ord('a')]=i
            if lastseen[0]!=-1 and lastseen[1]!=-1 and lastseen[2]!=-1:
                count+=min(lastseen)+1
        return count