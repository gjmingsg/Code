# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def show(self):
        cur = self
        s = ''
        while cur!=None:
            s=s+ '%d->' % (cur.val)
            cur = cur.next
        print s
        
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        first = ListNode(0)
        first.next = l1
        pre = first
        
        while l1!=None and l2!=None:
            if l1.val > l2.val:
                pre.next = l2
                pre = l2
                t = l2.next
                l2.next = l1
                l2 = t
            else:
                pre = l1
                l1 = l1.next
        if l1==None:
            pre.next = l2
        return first.next
        

c = Solution()
l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(5)
l.next.next.next = ListNode(5)
l.next.next.next.next= ListNode(7)
l.next.next.next.next.next= ListNode(9)
l.next.next.next.next.next.next= ListNode(13)
l.show()


l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(8)
l2.next.next.next.next= ListNode(10)
l2.next.next.next.next.next= ListNode(19)
l2.next.next.next.next.next.next= ListNode(23)
l2.show()
c.mergeTwoLists(l,l2).show()
