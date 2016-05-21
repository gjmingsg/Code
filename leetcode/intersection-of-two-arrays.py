class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic={}
        for item in nums1:
            dic[item]=1
        for item in nums2:
            if dic.has_key(item):
                dic[item] = 2
        l=[]
        for (key,value) in dic.items():
            if value==2:
                l.append(key)
        return l



c = Solution()
print c.intersection([1, 2, 2, 1],[2, 2])
