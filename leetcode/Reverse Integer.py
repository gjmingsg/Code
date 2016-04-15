class Solution:
    # @return an integer
    def reverse(self, x):
        issign = False
        if x < 0:
            issign = True
            x = 0-x
        s = str(x)[::-1]
        a = int(s)
        if 2147483647 < a:
            return 0
        if issign == True:
            a = 0 - a
        
        return a

x = Solution()
print x.reverse(123) == 321
print x.reverse(-123) == -321
print x.reverse(1534236469) == 0
