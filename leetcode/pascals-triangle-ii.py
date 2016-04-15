class Solution:
    # Could you optimize your algorithm to use only O(k) extra space?
    # @return a list of integers
    def getRow(self, rowIndex):
        ans = []
        numRows = rowIndex+1
        for i in range(0,numRows):
            temp = []
            for j in range(0,i+1):
                if i-1>=0 and j-1>=0 and i-1>=j:
                    temp.append(ans[i-1][j-1] + ans[i-1][j])
                else:
                    temp.append(1)
            ans.append(temp) 
        return ans[rowIndex]
