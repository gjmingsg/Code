# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.cur = root
        self.stack=[]
        while self.cur!=None:
            self.stack.append(self.cur)
            self.cur = self.cur.left
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack)>0

    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            ans = self.stack.pop()
            if ans.right!=None:
                self.cur = ans.right
            else:
                self.cur = None
            while self.cur!=None:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            return ans.val
        
        

root = TreeNode(5)
node1 = TreeNode(4)
root.left = node1
node2 = TreeNode(8)
root.right = node2
node3 = TreeNode(2)
node1.left = node3
node3.left = TreeNode(1)
node3.right = TreeNode(3)
node2.left = TreeNode(7)
node4 = TreeNode(9)
node2.right = node4

# Your BSTIterator will be called like this:
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())

print v
