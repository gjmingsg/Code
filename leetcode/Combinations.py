class Solution:
    def __init__(self):
        self.ans = []
    # @return a list of lists of integers
    def combine(self, n, k):
        self.n = n
        self.k = k
        self.backtrack(0,[])
        return self.ans
    def backtrack(self,i,t):

        if i==self.k:
            if len(t)==self.k:
                self.ans.append(t)
        else:
            if len(t)==0:
                y=0
            else:
                y = t[len(t)-1]
            for j in range(y+1,self.n+1):
                x = t[:]
                t.append(j)
                self.backtrack(i+1,t)
                t = x

c = Solution()
print c.combine(4,2)
