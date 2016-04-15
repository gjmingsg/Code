# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        stack = [root]
        level = 0
        if root==None:
            return level
        while len(stack)>0:
            tstack = []
            level = level + 1
            while len(stack)>0:
                t= stack[0]
                if t==None:
                    break
                if t.left==None and t.right==None:
                    return level
                if t.left!=None:
                    tstack.append(t.left)
                if t.right!=None:
                    tstack.append(t.right)
                del stack[0]
            stack = tstack
        return level
        
            
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

print c.minDepth(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
print c.minDepth(root)==2

a = None
print c.minDepth(a)==0

root = TreeNode(1)
print c.minDepth(root)==1
