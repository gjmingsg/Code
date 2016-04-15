class MinStack:
    def __init__(self):
        self.mystack = []
        self.myorder = []
    # @param x, an integer
    # @return an integer
   
    def push(self, x):
        self.mystack.append(x)
        if len(self.myorder)==0 or self.myorder[len(self.myorder)-1] >= x:
           self.myorder.append(x) 
        x
        #self.show()
    # @return nothing
    def pop(self):
        index = len(self.mystack)-1
        x = self.mystack[index]
        del self.mystack[index]
        index = len(self.myorder)-1
        if index>=0 and self.myorder[index] == x:
            del self.myorder[index]
        
    # @return an integer
    def top(self):
        length = len(self.mystack)
        if length>0:
            return self.mystack[length-1]
        
    # @return an integer
    def getMin(self):
        if len(self.myorder)>0:
            return self.myorder[len(self.myorder)-1]

    #=========
    def show(self):
        print self.myorder
        print 'myorder====================end'

s = MinStack()
s.push(0)
s.push(1)
s.push(0)
s.getMin()
s.pop()
s.getMin()
