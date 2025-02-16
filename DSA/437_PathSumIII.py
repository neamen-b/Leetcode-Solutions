'''
Initial thoughts

    For each node in the tree, preform a DFS to find all the paths from that node that can sum \
    up to targetsum. 

    * Cannot stop when sum  > targetsum because there are nodes with negatives values that could bring
        sum back down. 

    
    first write a funtion that performs a pre-order traversal. 
    for each node, call a helper DFS function that goes down each path, while adding up the values
    if you find a path that already adds up to tgsum, increment count, but keep going because there might be other
    nodes in that path that can add up to tgsum. UNtil you hit the leaf node

'''

def pathSum(root, targetsum):

    if root is None:
        return 0 if root.val != targetsum else 1
    
    def inorder(node):
        if node is None:
            return
        
        dfs(node, 0, 0)
        inorder(node.left)
        inorder(node.right)
    
    def dfs(curr, count, sum):
        if curr is None:
            return
        sum += curr.val
        print(count)
        if sum == targetsum:
            count += 1
        dfs(curr.left, count, sum)
        dfs(curr.right, count, sum)
    
    inorder(root)
        
# Just count the number of times sum == targetsum and return that sum
# Not going to work


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

A = TreeNode(1, TreeNode(3), TreeNode(7, TreeNode(6), TreeNode(5)))

def dfs(root,sum, target_sum, counter):
    if root is None:
        return 0
    
    sum += root.val

    if sum == target_sum:
        counter += 1
    
    return counter + dfs(root.left, sum, target_sum, 0) + dfs(root.right, sum, target_sum, 0)

arr = []
def pathsumIII(root, arr):
     
    if root is None:
        return None
    arr.append(dfs(root, sum = 0, target_sum = 13, counter= 0))
    # print(counter)
    pathsumIII(root.left, arr)
    pathsumIII(root.right, arr)

print(pathsumIII(A, arr))
print(sum(arr))



