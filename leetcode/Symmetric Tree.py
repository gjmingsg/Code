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
    def isSymmetric(self, root):
        if root==None:
             return True
        self.preOrder(root,'m')
        l = len(self.lst)
        print self.lst
        for i in range(0,l/2):
            if self.lst[i][1:]!=self.lst[l-1-i][1:] or self.lst[i][0]==self.lst[l-1-i][0]:
                return False
        return True
        #print self.lst
    def preOrder(self,node,dirc):
        if node!=None:
           self.preOrder(node.left,'l')
           self.lst.append(dirc+str(node.val))
           self.preOrder(node.right,'r')
        
    #{1,2,3,3,#,2,#}
        
c = Solution()
root = TreeNode(1)
left1 = TreeNode(2)
right1 = TreeNode(3)
root.left= left1
root.right = right1
left1.left = TreeNode(3)
right1.left=TreeNode(2)

print c.isSymmetric(root)

root = TreeNode(1)
left1 = TreeNode(2)
right1 = TreeNode(2)
root.left= left1
root.right = right1

print c.isSymmetric(root)
