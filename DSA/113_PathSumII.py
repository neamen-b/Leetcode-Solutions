'''
DFS

Keep track of paths.

Id they add up to target, add path to answer
'''
class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
         self.val = val if val else None
         self.left = left if left else None
         self.right = right if right else None


    # def __repr__(self):
    #      print(f"TreeNoe (val={self.val}, left={self.left}, right={self.right})")

A = TreeNode(val = 1, left = TreeNode(2), right = TreeNode(4) )
# A = TreeNode(val = 1)

def PathSum(root, targetSum):

    ans = []
    path = []


    def DFS(node, sum, path):
        # global path
        if node is None:
            return
        
        sum += node.val
        path.append(node.val)
        print(node.val, sum, path, ans)

        if node.left is None and node.right is None:
            if sum == targetSum:
                print(f"sum equal tag but path is {path}")
                ans.append(path[:])
                # path.clear()
                # print('update')
                # sum = 0
        DFS(node.left, sum, path)
        DFS(node.right, sum, path)
        sum -= node.val
        path.pop()

    DFS(root, 0, [])
    print(ans)
    return ans

print(PathSum(A, 3))



        
