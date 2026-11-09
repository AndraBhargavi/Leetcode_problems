class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        right=0
        maxi=0
        hashi={}
        n=len(fruits)
        while(right<n):
            hashi[fruits[right]]=hashi.get(fruits[right],0)+1
            if len(hashi)>2:
                while len(hashi)>2:
                    hashi[fruits[left]]=hashi[fruits[left]]-1
                    if hashi[fruits[left]]==0:
                        del hashi[fruits[left]]
                    left+=1
            if len(hashi)<=2:
                maxi=max(maxi,right-left+1)
                right+=1
        return maxi