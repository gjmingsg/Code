# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        self.sum = sum
        if root==None:
            return False
        return self.sumToLeaf(root,0)
    def sumToLeaf(self,node,acc):
        if node==None:
            return False
        elif node.left == None and node.right==None:
            return self.sum==acc+node.val
        else:
            return self.sumToLeaf(node.left,acc+node.val) or self.sumToLeaf(node.right,acc+node.val)

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

print c.hasPathSum(root,22)==True

root = TreeNode(1)
root.left = TreeNode(2)
print c.hasPathSum(root,1)==False

