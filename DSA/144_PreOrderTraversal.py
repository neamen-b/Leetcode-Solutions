
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val:str, left_child = None, right_child = None) -> None:
        self.val = val
        self.left_child = left_child
        self.right_child = right_child



class Solution:

    def PreOrderTraversal(self, root: Optional[TreeNode]) -> List[TreeNode]:

        def Helper(root: TreeNode, list_of_nodes: List[int]) -> None:

            if root is not None:
                print(f"Node Val: {root.val}")
                list_of_nodes.append(root.val)
                Helper(root.left_child, list_of_nodes)
                Helper(root.right_child, list_of_nodes)
            else: 
                print('None')

        list_of_nodes = []
        Helper(root,list_of_nodes)
        return list_of_nodes
        

A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')


A.left_child = B
A.right_child = C
B.left_child = D
B.right_child = E
E.right_child = F
C.left_child = G

# Preorder traversal with  
sol = Solution()
sol.PreOrderTraversal(A)
        
            

