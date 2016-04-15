class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count = 0
        if A==None or len(A)==0:
            return 0
        last = A[0]
        dellist = []
        for i in range(0,len(A)):
            if last==A[i]:
                count += 1
            else:
                count = 1
            last = A[i]
            if count>=3:
                dellist.append(i)
        while len(dellist)>0:
            i = dellist.pop()
            del A[i]
        return len(A)


c = Solution()
l = [1,1,1,2,2,3]
print c.removeDuplicates(l)
print l

l = [1,1,1,2]
print c.removeDuplicates(l)
print l


l = [1,1,1,1]
print c.removeDuplicates(l)
print l
