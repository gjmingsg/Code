# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head==None:
            return False
        cur = head.next
        dic = {}
        while cur!=None and dic.has_key(cur)==False:
            dic[cur]=1
            #print cur.val
            cur = cur.next
            
            
        if dic.has_key(cur):
            return True
        return False

    def hasCycle_good(self, head):
        if head==None:
            return False
        cur = head.next
        fast = head.next
        
        while cur!=None and fast!=None:
            #dic[cur]=1
            #print cur.val
            
            cur = cur.next
            if fast.next==None:
                return False
            fast = fast.next.next
            if cur==fast:
                return True
        return False
    
c = Solution()

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
print c.hasCycle(l)

l.next.next.next = l
print c.hasCycle(l)
