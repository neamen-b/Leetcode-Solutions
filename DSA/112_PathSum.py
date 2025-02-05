# Thoughts on how to solve it
'''
First thing that came to mind is DFS and check sum against the targetsum
1. Conditions
    a. If root is none : return False // No value
    b. Root.val and targest sum can be negative // So you can't stop halfway if sum is greater than targetsum
    c. 

'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # No sum is Tree is empty
        if root is None:
            return 0
        
        if root.left is None or root.right is None:
            print(f'leaf {root.val}')
            return 0
        else:
            # print(root.left.val)
            left_sum = self.hasPathSum(root.left, targetSum)
            right_sum = self.hasPathSum(root.right, targetSum)

            print(root.val, left_sum, right_sum)
            return root.val + left_sum, root.val + right_sum
        

    def PathSum_DFS (self, root : Optional[TreeNode], targetsum: int) -> bool:

        # Collects each root to leaf path's sum
        set_of_sums = set()

        # If tree is empty, return False
        if root is None:
            return False
        
        # DFS traversal iteratively requires a stack
        # Left -> right movement
        # Looks like preorder
        # It holds a tuple of the root node of the current subtree and its sum up until that point
        tree_stack = [(root, root.val)]

        # While stack is not empty
        # Stack is used to traverse tree Depth first
        while tree_stack:
            # Troubleshooting
            # print(f"----------")
            # for node in tree_stack:
            #     print(node.val)

            # Tuple of current node and the sum of nodes upto and including it
            current_node = tree_stack.pop()
            # print(f"Current node -> {current_node.val}")

            # If both children are None, we are at a leaf node
            # Sum is final for that particular root -> leaf path
            # 
            if current_node[0].left is None and current_node[0].right is None:
                # sum += current_node[0].val + current_node[1]
                # Below line stores path sum and leaf node
                #set_of_sums.add((current_node[1], current_node[0].val))

                # Below stores sum at leaf node
                set_of_sums.add(current_node[1])
                # print(f"Sum at {current_node[0].val} is {sum}")
                # sum -= current_node[0].val


            # If right child is not None
            # Add right child valule to path sum and push to stack the updated sum and right child
            if current_node[0].right:
                tree_stack.append((current_node[0].right, current_node[0].right.val + current_node[1]))

            # If left child is None
            # Add left child value to path sum and push to stack with updated path sum and left child
            if current_node[0].left:
                tree_stack.append((current_node[0].left, current_node[0].left.val + current_node[1]))

            # Broken code - Mismanages the summing 
            # elif current_node[0].left is None or current_node[0].right is None:
            #         sum = current_node[0].val + current_node[1]
            #         tree_stack.append((current_node[0].left if current_node[0].left else current_node[0].right,
            #                            current_node[0].left.val if current_node[0].left.val else current_node[0].right.val + current_node[1]))   
            # else:
            #     # print()
            print(f"Node: {current_node[0].val}, sum: {current_node[1]}")
            #     # sum = current_node[0].val + current_node[1]

        print(f"list_of_sums -> {set_of_sums}")

        return targetsum in set_of_sums




A = TreeNode(val=1)
B = TreeNode(val=-2)
C = TreeNode(val=-3)
D = TreeNode(val=1)
E = TreeNode(val=3)
F = TreeNode(val=-2)
G = TreeNode(val=-1)

A.left = B ; A.right = C ; B.left = D ; B.right = E ; C.left = F ; D.left = G

sol = Solution()
print(sol.PathSum_DFS(A, 3))