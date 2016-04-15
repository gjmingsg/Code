class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs==None or len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        i = 0
        
        flag = True
        
        while flag:
            pre = ""
            for s in strs:
                if i >= len(s):
                    flag=False
                    break
                if len(s)==0:
                    return ""
                if pre=="" or pre == s[i]:
                    pre = s[i]
                else:
                    flag=False
                    break
            if flag:
                i += 1
        return strs[0][:i]

c = Solution()

print c.longestCommonPrefix(["1234","12"])
print c.longestCommonPrefix(["",""])
print c.longestCommonPrefix(["c","c"])
print c.longestCommonPrefix(["aaa","aa","aaa"])
print c.longestCommonPrefix(["abab","aba","abc"])
            
