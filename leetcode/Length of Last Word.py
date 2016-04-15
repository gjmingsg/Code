class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip(' ')
        a = s.split(' ')
        if len(a)>0:
            return len(a[len(a)-1])
        else:
            return 0


s = Solution()
print s.lengthOfLastWord("Hello World") == 5
print s.lengthOfLastWord("Hello")==5
print s.lengthOfLastWord("") == 0
print s.lengthOfLastWord("a ") == 1
print s.lengthOfLastWord(" a ") == 1
