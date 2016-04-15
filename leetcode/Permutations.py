class Solution:
    def __init__(self):
        self.ans=[]
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.num = num
        self.backtrack(0,[])
        return self.ans
    def backtrack(self,i,lst):
        if i==len(self.num):
            self.ans.append(lst)
        else:
            for j in range(i,len(self.num)):
                t = lst[:]
                lst.append(self.num[j])
                self.backtrack(i+1,lst)
                lst = t
c = Solution()
print c.permute([1,2,3])
