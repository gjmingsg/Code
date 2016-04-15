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
    def insertionSortList(self, head):
        if head==None:
            return head
        first = ListNode(0)
        first.next = head
        preh,cur,pre = first,head,head
        cur = cur.next
        while cur!=None:
            if pre.val > cur.val:
                while head.val < cur.val:
                    preh = head
                    head = head.next
                pre.next = cur.next
                cur.next = head
                preh.next = cur
                cur = pre
                preh,head = first, first.next
                #first.show()
            else:
                pre = cur
            cur = cur.next
        return first.next

c = Solution()
l = ListNode(4)
l.next = ListNode(1)
l.next.next = ListNode(5)
l.next.next.next = ListNode(3)
l.next.next.next.next= ListNode(4)
l.next.next.next.next.next= ListNode(7)
l.next.next.next.next.next.next= ListNode(3)
l.show()
c.insertionSortList(l).show()
