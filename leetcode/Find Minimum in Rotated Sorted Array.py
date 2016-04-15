class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num)-1
        mid = (start + end)/2
        if num[start]<num[end]:
            return num[start]
        while end-start>1:
            if num[mid]>num[start]:
                start = mid
            elif num[mid]<num[end]:
                end = mid
            mid = (start + end) / 2    
        if num[start]>num[end]:
            return num[end]
        else:
            return num[start]

c = Solution()
print c.findMin([4,5,6,7,0,1,2])

print c.findMin([0,1,2,4,5,6,7])

print c.findMin([4])


print c.findMin([4,2])
