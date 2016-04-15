class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        length = round(len(num) / 2.0)
        #print length
        ab ={}
        for i in num:
            if ab.has_key(i):
                ab[i] = ab[i]+1
            else:
                ab[i]=1
            if ab[i]>=length:
                return i
            
a = Solution()
print a.majorityElement([1,2,3,4,2,2])==2 
print a.majorityElement([2,2])==2 
