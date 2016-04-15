class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        r = len(matrix)
        for i in range(0,r/2):
            for j in range(i,r-i-1):
                t = matrix[i][j]
                matrix[i][j] = matrix[r-j-1][i]
                matrix[r-j-1][i] = matrix[r-i-1][r-j-1]
                matrix[r-i-1][r-j-1] = matrix[j][r-i-1]
                matrix[j][r-i-1] = t
                #print '===='
                #print matrix
        return matrix


c = Solution()
print c.rotate(
    [[1,2,3],
     [4,5,6],
     [7,8,9]])
print c.rotate(
    [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]])
