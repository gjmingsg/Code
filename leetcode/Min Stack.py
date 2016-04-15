class MinStack:
    def __init__(self):
        self.mystack = []
        self.head = -1
    # @param x, an integer
    # @return an integer
    def push(self, x):
       if self.head==-1:
           self.mystack.append({'next':-1,'num':x})
           self.head=0
           x
       else:
            bi = 0
            ei = len(self.mystack)
            while bi<ei:
                mi = (ei + bi)/2
                if self.mystack[mi]['num']>x:
                    ei = mi - 1
                elif self.mystack[mi]['num']<x:
                    bi = mi + 1
                else:
                    break;
            self.mystack.insert(mi+1,{'next':self.head,'num':x})
            self.head = mi+1
            x
    # @return nothing
    def pop(self):
        if self.head!=-1:
            temp = self.mystack[self.head]['num']
            self.head = self.mystack[self.head]['next']
            del self.mystack[self.head]
    # @return an integer
    def top(self):
        if self.head!=-1:
            return self.mystack[self.head]['num']

    # @return an integer
    def getMin(self):
        if self.head!=-1:
           return self.mystack[0]['num']
        
    def show(self):
        print 'stack'
        for a in self.mystack:
            print a['next'] ,' ', a['num'] 
        print 'head',self.head


s = MinStack()
s.push(123)
s.push(12)
s.push(12)
s.push(1)
s.push(3)
s.push(13)
s.show()
