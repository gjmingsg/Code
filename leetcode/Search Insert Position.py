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

c = Solution()
print c.searchInsert([1,3,5,6], 5)

print c.searchInsert([1,3,5,6], 2)

print c.searchInsert([1,3,5,6], 7)

print c.searchInsert([1,3,5,6], 0)
