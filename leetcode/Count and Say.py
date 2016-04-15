class Solution:
    # @return a string
    def countAndSay(self, n):
        if n==1:
            return "1"
        n1 = "1"
        while n>1:
            i=0
            nxt = ""
            count = 1
            while i<len(n1):
                #print n1
                if i+1 < len(n1) and n1[i]==n1[i+1]:
                    count += 1                    
                else:
                    nxt = nxt + str(count) + n1[i]
                    count = 1
                i += 1
            n-=1
            n1 = nxt
        return nxt

c = Solution()
#print c.countAndSay(3)
for i in range(1,1000):
    print c.countAndSay(i) ==countAndSay(i)


