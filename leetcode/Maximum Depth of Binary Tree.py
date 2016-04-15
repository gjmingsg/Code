# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.md=0
        
    def maxDepth(self, root):
        if root==None:
            return 0
        self.getMaxDepth(root,1)
        return self.md
    def getMaxDepth(self,node,depth):
        if node.left==None and node.right==None:
            if self.md<depth:
                self.md = depth
        if node.left!=None:
            self.getMaxDepth(node.left,depth+1)
        if node.right!=None:
            self.getMaxDepth(node.right,depth+1)

c = Solution()
root = TreeNode(5)
node1 = TreeNode(4)
root.left = node1
node2 = TreeNode(8)
root.right = node2
node3 = TreeNode(11)
node1.left = node3
node3.left = TreeNode(7)
node3.right = TreeNode(2)
node2.left = TreeNode(13)
node4 = TreeNode(4)
node2.right = node4
node4.right =  TreeNode(1)

print c.maxDepth(root)
