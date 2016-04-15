class Solution:
    def __init__(self):
        self.hs={}
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n==0:
            return 1
        if n<0:
            x = 1 / x
            n = 0 - n
        if self.hs.has_key(n):
            return self.hs[h]
        
        if n % 2 == 1:
            self.hs[n-1] = x * self.pow(x,n-1)
            return self.hs[n-1]
        else:
            self.hs[n/2] = self.pow(x,n/2)            
            return  self.hs[n/2]*self.hs[n/2]




c = Solution()
print c.pow(2.0,-10) 
