class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n>0:
            count += (n & 1)
            n=n>>1
        return count

c = Solution()
print c.hammingWeight(11) == 3

