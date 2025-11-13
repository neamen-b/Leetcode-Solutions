'''
Initial thought was to recusively check if a node and it's children were the same value
    then do logic comparision and buildup from bottom to up . but implementing it beat me
    so I went the easy way



    Method 2:

    traverse the tree in any order, I chose to traverse in pre-order. 
    add the value of each node to a set
    in the end, if the set's size is greater than one then the tree is not univalued

    O(n) - time as each node is visited
    O(n) - space (worst case) if all the node values are different
         - call stack is logn for balanced tree but o(n) for skewed for o(n) in total
'''


# methods 2. Wroks fine
def isUniValTree(root):
    node_vals = set()
    def dfs(node):
        if node is None: return None

        node_vals.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    return True if len(node_vals) == 1 else False


# build up from bottom. evalute bools as recursion unwinds
# I give yo for now
def isUnivalTree2(root):

    # leaf empty tree/subtree is univalues
    if root is None: return True

    left_sub = isUnivalTree2(root.left)
    right_sub = isUnivalTree2(root.right)
    
    if root.left and root.left.val == root.val:
        return True
    
    if root.right and root.right.val == root.val:
        return True

