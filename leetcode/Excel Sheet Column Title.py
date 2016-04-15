class Solution:
    def __init__(self):
        self.strlist = 'abcdefghijklmnopqrstuvwxyz'.upper()
    # @return a string
    def convertToTitle(self, num):
        s = ''
        while num > 26:
            k = num % 26
            num = (num - 1) / 26
            s= self.strlist[k-1] + s 
        else:
            s= self.strlist[num-1] + s
        return s

c = Solution()


for i in range(1,200):
    print '%d %s'%(i,c.convertToTitle(i))
    
print c.convertToTitle(52) #AZ
#print c.convertToTitle(26)
#print c.convertToTitle(28)
#print c.convertToTitle(27)
