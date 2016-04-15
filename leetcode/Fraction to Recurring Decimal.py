class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator==0:
            return '0'
        dic={}        
        l = []
        s = ''
        k = 0
        point=True
        signed = (numerator * denominator)<0
        numerator = abs(numerator)
        denominator = abs(denominator)
        while numerator !=0 and dic.has_key(numerator)!=True:
            r = numerator/denominator
            l.append(r)
            if point==False:
                dic[numerator] = k
                
            #print "%s %d" %(point,numerator)
            #if k>100:
            #    break
            
            numerator = numerator%denominator
            if  numerator!=0 and numerator < denominator:
                if point==True:
                    point=False
                    l.append('.')
                numerator *= 10
            k+=1
            
        if numerator !=0:
            l.insert(l.index('.')+dic[numerator],'(')
            l.append(')')
        if signed:
            s='-'+s
        for i in l:
            s+=str(i)
        return s


c = Solution()
print c.fractionToDecimal(1,2)
print c.fractionToDecimal(2,1)
print c.fractionToDecimal(1,3)
print c.fractionToDecimal(2,3)
print c.fractionToDecimal(22,7)
print c.fractionToDecimal(97,37)
print c.fractionToDecimal(7,12)
print c.fractionToDecimal(7,-12)
print c.fractionToDecimal(0,10)
