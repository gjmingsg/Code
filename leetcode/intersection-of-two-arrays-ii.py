class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic={}
        for item in nums1:
            if dic.has_key(item):
                dic[item] = dic[item] + 1
            else:
                dic[item]=1
        l=[]
        for item in nums2:
            if dic.has_key(item) and dic[item]>0:
                dic[item] = dic[item] - 1
                l.append(item)
        
        return l



c = Solution()
print c.intersect([1, 2, 2, 1],[2, 2])
