class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        index=0
        l = len(A)-1
        while index<l:
            index +=A[index]
            if A[index]==0:
                return False
        return index==l

c = Solution()
A = [2,3,1,1,4]
print c.canJump(A)
A = [3,2,1,0,4]
print c.canJump(A)
