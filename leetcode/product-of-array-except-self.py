class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def isZore(x,prd):
            
            if x==0:
                return prd
            else:
                return 0
        if nums==None or len(nums)==0:
            return None
        count = 0
        t = 1
        for item in nums:
            if item==0:
                count = count + 1
            else:
                t = t * item
            if count>1:
                t = 0
                break
        
        if t==0:
            return map(lambda x: 0, nums)
        elif count==1:
            
            return map(lambda x: isZore(x,t), nums)
        else:
            return map(lambda x: t/x, nums)
        
c = Solution()
print c.productExceptSelf([1,2,3,4])
print c.productExceptSelf([0,0])
print c.productExceptSelf([0,1])
