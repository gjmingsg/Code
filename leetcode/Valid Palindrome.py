class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i].isalnum()==False:
                i=i+1
                continue
            if s[j].isalnum()==False:
                j=j-1
                continue
            if s[i].upper()==s[j].upper():
                j=j-1
                i=i+1
            else:
                #print 'l=',s[i],' r=',s[j]
                return False
        return True



s = Solution()
print s.isPalindrome('A man, a plan, a canal: Panama')==True
print s.isPalindrome('race a car')==False
print s.isPalindrome('')==True

         
