class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        sum1=0
        for key,value in freq.items():
            if value%k==0:
                sum1+=(key*value)
        return sum1

        