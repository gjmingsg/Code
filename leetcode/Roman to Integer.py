class Solution:
    # @return an integer
    def romanToInt(self, s):
        R2D = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,
               "XC":90,"L":50,"XL":40,"X":10,
               "IX":9,"V":5,"IV":4,"I":1}
        num = 0
        bi = 0
        ei = 1
        l = len(s)
        while ei <= l:
            key1 = s[bi:ei]
            key2 = s[bi:ei+1]
            if R2D.has_key(key2):
                #print key2
                num+=R2D[key2]
                ei+=1
            elif R2D.has_key(key1):
                #print key1
                num+=R2D[key1]
            bi=ei
            ei+=1
        return num

c = Solution()
#print c.romanToInt("I")==1
#print c.romanToInt("MC")==1100
print c.romanToInt("MMMCMXCIX")==3999
print c.romanToInt("MDCCCXCIX")==1899
            
        
        
