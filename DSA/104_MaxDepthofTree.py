
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val:str, left_child = None, right_child = None) -> None:
        self.val = val
        self.left_child = left_child
        self.right_child = right_child



class Solution:

    def MaxDepth(self, root: Optional[TreeNode]) -> List[TreeNode]:
            
            if root is not None:
                # print(f"Node Val: {root.val}")
                left_depth = self.MaxDepth(root.left_child)
                right_depth = self.MaxDepth(root.right_child)
                # print(f"left_depth {left_depth}, right_depth {right_depth}")
                return 1 + max(left_depth, right_depth)
            else: 
                # print('None')
                return 0
        

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
# print(sol.MaxDepth(A))

sum, max = 0, float("-inf")
def traverse(root: Optional[TreeNode]):
     global sum, max
     sum+=1
     if root is None:
          sum-=1
          if sum > max:
               max = sum
          return
     
     traverse(root.left_child)
     print(root.val, sum)
     traverse(root.right_child)
     sum-=1

traverse(A)
print(max)
     
        
            

