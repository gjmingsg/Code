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
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head==None:
            return head
        old,pre,nxt = head,head,head
        cur = head.next
        dl = False
        while cur!=None:
            
            if pre.val==cur.val:
                dl = True
                nxt = cur
            elif dl==True:
                dl = False
                #print cur.val
                if pre==head:
                    head = nxt.next
                else:
                    old.next = cur
                #old = pre
                pre = cur
            else:
                old = pre
                pre = cur
            cur = cur.next
        if dl==True:
            if pre==head:
                head = nxt.next
            else:
                old.next = cur
        return head






c = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(3)
l.next.next.next.next= ListNode(4)
l.next.next.next.next.next= ListNode(4)
l.next.next.next.next.next.next= ListNode(5)
c.deleteDuplicates(l).show()


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(3)
l.next.next.next.next= ListNode(4)
l.next.next.next.next.next= ListNode(4)
l.next.next.next.next.next.next= ListNode(4)
c.deleteDuplicates(l).show()


l = ListNode(2)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(3)
l.next.next.next.next= ListNode(3)
l.next.next.next.next.next= ListNode(4)
l.next.next.next.next.next.next= ListNode(5)
c.deleteDuplicates(l).show()

c.deleteDuplicates(None)
