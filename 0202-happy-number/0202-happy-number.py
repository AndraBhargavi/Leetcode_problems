class Solution:
    def isHappy(self, n: int) -> bool:
        if self.fun(n,[])==1:
            
            return True
        else:
            return False
    def fun(self,n,seen):
        ans=0
        while n>0:
            ans+=((n%10)**2)
            n=n//10
        if ans in seen:
            
            return ans
        seen.append(ans)
        if ans==1:
            return ans
        else:
            return self.fun(ans,seen)
        
            

        