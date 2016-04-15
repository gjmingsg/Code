# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = [root]
        stack_v = {}
        al =[]
        while len(stack)>0:
            top = stack[len(stack)-1]
            if top!=None:
                if (top.left==None and top.right==None) or (stack_v.has_key(top) and stack_v[top]==1):
                    al.append(top.val)
                    stack.pop()
                    stack_v[top]=0
                    if top.right!=None:
                        stack.append(top.right)
                else:
                    if top.left!=None:
                        stack.append(top.left)
                stack_v[top]=1
            else:
                stack.pop()
        return al       


c = Solution()
root = TreeNode(5)
left1 = TreeNode(4)
right1 = TreeNode(8)
root.left= left1
root.right = right1
left21 = TreeNode(3)
right21 = TreeNode(7)
right22 = TreeNode(13)
left1.left = left21
right1.left = right21
right1.right = right22
left21.left = TreeNode(1)
left21.right = TreeNode(3)
right22.left =TreeNode(12)
right22.right =TreeNode(15)
print c.inorderTraversal(root)

root = TreeNode('-')
left1 = TreeNode('+')
right1 = TreeNode('/')
root.left= left1
root.right = right1
left21 = TreeNode('a')
left22 = TreeNode('*')
left1.left = left21
left1.right = left22
left31 = TreeNode('b')
left32 = TreeNode('-')
left22.left = left31
left22.right = left32
left32.left = TreeNode('c')
left32.right = TreeNode('d')
right1.left = TreeNode('e')
right1.right = TreeNode('f')
print c.inorderTraversal(root)

root = TreeNode(1)
root.right = TreeNode(2)
print c.inorderTraversal(root)
