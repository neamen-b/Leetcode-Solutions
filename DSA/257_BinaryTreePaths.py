class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
         self.val = val if val else None
         self.left = left if left else None
         self.right = right if right else None


    # def __repr__(self):
    #      print(f"TreeNoe (val={self.val}, left={self.left}, right={self.right})")

A = TreeNode(val = 1, left = TreeNode(2), right = TreeNode(3) )
# A = TreeNode(val = 1)

from typing import Optional , List

def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        # path = ""

        def traverse(origin, path):
            print(origin)
            print("path", path)
            if origin is None:
                return
            

            if origin.left is None and origin.right is None:
                path += f"{origin.val}"
                ans.append(path)
                path = ""
            else:
                path += f"{origin.val}->"

            traverse(origin.left, path)
            traverse(origin.right, path)
        traverse(root, "")

        # for i in range(len(ans)):
        #      ans[i] = ans[i][:len(ans[i])-2]
        
        final_ans = set(ans)
        return ans

print(binaryTreePaths(A))