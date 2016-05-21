class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        for item in nums:
            if dic.has_key(item):
                dic[item] = dic[item] + 1
            else:
                dic[item] = 1
        
        dic = sorted(dic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
        l = []
        i = 0
        
        for item in dic:
            if i<k:
                l.append(item[0])
            else:
                break
            i=i+1
        return l
        


c = Solution()

print c.topKFrequent([1,1,1,2,2,3],2)
print c.topKFrequent([1],1)
print c.topKFrequent([4,1,-1,2,-1,2,3],2)
