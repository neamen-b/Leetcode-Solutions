'''
Initial thoughts

    DFS and aadd each leaf node to a list
    compare lists

    Time O(n)
    space O(n + m)

    can this be done in O(1) space?

    Here's an idea

    while dfsing, 
        when you a hit a leaf node. return node.val as string and add it up as you go

        comapre two strings Time (O(min(n,m))), space O(number of leaf nodes)
'''

from typing import Optional
# list comaprison approach
def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        t = []

        def dfs (node):
            if node is None:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left is None and right is None:
                t.append(node.val)
            return node
        
        dfs(root1)
        t1 = t[:]
        t.clear()
        dfs(root2)
        
        if len(t1) != len(t):
            return False
        i = 0
        while i < len(t1):
            if t1[i] != t[i]:
                return False
            i += 1
        return True


# strings

def leafsimilar (root1, root2):
     
     def dfs(node):
        if node is None:
            return None

        left = dfs(node.left)
        right = dfs(node.right)

        ret = ""
        if left is None and right is None:
            ret = str(node.val)

        return "" + ret 

        