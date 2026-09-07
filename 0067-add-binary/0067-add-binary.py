class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m=len(a)-1
        n=len(b)-1
        carry=0
        sum1=0
        ans=""
        while(m>=0 or n>=0 or carry):
            sum1=carry
            if m>=0:
                sum1+=int(a[m])
            if n>=0:
                sum1+=int(b[n])
            ans+=str(sum1%2)
            carry=sum1//2
            m-=1
            n-=1
        
        
        return ans[::-1]
            

        