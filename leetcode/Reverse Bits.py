class Solution:
    def __init__(self):
        self.base=[]
        for i in range(0,32):
            self.base.append(1<<i)

    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        t = 0
        #z=[]
        for i in range(0,32):
            #print (n&self.base[i])>>i
            #z.append((n&self.base[i])>>i)
            t=t|((n&self.base[i])>>i)
            t=t<<1
        #print '{0:b}'.format(t).rjust(32,"0")
        return t>>1


c = Solution()
print c.reverseBits(43261596)==964176192
            
        
