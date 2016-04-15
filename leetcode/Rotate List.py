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
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        
        if head==None or k == 0:
            return head
        cur = head
        tail = head
        length = 0
        while cur!=None:
            length += 1
            tail = cur
            cur = cur.next
        #tail.next = head
        k = k % length
        if k==0:
            return head
        cur,pre = head,head
        while length>k:
            length -= 1
            pre = cur
            cur = cur.next
        tail.next = head
        head = cur
        pre.next=None
        return head

c = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next= ListNode(5)
c.rotateRight(l,2).show()

l = ListNode(1)
l.next = ListNode(2)
c.rotateRight(l,2).show()

l = ListNode(1)
l.next = ListNode(2)
c.rotateRight(l,3).show()
        
