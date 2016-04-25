class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==None or len(nums)<2:
            return False
        dic ={}
        i = 0
        while i < len(nums):
            item = nums[i]
            if dic.has_key(item):
                if  i - dic[item] <=k:
                    return True
                else:
                    dic[item] = i
            else:
                dic[item] = i
            i=i+1
        return False


c = Solution()
print c.containsNearbyDuplicate([99,99],2) == True
print c.containsNearbyDuplicate([1,0,1,1],1) == True

