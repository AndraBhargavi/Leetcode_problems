class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left_sum=0
        right_sum=0
       
        for i in range(0,k):
            left_sum+=cardPoints[i]
        left=k-1
        n=len(cardPoints)
        right=n-1
        maxi=0
        while(left>=-1):
            maxi=max(maxi,left_sum+right_sum)
            left_sum-=cardPoints[left]
            left-=1
            right_sum+=cardPoints[right]
            right-=1
            
        return maxi
        