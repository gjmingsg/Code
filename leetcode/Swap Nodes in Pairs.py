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
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head==None:
            return head
        cur = head
        nxt = head.next
        if nxt==None:
            return head
        head=nxt
        cur.next = nxt.next 
        head.next = cur
        while cur.next!=None:
            pre = cur
            cur = cur.next
            nxt = cur.next
            if nxt==None:
                break
            pre.next = nxt
            cur.next = nxt.next 
            nxt.next = cur
        return head

c = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
print c.swapPairs(l).show()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
print c.swapPairs(l).show()
        
