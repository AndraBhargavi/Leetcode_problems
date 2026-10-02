class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        map1={}
        for i in range(len(nums)):
            if nums[i] in map1:
                if abs(map1[nums[i]]-i)<=k:
                    return True
                else:
                    map1[nums[i]]=i
            else:
                map1[nums[i]]=i
        return False

        