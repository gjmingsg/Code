class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        s = []
        
        for i in range(0,len(board)):
            b = []
            for j in range(0,len(board[0])):
                b.append(1)
            s.append(b)
        #print s
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j]==word[0] and self.seach(board,i,j,word,1,s)):
                    return True
        return False
    
    def seach(self,board,i,j,word,k,s):
        if k==len(word):
            return True
        s[i][j]=0
        #print "%d %d %c %c %d" %(i,j,board[i][0][j],word[k-1],k)
        if j-1>=0 and board[i][j-1]==word[k] and s[i][j-1]==1 and self.seach(board,i,j-1,word,k+1,s):
            return True
        elif j+1<len(board[0]) and board[i][j+1]==word[k] and  s[i][j+1]==1 and self.seach(board,i,j+1,word,k+1,s):
            return True
        elif i-1>=0 and board[i-1][j]==word[k] and  s[i-1][j]==1 and self.seach(board,i-1,j,word,k+1,s):
            return True
        elif i+1< len(board) and board[i+1][j]==word[k] and  s[i+1][j]==1 and self.seach(board,i+1,j,word,k+1,s):
            return True
        else:
            s[i][j]=1
            return False
            

c = Solution()
print c.exist([
  "ABCE",
  "SFCS",
  "ADEE"
],'ABCCED')

print c.exist([
  "ABCE",
  "SFCS",
  "ADEE"
],'SEE')

print c.exist([
  "ABCE",
  "SFCS",
  "ADEE"
],'ABCB')


print c.exist(["aa"], "aa")
