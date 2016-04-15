# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.numlist = []
        self.target = 0
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.target = sum
        self.getNum(root,0,[])
        return self.numlist
    def getNum(self,node,num,al):
        if node==None:
            return
        num = num + node.val
        al.append(node.val)
        if (node.left==None and node.right==None):
            if num==self.target:
                self.numlist.append(list(al))
        if node.left!=None:
            self.getNum(node.left,num,al)
            al.pop()
        if node.right != None:
            self.getNum(node.right,num,al)
            al.pop()
c = Solution()


root = TreeNode(5)
left1 = TreeNode(4)
right1 = TreeNode(8)
root.left= left1
root.right = right1
left21 = TreeNode(11)
right21 = TreeNode(13)
right22 = TreeNode(4)
left1.left = left21
right1.left = right21
right1.right = right22
left21.left = TreeNode(7)
left21.right = TreeNode(2)
right22.left =TreeNode(5)
right22.right =TreeNode(1)
print c.pathSum(root,22)
