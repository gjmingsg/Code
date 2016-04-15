class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        zeros = 0
        if n<5:
            return zeros
        dic={5:1}
        for i in range(5,n+1,5):
           t = i
           c = 0
           while t>=5 and t % 5 == 0:
               t = t / 5
               c = c + 1
           dic[i]=c
        for num,count in dic.items():
            zeros = zeros + count
        return zeros

    def fac(self,n):
        ans = 1
        for i in range(1,n):
            ans = ans * i
        return ans * n
c = Solution()


print "%d" % (c.trailingZeroes(1808548329))

