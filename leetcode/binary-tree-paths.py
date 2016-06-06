# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.path=[]
    def buildPath(self,node,path):
        if node == None:
            return
        if path=='':
            t=str(node.val)
        else:
            t= ''.join([path,"->", str(node.val)])
        if node.left==None and node.right==None:
            self.path.append(t)
        if node.left!=None:
            self.buildPath(node.left,t)
        if node.right!=None:
            self.buildPath(node.right,t)
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.buildPath(root,"")
        return self.path
    



c = Solution()

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(5)
print c.binaryTreePaths(t)
