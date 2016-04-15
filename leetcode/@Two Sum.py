class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic = {}
        for i in range(0,len(num)):
            if dic.has_key(num[i])==False:
                dic[num[i]]=[]
            dic[num[i]].append(i)
        #print dic
        for i in range(0,len(num)):
            if dic.has_key(target-num[i]):
                if target-num[i]== num[i]:
                    if len(dic[target-num[i]])==1:
                        continue
                    else:
                        j = dic[target-num[i]][1]
                else:
                    j = dic[target-num[i]][0]
                if i<j:
                    return (i+1,j+1)
                else:
                    return (j+1,i+1)
        

c = Solution()
print c.twoSum([2, 7, 11, 15],9)
print c.twoSum([5,75,25],100)
print c.twoSum([3,2,4], 6)
print c.twoSum([0,4,3,0], 0)
