class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        bi = 0
        ei = len(A)
        while bi < ei:
            mi = (bi+ei)/2
            #print "%d %d %d" %(bi,ei,mi)
            if A[mi]>=target:
                ei = mi
            else:
                bi = mi + 1
        return bi
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        i = self.searchInsert(A,target)
        if len(A)<=i or A[i]!=target:
            return [-1,-1]
        j = self.searchInsert(A,target+1)
        return [i,j-1]
c = Solution()
print c.searchRange([5, 7, 7, 8, 8, 10], 8)
print c.searchRange([2,2], 3)
 
