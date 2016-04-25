class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums==None:
            return None
        if len(nums)==0:
            return nums
        i = end = start = 0
        ranges = []
        change = True
        while i < len(nums):
            if i==0:
                i = i + 1
                continue
            if nums[i-1]+1 == nums[i]:
                end = end + 1
            else:
                if start == end:
                    ranges.append(str(nums[start]))
                else:
                    ranges.append(str(nums[start]) + "->" + str(nums[end]))
                start = i
                end = i
            i = i + 1
        if start == end:
            ranges.append(str(nums[start]))
        else:
            ranges.append(str(nums[start]) + "->" + str(nums[end]))
        return ranges



c = Solution()

print c.summaryRanges([0,1,2,4,5,7])
print c.summaryRanges([0])
print c.summaryRanges([0,1,2,3])
print c.summaryRanges([])  
        
