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
        self.numlist = []
    def sumNumbers(self, root):
        self.getNum(root,0)
        sumVal = 0
        print self.numlist
        for i in self.numlist:
            sumVal = sumVal + i
        return sumVal
        
    def getNum(self,node,num):
        if node==None:
            return
        num = num * 10 +node.val
        if (node.left==None and node.right==None):
            self.numlist.append(num)
        if node.left!=None:
            self.getNum(node.left,num)
        if node.right != None:
            self.getNum(node.right,num)
            
c = Solution()


root = TreeNode(0)
left = TreeNode(1)
right = TreeNode(3)
root.left= left
root.right = right
print c.sumNumbers(root)
