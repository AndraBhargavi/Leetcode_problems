class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n<=1:
            return n
        left=0
        right=1
        maxi=0
        while(right<n):
            if s[right] in s[left:right]:
                maxi=max(maxi,right-left)
                left+=1
            else:
                right+=1
        maxi=max(maxi,right-left)
        return maxi

        