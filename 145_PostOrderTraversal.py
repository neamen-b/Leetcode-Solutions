# Definition for a binary tree node.

from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = [root]
        result_values = []

        while queue:
            off_the_queue = queue.pop()
            #print(f"Root after pop {off_the_queue.val}")
            result_values.append(off_the_queue.val)

            if off_the_queue.left is not None:
                queue.append(off_the_queue.left)

            if off_the_queue.right is not None:
                queue.append(off_the_queue.right)

           # print(list(map(lambda node: node.val,queue)))

        result_values.reverse()
        return result_values


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.right = b
b.left = c

print(Solution.postorderTraversal(a))

        