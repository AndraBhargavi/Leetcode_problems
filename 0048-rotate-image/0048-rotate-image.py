class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(m):
            self.reverse(matrix[i])
    def reverse(self,matrix):
        left=0
        right=len(matrix)-1
        while(left<=right):
            matrix[left],matrix[right]=matrix[right],matrix[left]
            left+=1
            right-=1

        