# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        while cur.next!=None:
            cur.val = cur.next.val
            if cur.next.next == None:
                cur.next=None
            else:
                cur = cur.next
        


a = ListNode(1)
a.next = ListNode(2)
c = ListNode(3)
a.next.next = c
a.next.next.next = ListNode(4)


b = Solution()
b.deleteNode(c)

while a!=None:
    print(a.val)
    a = a.next
