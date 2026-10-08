class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum1=0
        row=0
        for i in range(1,n+1):
            sum1+=i
            if sum1<=n:
                row=i
            else:
                break

        return row

        