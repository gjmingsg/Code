class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        k = m + n - 1
        s = 1
        j = 1
        for i in range(1,k):
            if i==n:
                j=1
            s = s * i / j
            j+=1
        return s


c = Solution()
print c.uniquePaths(1,10)
