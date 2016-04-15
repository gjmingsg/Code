class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        l = 0
        delv = []
        for item in A:
            if elem == item:
                delv.append(item)
            else:
                l = l + 1
        for item in delv:
            A.remove(item)
        #print A
        return l

c = Solution()
print c.removeElement([4,5], 4)
