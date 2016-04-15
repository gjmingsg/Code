class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if str=='' or str==None:
            return 0
        flag = 1
        if str[0]=='-':
            flag = -1
            str=str[1:]
        elif str[0]=='+':
            str=str[1:]
        i = 0
        l=[]
        for x in str:
            t = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}.get(x)
            if t!=None:
                l.append(t)
            else:
                break
        try:
            i = reduce(lambda x,y:x*10+y,l )
        except:
            return i*flag
        i = i*flag
        if i>2147483647:
            return 2147483647
        if  i < -2147483648:
            return -2147483648
        return i



c = Solution()
print c.atoi('-12312')
print c.atoi('+12312')

print c.atoi('+1231a2')

print c.atoi('-+1')

print c.atoi('  -0012a42')
