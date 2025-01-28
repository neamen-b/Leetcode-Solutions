# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
from typing import Optional 
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inOrder(root: Optional[TreeNode], array: List[int]) -> None:

            if root is not None:
                inOrder(root.left, array)
                array.append(root.val)
                inOrder(root.right, array)

        array = []
        inOrder(root,array)
        return array

order = []

def traverse(root: Optional[TreeNode])->None:

    if root is None:
        return None
    
    if root:
        traverse(root.left)

    order.append(root)

    if root:
        traverse(root.right)

