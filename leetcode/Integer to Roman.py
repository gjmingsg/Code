class Solution:
    # @return a string
    def intToRoman(self, num):
        D2R = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",
               90:"XC",50:"L",40:"XL",10:"X",
               9:"IX",5:"V",4:"IV",1:"I"}
        dr=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i = 0
        s=""
        while num > 0:
            if num<dr[i]:
                i+=1
                continue
            else:
                r = num/dr[i]
                num = num % dr[i]
                s=s+r*D2R[dr[i]]
        
        return s

c = Solution()
print c.intToRoman(1984)=="MCMLXXXIV"
print c.intToRoman(1)=="I"
print c.intToRoman(3999)=="MMMCMXCIX"
