'''
dfs and find node.val == val
    assing subtree head as node

    When traversing, go in the direction where vsl will be
        if val > node.val, go right
        if val < node.val, go left

        This works since this is a BST. 

    Time O(logn)
    Space O(logn)
'''

def searchBST(root,  val: int):
        sub = None

        def dfs(node, val):
            nonlocal sub
            if node is None:
                return None
            
            if node.val == val:
                sub = node
            # go to left subtree to find something smaller
            if node.val > val:
                dfs(node.left, val)
            # go to right subtree to find something bigger
            else:
                dfs(node.right, val)
        dfs(root, val)

        return sub