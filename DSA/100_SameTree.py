from typing import Optional 
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def isSameTree2(p:Optional[TreeNode], q:Optional[TreeNode])-> bool:

        #If both roots None -> True
        #If one root None and other not -> False
        # If node.val is not the same as node2.val at the same level -> False
        # return issame on node1 left & right AND issame on node2 left & right
        # Goes back up recursion tree with the logical comparison

        # Both Trees are the None in this case
        if p is None and q is None:
            return True
        
        # If either p or q are None, return False
        if p is None or q is None:
            return False
        
        # If the values are different at the same recursive step, return False
        if p.val != q.val:
            return False
        
        # Call issame on left and right subtree of both root/current nodes
        # THis is comparing the remaining subtrees as another pair of tree with roots at the left and right
        # childs of p and q
        return Solution.isSameTree2(p.left,q.left) and Solution.isSameTree2(p.right, q.right)

















    # Scraped
    # DOES NOT WORK 
    # NOT ROBUST ENOUGH
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Logic
        # Traversal should result in the same array of values - answers same value question
        def isOrderTraversal (root: Optional[TreeNode]) -> List[TreeNode]:
            if root is None:
                return []

            stack = []
            traversed_list = []
            current = root

            # Traverse
            while current is not None or stack:

                # For each "root" node, go left most
                # Add to stack along the way
                # You get to the leaves with this
                while current is not None:
                    stack.append(current)
                    current = current.left

                # At the leaves, process them
                #and build back up Left/Root->Right
                # Because leaf is root and left

                if current is None: traversed_list.append(current)
                if current is None: traversed_list.append(current)

                current = stack.pop()
                traversed_list.append(current.val)
                current = current.right

            return traversed_list

        # Now traverse both trees with inorder and compare traversed_list
        p_traversal = isOrderTraversal(p)
        q_traversal = isOrderTraversal(q)
        print(p_traversal, q_traversal)

        return len(p_traversal) == len(q_traversal) and all(x == y for x,y in zip(p_traversal,q_traversal))
    

#[3,3]
a = TreeNode(3)
b = TreeNode(3)
a.left = b

#[1,None,1]
c = TreeNode(3)
d = TreeNode(3)
c.right = d

#print(f"[3,3]{a.val, a.left.val, a.right}, [3,None,3] {c.val,c.left,c.right.val}")
print(Solution.isSameTree2(a,c))


'''Poor me, this does not work because Trees can have the same inordertraversal list 
but have different structures. Solution: You have to compare each node while traversing.'''