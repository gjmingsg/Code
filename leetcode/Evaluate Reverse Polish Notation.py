class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        if tokens==None or len(tokens)==0:
            return
        for item in tokens:
            if item == '*':
                item2 = stack.pop()
                item1 = stack.pop()
                stack.append(str(int(item1)*int(item2)))
            elif item == '+':
                item2 = stack.pop()
                item1 = stack.pop()
                stack.append(str(int(item1)+int(item2)))
            elif item == '-':
                item2 = stack.pop()
                item1 = stack.pop()
                stack.append(str(int(item1)-int(item2)))
            elif item == '/':
                item2 = stack.pop()
                item1 = stack.pop()
                x1 = int(item1)
                x2 = int(item2)
                ans = x1 / x2
                if ans < 0:
                    ans = 0- (abs(x1) / abs(x2))
                stack.append(str(ans))
            else:
                stack.append(item)
            #print stack
        return int(stack[0])

c = Solution()

#print c.evalRPN( ["2", "1", "+", "3", "*"]) == 9
#print c.evalRPN(["4", "13", "5", "/", "+"]) ==6
print c.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])==22
print c.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])==165
