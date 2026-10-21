class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        list1=[]
        if m*n==r*c:
            arr=[]
            for a in range(m):
                for k in range(n):
                    arr.append(mat[a][k])
            print(arr)
            index=0
            for i in range(r):
                ans=[]
                for j in range(c):
                    ans.append(arr[index])
                    index+=1
                list1.append(ans)
            return list1
        else:
            return mat


        