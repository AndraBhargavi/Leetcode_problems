class Solution:
    def maxScore(self, s: str) -> int:
        right_ones=0
        left_zeroes=0
        maxi=0
        for i in s:
            if i!='0':
                right_ones+=1
        left=0
        for i in range(len(s)-1):
            if s[i]=='0':
                left+=1
            else:
                right_ones-=1
            
            maxi=max(maxi,left+right_ones)
        return maxi
        