class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = hi = len(nums) - 1
        lo = 0
        while hi - lo>=1:
            m = (hi + lo)/2
            if nums[m]>nums[hi]:
                lo = m+1
            elif nums[m]<nums[lo]:
                hi = m
            else:
                hi = lo
                break
        
        
        if target>=nums[0]:
            if hi == 0:
                return self.binSearch(nums,0,l,target)
            else:
                return self.binSearch(nums,0,hi-1,target)
        if target<=nums[l]:
            return self.binSearch(nums,hi,l,target)
        return -1
    
    def binSearch(self,nums,lo,hi,target):
        while hi-lo>=0:
            m = (lo+hi)/2
            if nums[m]< target:
                lo = m+1
            elif nums[m]>target:
                hi = m-1
            else:
                return m
        return -1
            
c = Solution()

print c.search([1,3],1) == 0
print c.search([5,1],1) == 1
print c.search([5,1],5) == 0
print c.search([1,3],11) == -1

print c.search([5,1,3],1) == 1
print c.search([5,1,3],5) == 0
print c.search([5,1,3],3) == 2
print c.search([5,1,3],15) == -1

print c.search([1,3],3) == 1
print c.search([4, 5, 6, 7, 0, 1, 2],0) == 4
print c.search([4, 5, 6, 7, 0, 1, 2],4) == 0
print c.search([4, 5, 6, 7, 0, 1, 2],2) == 6
print c.search([4, 5, 6, 7, 0, 1, 2],12) == -1

print c.search([1, 2, 4, 5, 6, 7, 0],4)==2
print c.search([1, 2, 4, 5, 6, 7, 0],1)== 0
print c.search([1, 2, 4, 5, 6, 7, 0],0)== 6
print c.search([1, 2, 4, 5, 6, 7, 0],12)== -1

print c.search([0, 1, 2, 4, 5, 6, 7],4)== 3
print c.search([0, 1, 2, 4, 5, 6, 7],0)== 0
print c.search([0, 1, 2, 4, 5, 6, 7],7)== 6
print c.search([0, 1, 2, 4, 5, 6, 7],12)== -1
""""""
