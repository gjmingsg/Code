class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        f1=1
        f2=2
        while n > 2:
            f = f1+f2
            n=n-1
            f1 = f2
            f2=f
        return f

c = Solution()
print c.climbStairs(1)
            
