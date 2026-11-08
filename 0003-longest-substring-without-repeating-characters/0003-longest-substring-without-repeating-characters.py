class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n<=1:
            return n
        map1={}
        left=0
        right=0
        maxi=0
        while(right<n):
           
            if map1.get(s[right],-1)>=left:
                left=map1[s[right]]+1
            map1[s[right]]=right
            maxi=max(maxi,right-left+1)
            right+=1
        
        return maxi


        