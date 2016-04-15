class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for item in s:
            top = len(stack)-1
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            elif top>=0:
                if item==')' and stack[top] == '(':
                    stack.pop()
                elif item==']' and stack[top] == '[':
                    stack.pop()
                elif item=='}' and stack[top] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False

s = Solution()
print s.isValid("()[]{}")==True

print s.isValid("(]")==False

print s.isValid("([)]")==False

print s.isValid("[")==False
print s.isValid("]")==False
