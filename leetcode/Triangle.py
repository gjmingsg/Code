class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        h = len(triangle)
        for y in range(h-1,0,-1):
            l = len(triangle[y])
            for l in range(0,l-1):
                if triangle[y][l]>triangle[y][l+1]:
                    triangle[y-1][l] += triangle[y][l+1]
                else:
                    triangle[y-1][l] += triangle[y][l]
        return triangle[0][0]

a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
c = Solution()
print c.minimumTotal(a) 
