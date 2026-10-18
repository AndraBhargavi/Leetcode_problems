class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxi=0
        sum1=0
        for i in gain:
            sum1+=i
            maxi=max(maxi,sum1)
        return maxi
        