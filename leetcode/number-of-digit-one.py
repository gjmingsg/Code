class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1,n+1):
            t = i
            while t>0:
                if (t % 10 == 1):
                    count = count + 1
                    
                t = t/10
        return count



c = Solution()
print c.countDigitOne(13)
print c.countDigitOne(3184191)   
