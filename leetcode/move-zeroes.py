class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums==None:
            return None
        
        i = 0
        last = 0
        count = 0
        change = True
        while i < len(nums):
            if nums[i] == 0:
                count = count + 1
                if change:
                    last = i
                    change = False
            else:
                nums[last] = nums[i]
                last = last + 1
            
            i = i + 1
        i = len(nums)-count
        while i < len(nums):
            nums[i] = 0
            i = i + 1
        "return nums"


c = Solution()

print c.moveZeroes([0, 1, 0, 3, 12])
print c.moveZeroes([0])
print c.moveZeroes([1,2,3])
print c.moveZeroes(None)
