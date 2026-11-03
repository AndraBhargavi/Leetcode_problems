class Solution:
    def isHappy(self, n: int) -> bool:
        return self.fun(n,[])
    def fun(self,n,seen):
        ans=0
        while n>0:
            ans+=((n%10)**2)
            n=n//10
        if ans in seen:
            
            return False
        seen.append(ans)
        if ans==1:
            return True
        else:
            return self.fun(ans,seen)
        
            

        