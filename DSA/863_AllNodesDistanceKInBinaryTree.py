'''
Initial thoughts.

    step 1
    conver the BT into a graph so that traversal is not limited by BT's directedness

        do dfs
            for each node:
                node_neightbours.appedn([ parent if nay, node.left, node.right])
        
    step 2
    perform bfs from target node

    while performing dfs, if depth count reaches k, then add that node to the answer list


    all the values are guaranteed to be unique so I don't have to worry about my bfs not working
    becuase I will be using a set to keep track of visited nodes
'''

from collections import deque
class Solution:

    graph = {}

    def buildgraph(self, root, parent):

        if root is None:
            return None
        
        neighbours = []

        if parent:
            neighbours.append(parent.val)
        if root.left:
            neighbours.append(root.left.val)
        if root.right:
            neighbours.append(root.right.val)
        
        self.graph[root.val] = neighbours
        self.buildgraph(root.left, root)
        self.buildgraph(root.right, root)

        return root
    
    def bfs(self, target, k):
        visited = set()
        # bfs start point and the count from itself
        queue = deque([(target, 0)])
        ans = []

        while queue:
            # unpacks the tuples
            curr, count = queue.popleft()
            visited.add(curr)

            # If at a distance of k from target, add it to ans list
            if count == k: ans.append(curr)

            for neighbour in self.graph[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    # increase the distance from start by one
                    queue.append((curr, count + 1))
        return ans
    
    def distanceK(self, root, target, k):
        self.buildgraph(root)
        return self.bfs(target, k)


