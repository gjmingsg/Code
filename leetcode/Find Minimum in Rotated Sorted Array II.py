class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num)-1
        mid = (start + end)/2
        if num[start]<num[end]:
            return num[start]
        while end-start>1 and num[start]>=num[end]:
            #print "mid=%d"% mid
            
            if num[mid]>num[start]:
                start = mid
            elif num[mid]<num[end]:
                end = mid
            else:
                if num[mid]==num[start]:
                    start += 1
                if num[mid]==num[end]:
                    end -= 1
            mid = (start + end) / 2    
        if num[start]>num[end]:
            return num[end]
        else:
            return num[start]

c = Solution()
print c.findMin([10,1,10,10,10])==1

print c.findMin([1,2,1])==1

print c.findMin([4])==4


print c.findMin([4,2])==2


print c.findMin([3,1,3])==1
print c.findMin([1,3,3])==1

print c.findMin([2,2,2,1,1,2])
