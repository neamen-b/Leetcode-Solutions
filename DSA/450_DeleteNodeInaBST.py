'''
Initial thoiughs
    DFS guided guided by val
'''

from typing import List, Optional
class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def createBST(sorted_array: List[TreeNode]) -> TreeNode:

    if len(sorted_array) == 0:
        return None
    
    mid = (len(sorted_array) - 1) // 2

    root = TreeNode(sorted_array[mid])
    root.left = createBST(sorted_array[:mid])
    root.right = createBST(sorted_array[mid + 1 : ])

    # print(root.val)
    return root

root = createBST([4,5,7,9])
# print(root.left.val, root.val, root.right.val)

def deleteNode(root: TreeNode, key: int) -> TreeNode:

    if root is None:
        return None
    if root.left is None and root.right and root.val == key:
        return None

    def recurse(node, key, parent, child):
        if node is None:
            return None

        # print(node.val)
        if node.val == key:
        
            if node.right:
                replacement = node.right
            elif node.right is None and node.left is not None:
                replacement = node.left
            elif node.right is None and node.left is None:
                replacement = None
            else:
                pass
                
            if replacement and parent:
                if child == 0:
                    parent.left = replacement
                else:
                    parent.right = replacement
            # if the replacement node has a subtree under it. these changes have to trickle down
                replacement.left = node.left
            
            return replacement
        
        if node.val > key:
            recurse(node.left, key, node, 0)
        else:
            recurse(node.right, key, node, 1)
        return node
    recurse(root, key, None, 0)
new_root = deleteNode(root, 5)

print(new_root)
