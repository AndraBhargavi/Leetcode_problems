class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n=len(nums)
        set1=set(nums)
        m=len(set1)
        print(n,m)
        return n!=m
        