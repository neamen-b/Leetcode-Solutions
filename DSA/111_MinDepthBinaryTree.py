# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.depth = -1

from typing import Optional

class Solution:
    # Given a root, returns the shortest depth from root to leaf node
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # return 0 because we are at leaf of subtree/tree
        if root is None:
            return 0
        # Troubleshooting
        print(f"cuurent root {root.val}")
        
        # With the maxdepth solution, we did not None children did not affect the max depth
        # With minDepth, None children cannot be counted towards the mind depth because they will always return zero
        # which is less that the other child's depth
        # This goes back up the whole tree and a min_depth 7 tree will just say 1
        # all would be 1 + min (0, some_depth) and zero is chosen
        # So this program considers only non-None subtrees/nodes
        if root.left is None or root.right is None:
            # Troubleshooting
            print(root.val)
            print(f"root's left {root.left}, root's right {root.right}")
            return 1 + self.minDepth(root.left if root.left else root.right)

        else:
            left_depth = self.minDepth(root.left) #print(f"{root.val}'s left {root.left.val}") ; print(f"{root.val}'s left {root.right.val}")
            right_depth = self.minDepth(root.right)
            #Troubleshooting
            print(f"{root.val}'s left_depth = {left_depth}, right_depth = {right_depth}")

            root.depth = 1 + min(left_depth, right_depth)
            return 1 + min(left_depth, right_depth)
A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')

Nodes  = [A, B, C, D, E, F, G]

# Tree = [A, B, C, D, E, G, None, None, None, None, F, None, None, None, None]
A.left = B
A.right = C
B.left = D
B.right = E
E.right = F
C.left = G

# Tree 
# A.right = B
# B.right = C
# C.right = D
# D.right = E
# E.right = F
# F.right = G
# Postorder traversal with  
sol = Solution()
# print(A.left, A.right)
print(sol.minDepth(A))

# Displays the nodes' min depth
# for node in Nodes:
#     print(f"Node-> {node.val}, {node.depth}")