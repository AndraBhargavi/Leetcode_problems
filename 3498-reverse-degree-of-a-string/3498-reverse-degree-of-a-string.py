class Solution:
    def reverseDegree(self, s: str) -> int:
        sum1=0
        for i in range(len(s)):
            ch=s[i]
            num=ord('z') - ord(ch) + 1
            sum1=sum1+(num*(i+1))
        return sum1
        