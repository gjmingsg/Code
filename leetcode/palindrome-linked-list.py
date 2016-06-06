# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t = head
        l = []
        while t!=None:
            l.append(t.val)
            t=t.next
        i = len(l)-1
        up = len(l)/2
        t = head
        while i>=up:
            if t.val!=l[i]:
                return False
            t=t.next
            i = i-1
        return True


t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(3)
t.next.next.next = ListNode(2)
t.next.next.next.next = ListNode(1)
c = Solution()
print c.isPalindrome(t)


t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(3)
print c.isPalindrome(t)

