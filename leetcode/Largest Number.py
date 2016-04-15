class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num.sort(self.cmp)
        s = ''
        for i in num:
            s += str(i)
        s = s.lstrip('0')
        
        
        if len(s)==0:
            s='0'
        return s
    
    def cmp(self,x,y):
        sx = str(x)+str(y)
        sy = str(y)+str(x)
        if sx >=sy:
            return -1
        elif sx == sy:
            return 0
        return 1


c = Solution()
print c.largestNumber([3, 30, 34, 5, 9])
print c.largestNumber([0,0])
