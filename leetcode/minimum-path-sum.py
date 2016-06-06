class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None:
            return None
        
        h = len(grid) - 1
        w = len(grid[0]) - 1
        
        i = j =0
        while h>=i:
            j = 0
            while w>=j:
                if i-1>=0:
                    if j-1>=0:
                        if grid[i-1][j]>grid[i][j-1]:
                            grid[i][j] = grid[i][j] + grid[i][j-1]
                           
                        else:
                            grid[i][j] = grid[i][j] + grid[i-1][j]
                            
                    else:
                        grid[i][j] = grid[i][j] + grid[i-1][j]
                        
                else:
                    if j-1>=0:
                        grid[i][j] = grid[i][j] + grid[i][j-1]
                        
                j=j+1
            i=i+1

        return grid[h][w]

            
c = Solution()
print c.minPathSum([[1,2,3],[4,5,6],[7,8,9]])
