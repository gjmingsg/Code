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
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        i = 1
        first = ListNode(0)
        first.next,pre,cur=head,first,head
        fitem,litem = None,None
        while i < n:
            pre = cur
            cur = cur.next
            if i == m:
                fitem = pre
            if i>=m:    
                t = cur.next
                cur.next = pre
                pre = cur
                cur = t
                i+=1
                if i==n:
                   fitem.next = pre
                   
            i+=1

            
c = Solution()
l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(5)
l.next.next.next = ListNode(5)
l.next.next.next.next= ListNode(7)
l.next.next.next.next.next= ListNode(9)
l.next.next.next.next.next.next= ListNode(13)
l.show()

c.reverseBetween(l,2,4).show()
