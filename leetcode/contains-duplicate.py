class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==None or len(nums)<2:
            return False
        dic ={}
        for item in nums:
            if dic.has_key(item):
                return True
            else:
                dic[item] = 1
        return False
