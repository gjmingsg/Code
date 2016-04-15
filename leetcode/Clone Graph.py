# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.visited ={}
       
    def cloneGraph(self, node):
        if node == None:
            return node
        t = UndirectedGraphNode(node.label)
        self.visited[node]= t
        for item in node.neighbors:
            if item in self.visited:
                t.neighbors.append(self.visited[item])
            else:
                t.neighbors.append(self.cloneGraph(item))
        return t
    
    def show(self,node):
        #print node.label
        s = ""
        s = s + "%d[" % node.label
        self.visited[node]=1
        for item in node.neighbors:
            if item in self.visited:
                s = s + "%d," % item.label
            else:
                #print item.label
                s = s + "%d," % item.label
                self.show(item)
        s += "]"
        print s
        return t

g = UndirectedGraphNode(0)
g.neighbors.append(UndirectedGraphNode(1))
g.neighbors.append(UndirectedGraphNode(2))
g.neighbors[0].neighbors.append(g.neighbors[1])
g.neighbors[1].neighbors.append(g.neighbors[1])
c = Solution()
t = c.cloneGraph(g)

c.show(t)

g = UndirectedGraphNode(0)
g.neighbors.append(UndirectedGraphNode(0))
g.neighbors.append(UndirectedGraphNode(0))

t = c.cloneGraph(g)

c.show(t)

