# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        stack=[root]
        last = root
        while len(stack)>0:
            item = stack.pop()
            if item!=None:
                stack.append(item.right)
                stack.append(item.left)
                if item!=root:
                    last.left = None
                    last.right = item
                    last = item
                    #print item.val
        return root

    def show(self,root,st):
        item = root
        s = ''
        while item!=None:
            s = s + st % (item.val)
            item = item.right
        print s
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
c.flatten(root)
c.show(root,'%d ->')

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
c.flatten(root)
c.show(root,'%s ->')



root = TreeNode(1)
root.right = TreeNode(2)
c.flatten(root)
c.show(root,'%d ->')
