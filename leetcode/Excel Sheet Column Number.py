class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        
        ans = 0
        i=0
        for i in s:
            t = ord(i) - ord('A') + 1
            if i==0:
                ans = t
                i=1
            else:
                ans = ans * 26 + t
        return ans

s = Solution()
print s.titleToNumber('AB')  
print s.titleToNumber('AA') 
print s.titleToNumber('Z')  
