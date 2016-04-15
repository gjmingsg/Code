class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i=0
        j=0
        while i<len(A)-1:
            if A[j]==A[i+1]:
                i=i+1
            else:
                j=j+1
                A[j]= A[i+1]
                i=j
        print A
        return j

c = Solution()
print c.removeDuplicates([1,1,2])


class Solution2:
# @param a list of integers
# @return an integer

    def removeDuplicates(self, A):
        if not A:
            return 0
        else:
            ii,jj=1,1
            while jj<len(A):
                if A[ii-1]!=A[jj]:
                    A[ii]=A[jj]
                    ii+=1
                jj+=1
            
            return ii
