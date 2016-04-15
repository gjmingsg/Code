# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def show(self):
        t = self
        st = ''
        while t!=None:
            st = st + '%d->' %t.val
            t = t.next
        print st
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        t = head
        pre = head
        s = set()
        while t!=None:
            if s.__contains__(t.val):
                pre.next = t.next
                del t
                t = pre.next
            else:
                s.add(t.val)
                pre = t
                t = t.next
        return head

c = Solution()

l = ListNode(1)
t = l
t.next = ListNode(1)
t = t.next
t.next = ListNode(2)
t = t.next
t.next = ListNode(3)
t = t.next
t.next = ListNode(3)
l.show()

c.deleteDuplicates(l).show()

c.deleteDuplicates(None).show()
