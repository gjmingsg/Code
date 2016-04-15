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
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        sl=[]
        bl=[]
        cur = head
        while cur!=None:
            if cur.val<x:
                sl.append(cur.val)
            else:
                bl.append(cur.val)
            cur = cur.next
        cur = head
        while cur!=None:
            for i in sl:
                cur.val = i
                cur = cur.next
            for i in bl:
                cur.val = i
                cur = cur.next
        return head



c = Solution()
l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(5)
l.next.next.next = ListNode(2)
l.next.next.next.next= ListNode(4)
l.next.next.next.next.next= ListNode(9)
l.next.next.next.next.next.next= ListNode(13)
l.show()
l = c.partition(l,5)
l.show()
