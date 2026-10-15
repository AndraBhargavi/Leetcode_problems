class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        arr=[1]
        current=1
        for c in range(1,rowIndex+1):
            current=current*(rowIndex-c+1)//c
            arr.append(current)
        return arr
        