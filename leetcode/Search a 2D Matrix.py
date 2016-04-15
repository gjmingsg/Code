class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        bi = 0
        r = len(matrix[0])
        c = len(matrix)
        ei = c * r
        
        while bi < ei:
            mi = (bi+ei)/2
            #print "%d %d %d" %(bi,ei,mi)
            if matrix[mi/r][mi%r]>=target:
                ei = mi
            else:
                bi = mi + 1
        if bi/r>=c:
            return False
        #print "%d %d %d %d"%(bi/r,bi%r,r,bi)
        return matrix[bi/r][bi%r]==target 

c = Solution()
print c.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],3)


print c.searchMatrix([
  [1,1]
],2)

print c.searchMatrix([
  [1]
],2)
