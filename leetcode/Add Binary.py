class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        al = len(a)
        bl = len(b)
        ans = ''
        if al > bl:
            b = b.rjust(al,'0')
        elif al<bl:
            a = a.rjust(bl,'0')
        carry = 0
        for i in range(len(a) - 1,-1,-1):
            t = (ord(a[i]) - ord('0')) + (ord(b[i]) - ord('0')) +carry
            if t>=2:
                carry = 1
                t = t % 2
            else:
                carry = 0
            ans = chr(ord('0')+t)+ans
        if carry>0:
            return chr(ord('0')+carry)+ ans
        return ans

c = Solution()

print c.addBinary('11','1')
print c.addBinary('1','1')        
