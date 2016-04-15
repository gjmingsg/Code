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
    # @return nothing
    def reorderList(self, head):
        if head==None:
            return head
        l = []
        cur = head
        while cur!=None:
            l.append(cur)
            cur = cur.next
        n = len(l)
        up = n / 2 
        cur = head
        for i in range(0,up):
            t = l[n-i - 1]
            nxt = cur.next

            #print cur.val
            #print t.val
            
            cur.next = t
            t.next =nxt
            cur = nxt
        if n%2==0:
            cur.next.next=None
        else:
            cur.next = None
        return head


c = Solution()
l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(5)
l.next.next.next = ListNode(5)
l.next.next.next.next= ListNode(7)
l.next.next.next.next.next= ListNode(9)
l.next.next.next.next.next.next= ListNode(13)
l.show()
l = c.reorderList(l)
l.show()


l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(5)
l.next.next.next = ListNode(5)
l.next.next.next.next= ListNode(7)
l.next.next.next.next.next= ListNode(9)
#l.next.next.next.next.next.next= ListNode(13)
l.show()
l = c.reorderList(l)
l.show()

l = ListNode(1)

l.show()
l = c.reorderList(l)
l.show()

