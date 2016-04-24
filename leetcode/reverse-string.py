class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==None or len(s) < 1:
            return s
        return s[::-1]


c = Solution()
print c.reverseString('hello') == 'olleh'
