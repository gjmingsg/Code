class Solution:
    # @return an integer
    def numTrees(self, n):
        f0=1
        f1=1
        if n==0:
            return 1
        if n==1:
            return 1
        for i in range(1,n):
            f0 = f1
            f1 = 2 * (2 * i + 1) * f0 / (i+2) 
        return f1

c = Solution()
#print c.numTrees(3)
for i in range(0,100):
    print c.numTrees(i)
