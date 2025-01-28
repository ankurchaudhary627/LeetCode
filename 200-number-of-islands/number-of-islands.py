class Solution:
    def dfs(self,R,C,grid,i,j, vis):
        if i<0 or i>=R or j<0 or j>=C:
            return 0
        if grid[i][j]=="0":
            return 0
        if vis[i][j]:
            return 0
        vis[i][j]=1
        top = self.dfs(R,C,grid,i-1,j, vis)
        right =self.dfs(R,C,grid,i,j+1, vis)
        bottom=self.dfs(R,C,grid,i+1,j, vis)
        left=self.dfs(R,C,grid,i,j-1, vis)
        if any([top,right,bottom,left]) or grid[i][j]=="1":
            return 1
        return 0
    
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        vis = [[0 for _ in range(c)] for __ in range(r)]
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1" and not vis[i][j]:
                    if self.dfs(r,c,grid,i,j,vis):
                        count+=1
        return count