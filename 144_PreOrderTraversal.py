
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left_child = None, right_child = None) -> None:
        self.val = val
        self.left_child = left_child
        self.right_child = right_child



class Solution:

    def PreOrderTraversal(self, root: Optional[TreeNode]) -> List[TreeNode]:

        def Helper(root: TreeNode, list_of_nodes: List[int]) -> None:

            if root is not None:
                list_of_nodes.append(root.val)
                Helper(root.left_child, list_of_nodes)
                Helper(root.right_child, list_of_nodes)

        list_of_nodes = []
        Helper(root,list_of_nodes)
        return list_of_nodes
        


        
        
            

