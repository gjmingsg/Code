class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==None or len(s)<2:
            return s
        x = lambda s: s == 'a' or s == 'A' or \
            s == 'e' or s == 'E' or \
            s == 'i' or s == 'I'or \
            s == 'o' or s == 'O' or \
            s == 'u' or s == 'U'
        t = filter(x,s)
        t = t[::-1]
        last = j = i = 0
        
        arr=[]
        
        while i<len(s):
            if x(s[i]):
                if last<i:
                    arr.append(s[last:i])
                arr.append(t[j])
                j = j + 1
                last = i+1
            
            i=i+1
        if last<i:
            arr.append(s[last:i])
        return ''.join(arr)


x = Solution()

print x.reverseVowels('hello')=='holle'
print x.reverseVowels('leotcede')=='leetcode'
print x.reverseVowels('a.')=='a.'
print x.reverseVowels('aA')=='Aa'

