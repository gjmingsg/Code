class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x==0:
            return 0
        r0 = x
        r1 = (r0 + x / r0) / 2
        
        while r0-r1 > 0.01:
            r0 = r1
            r1 = (r0 + x / r0) / 2
        #print "%d %d" % (r0,r1)
        if x==r1 * r1:
            return r1
        return r0

c = Solution()

print c.sqrt(3)

print c.sqrt(16)

print c.sqrt(9)

print c.sqrt(12)
        
