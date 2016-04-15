class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x< 0:
            return False
        if x < 10:
            return True
        maxint = 1000000000
        t = x / maxint
        while t == 0:
            maxint = maxint / 10
            t = x / maxint
        base = 10
        t=x
        while base <= maxint:
            #print 'base %d %d'%(base,maxint)
            h = t / maxint
            l = t % base
            #print 't %d %d'%(h,l)
            if h == l:
                t = t % maxint
                t = t / base
                maxint = maxint / base / 10
            else:
                return False
        return True

c = Solution()
print c.isPalindrome(101) == True

print c.isPalindrome(1012) == False

print c.isPalindrome(0) == True

print c.isPalindrome(-2147483648) == False
print c.isPalindrome(-101) == False
print c.isPalindrome(1001) == True
print c.isPalindrome(10) == False
