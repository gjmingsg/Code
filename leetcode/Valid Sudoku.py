class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        self.board = board
        for i in range(0,9):
            if self.rule1(i)==False:
                return False
        for i in range(0,9):
            if self.rule2(i)==False:
                return False
        for i in range(0,7,3):
            for j in range(0,7,3):
                if self.rule3(i,j)==False:
                    return False
        return True
    def rule1(self,i):
        dic={}
        for item in self.board[i]:
            if item=='.':
                continue
            if dic.has_key(item):
                return False
            else:
                dic[item]=1
        return True
            
    def rule2(self,j):
        dic={}
        for item in self.board:
            if item[j]=='.':
                continue
            if dic.has_key(item[j]):
                return False
            else:
                dic[item[j]]=1
        return True

    def rule3(self,i,j):
        dic={}
        for xi in range(i,i+3):
            for yj in range(j,j+3):
                if self.board[xi][yj]=='.':
                    continue
                if dic.has_key(self.board[xi][yj]):
                    return False
                else:
                    dic[self.board[xi][yj]]=1
        return True
