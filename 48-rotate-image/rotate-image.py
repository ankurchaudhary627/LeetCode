class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top=0
        N=len(matrix)
        bottom=N-1
        while top<bottom:
            for c in range(N):
                matrix[top][c],matrix[bottom][c]=matrix[bottom][c],matrix[top][c]
            top+=1
            bottom-=1
        for i in range(N):
            for j in range(i+1,N):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]