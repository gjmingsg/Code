class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        i = 0
        l = 0
        if len(v1) > len(v2):
            l = len(v1)
        else:
            l = len(v2)
        
        for i in range(0,l):
            ai = '0'
            bi = '0'
            if i < len(v1):
                ai = v1[i]
            if i < len(v2):
                bi = v2[i]
                
            if len(ai)>len(bi):
                bi = bi.rjust(len(ai),'0')
            
            if len(ai)<len(bi):
                ai = ai.rjust(len(bi),'0')
            
            if ai > bi:
                return 1
            elif ai < bi:
                return -1
            else:
              i=i+1
        
        return 0
         
                
s= Solution()
print s.compareVersion('01','1')==0
print s.compareVersion('0.1','1.1')==-1
print s.compareVersion('1.1','1.2')==-1
print s.compareVersion('1.2','13.37')==-1
print s.compareVersion('01','1.0')==0
print s.compareVersion('01.1.1.1','1.0')==1
print s.compareVersion('01.2','1.10')==-1
