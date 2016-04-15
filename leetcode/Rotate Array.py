class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    def rotate(self, nums, k):
        for i in range(0,k):
            t = nums.pop()
            nums.insert(0,t)


l = [1,2,3,4,5,6,7]
c = Solution()
c.rotate(l,3)
print l
    
