class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        c = 0
        
        length = len(digits) - 1
        for i in range(length,-1,-1):
            if i==length:
                digits[i]=digits[i] + 1
            else:
                digits[i]=digits[i] + c
                c = 0
            if digits[i]>=10:
                c = digits[i] / 10
                digits[i] = digits[i] % 10
        if c>0:
            digits.insert(0,c)
        return digits

a = Solution()
print a.plusOne([1,2,3,4,5,6,9])
print a.plusOne([9])
print a.plusOne([9,9,9,9,9])
