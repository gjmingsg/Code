# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.lst=[]    
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        
        if root==None:
             return True
        return self.preOrder(root)
        #print self.lst
    def preOrder(self,node):
        if node!=None:
           flag = self.preOrder(node.left)
           self.lst.append(node.val)
           l = len(self.lst)
           if l>1 and self.lst[l-1] <= self.lst[l-2]:
               return False
           flag &= self.preOrder(node.right)
           return flag
        else:
            return True
    #{10,5,15,#,#,6,20}
        
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
print c.isSymmetric(root)
