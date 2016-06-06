class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic={0:0,1:1,2:2,3:3,4:1,5:2}
        if n <= 5:
            return dic[n]
        v =[item*item for item in range(1,n/2)]
        m = n

        for item in v:
            sub = n            
            while dic.has_key[sub]==False:
                sub = sub - item
                if dic.has_key(sub):
                    m = m + 1 + dic[sub]
                    if dic.has_key[m]:
                        if dic[n] > m:
                            dic[n] = m
                    else:
                        dic[n] = m
                else:
                
            
