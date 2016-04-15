# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def show(self):
        x = self
        st = ''
        while x!=None:
            st=st+'%d->'%x.val
            x = x.next
        print st
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        t1 = l1
        t2 = l2
        carry = 0
        pre = t1
        if t1==None:
            return l2
        if t2==None:
            return l1
        while t1!=None or t2!=None or carry>0:
            if t1==None:
                t1 = ListNode(0)
                pre.next = t1
            if t2==None:
                tmp = t1.val + carry
            else:
                tmp = t1.val + t2.val + carry
                t2=t2.next
                #print '%d=%d+%d+%d'%(tmp,t1.val, t2.val , carry)
            carry = 0
            if tmp >= 10:
                carry = tmp / 10
                tmp = tmp % 10
            t1.val = tmp
            pre = t1
            t1=t1.next
        return l1
c = Solution()
#print c.addTwoNumbers(None,None) == None



l1 = ListNode(2)
hl1 = l1
l1.next = ListNode(4)
l1 = l1.next
l1.next = ListNode(3)
#print c.addTwoNumbers(hl1,None)==hl1
#print c.addTwoNumbers(None,hl1)==hl1

l2 = ListNode(5)
hl2 = l2
l2.next = ListNode(6)
l2 = l2.next
l2.next = ListNode(9)
#print c.addTwoNumbers(hl1,hl2).show()

l2 = l2.next
l2.next = ListNode(9)
hl1.show()
hl2.show()
#c.addTwoNumbers(hl1,hl2).show()
c.addTwoNumbers(hl2,hl1).show()
