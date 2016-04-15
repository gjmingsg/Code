# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    def show(self):
        cur = self
        s = ''
        while cur!=None:
            if cur.random==None:
                s=s+ '%d->' % (cur.label)
            else:
                s=s+ '%d(%d)->' % (cur.label,cur.random.label)
            cur = cur.next
        print s
        
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head==None:
            return head
        dic={}
        newhead = RandomListNode(head.label)
        newcur,dic[head] = newhead,newhead
        cur = head.next
        while cur!=None:
            dic[cur]=RandomListNode(cur.label)
            newcur.next = dic[cur]
            cur,newcur = cur.next,newcur.next
        cur,newcur = head,newhead
        while cur!=None:
            if cur.random!=None:
                newcur.random = dic[cur.random]
            newcur,cur = newcur.next,cur.next
        return newhead
            

c = Solution()
l = RandomListNode(1)
l.next = RandomListNode(3)
l.next.next = RandomListNode(5)
l.next.random = l
l.next.next.next = RandomListNode(5)
l.next.next.next.next= RandomListNode(7)
l.next.next.next.next.next= RandomListNode(9)
l.next.next.next.random = l.next
l.next.next.next.next.next.next= RandomListNode(13)
h = c.copyRandomList(l)
h.show()
