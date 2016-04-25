class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return None
        last = 0
        i = 0
        while i<len(nums) and last == nums[i]:
            last = last + 1
            i = i + 1
        return last


c=Solution()
print c.missingNumber( [0, 1, 3])
print c.missingNumber( [1])
