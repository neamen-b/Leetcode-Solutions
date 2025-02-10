'''
Initial thoughts

    going to do pre-ordere traversal of the binary tree. 

        The difference?
            depending on my depth (or label), I am going to make the recursive calls differntley

            if depth is odd. 
                calls
                left child 
                right chiles
            else:
                calls
                right child
                left child
            for each root, add to ans list

        O(n) time
        O(n) space
        Let's see if it works

        IT DOES NOT WORK AT ALL
    
        Approach #2 

        Create a tree using pre-order traversal, 
        when you create the node with the given label. Start a dfs from the root of the tree
        you created until you meet the label. Then return all the nodes traversed

        Problem?
        How do you create a tree following the label rules? Don't think this is possible
        Also time complexity, this an infinite tree so you might be building for a long time before performing DFS

        Won't work either

        Approach #3

        Mathematical

        For a normal binary tree, labeled following row-label rule, the parent of a node is node // 2
        finding the level of a node = floor(log2(node.val) + 1)
        find the range of values on a specific row [ 2^(level-1) , (2^level) - 1 ]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# A = TreeNode(1, TreeNode(3), TreeNode(7, TreeNode(6), TreeNode(5)))


import math
ans = []
def PathInZigzagTree(label):
    # ans.append(label)
    if label == 1:
        return ans.append(label)
    
    parent = label // 2
    label_level = math.floor(math.log2(label) + 1)
    parent_level = label_level - 1

    if parent_level % 2 == 0:
        parent_range = [x for x in range(int(math.pow(2, parent_level) - 1), int(math.pow(2, parent_level -1) - 1), -1)]
    else:
        parent_range = [x for x in range(int(math.pow(2, parent_level - 1)), int(math.pow(2, parent_level)))]
    
    true_parent = abs(parent_range[0] + parent_range[-1] - parent)
    print(f"label = {label}, label_level= {label_level}, parent range = {parent_range}, true_parent= {true_parent}")
    ans.append(label)
    PathInZigzagTree(true_parent)


print(PathInZigzagTree(14)) 
print(ans[::-1])
# parent_level = 3
# for x in range(int(math.pow(2, parent_level) - 1), int(math.pow(2, parent_level - 1)) -1, -1):
#     print(x)



# This traversal does not work.   
class Solution:
    ans = []

    def traverse(self, root, label):
        if root is None:
            return None
        
        self.ans.append(root.val)

        if label % 2 == 0:
            self.traverse(root.right, label + 1)
            self.traverse(root.left, label + 1)
        else:
            self.traverse(root.left, label + 1)
            self.traverse(root.right, label + 1)

        return root

    def pathZigzag(self, label):
        self.traverse(A, label)
        return self.ans
# sol = Solution()
# print(sol.pathZigzag(2))

