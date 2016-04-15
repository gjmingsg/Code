# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.h={}
    # @param root, a tree node
    # @return an integer
    def isBalanced(self, root):
        if root==None:
            return True
        #return self.isDiff(root)
        return self.isOk(root)!=-1
        
    def isDiff(self,node):
        if node != None:
            #print "ln=%d rn=%d" % (self.height(node.left),self.height(node.right))
            if abs(self.height(node.left) - self.height(node.right))>1:
                return False
            else:
                return self.isDiff(node.left) and self.isDiff(node.right)
        return True
    
    def height(self,node):
        if node==None:
            return 0
        elif self.h.has_key(node):
            return self.h[node]
        else:
            self.h[node]=max(self.height(node.left)+1,self.height(node.right)+1)
            return self.h[node]


    # it is better method            
    def isOk(self,node):
        if node==None:
            return 0
        else:
            ld = self.isOk(node.left)
            rd = self.isOk(node.right)
            if ld==-1 or rd==-1 or abs(ld-rd)>1:
                return -1
            return 1+ max(ld,rd)
        
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

print c.isBalanced(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
print c.isBalanced(root)==True

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
print c.isBalanced(root)==False

a = None
print c.isBalanced(a)==True

root = TreeNode(1)
print c.isBalanced(root)==True


