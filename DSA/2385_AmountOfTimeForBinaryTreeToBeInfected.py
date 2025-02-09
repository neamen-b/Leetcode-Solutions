'''
initial thoughts

gotta covnvert the tree to a graph because start point is not guarranted to be root. 
I won't be able to traverse freely if my movement is limited to just my children


how to convert?
    traverse the tree:
     for each node, if children and it's parent (if not root) are its neighbours

     before call the recursive funciton, set child neighbout to parent then call. 


     after this, 

     bfs/dfs from the start point and find the max depth from this node. 
'''
# Now perform Bfs from starts point
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

A = TreeNode(1, TreeNode(3), TreeNode(7, TreeNode(6), TreeNode(5)))

def InfectionTime(root):

    # If the root is only node, then it is the only start point, therefore infection time = 0
    if not root.left and not root.right:
        return 0
    
    # node to list of neightbours
    graph = {}

    # This makes my graph
    def postOrder(node, parent):
        if node is None:
            return None
        
        left = postOrder(node.left, node)
        right = postOrder(node.right, node)

        node_neighbours = []
        if left:
            node_neighbours.append(left.val)
        if right:
            node_neighbours.append(right.val)
        if parent:
            node_neighbours.append(parent.val)
        graph[node.val] = node_neighbours
        return node
    
    postOrder(root, None)
    


    def BFS(start):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)
        max_count = float('-inf')
        while queue:
            curr, count = queue.popleft()
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append((neighbour, count + 1))
                    visited.add(neighbour)
            # count -= len(graph[curr])
            # count += 1
            if count > max_count: max_count = count
            print(f"node {curr} count {count}")
        return max_count
    return BFS(root.val)

print(InfectionTime(A))