class Solution:
    # @return a string
    def convert(self, s, nRows):
        if len(s) < nRows:
            return s
        if nRows-2<=0:
            nextRows = nRows
        else:
            nextRows = nRows - 1
        l=0
        if nextRows-1>0:    
            l = len(s)/(nextRows-1)
        else:
            l = len(s)/nextRows
        a=[]
        l=l*2
        for i in range(0,nRows):
            t=[]
            for j in range(0,l):
                t.append('\n')
            a.append(t)
        i,j=0,0
        
        for e in s:
            a[i][j]=e
            if j%2==0:
                i+=1
            else:
                i-=1
            
                
            #print "i=%d j=%d"%(i,j)
            if j%2==0 and i>=nRows:
                if nRows-2<=0:
                    j+=2
                    i=0
                else:
                    i=nextRows-1
                    j+=1
            elif j%2==1 and i<1:
                i = 0
                j+=1
            
        sa=""
        for i in range(0,nRows):
            #ts=""
            for j in range(0,l):
                #ts+= a[i][j]
                if a[i][j]!='\n':
                    sa+= a[i][j]
            #print ts
        return sa


c = Solution()
print c.convert("ABCD",2)
print c.convert("PAYPALISHIRING", 3)=="PAHNAPLSIIGYIR"

print c.convert("A",2)
print c.convert("ABC",2)=="ACB"

print c.convert("PAYPALISHIRING", 7)

print c.convert("ABCDE", 4)=="ABCED"

print c.convert("AB", 1)

print c.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 1)=="Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
            
        
