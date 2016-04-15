# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def show(self):
        t = self
        while t!=None:
            print t.val
            t=t.next
        
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        s = []
        t = head
        while t!=None:
            s.append(t)
            t = t.next
        d = s[len(s) - n]
        if len(s) == n:
            head = d.next
        elif n==1 and len(s) > n:
            s[len(s) - 1 - n].next = d.next
        else:
            pred = s[len(s) - 1 - n]
            nextd = s[len(s) - n + 1]
            pred.next = nextd
        del d
        return head

head = ListNode(1)
t = ListNode(2)
head.next = t
for i in range(3,6):
    x = ListNode(i)
    t.next = x
    t = x

head.show()
print '====='
c = Solution()
c.removeNthFromEnd(head,2).show()
print '====='
c.removeNthFromEnd(head,2).show()
print '====='
c.removeNthFromEnd(head,2).show()
print '====='
c.removeNthFromEnd(head,2).show()
print '====='
head = ListNode(1)
print c.removeNthFromEnd(head,1)
#head.show()
