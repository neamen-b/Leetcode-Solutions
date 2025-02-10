'''
initial thoughts

    dfs the tree, at each root sum (left height, right height) and check if that is > max
    if so, set max to 

    in the end retuen max - 1


    Does not work because 


    Approach #2

    how about turning the tree into graph. 
    after turning into a graph, dfs from each node to find the longest path?

    But dfs for tree with n nodes is n
    dfs n times means time = O(n^2)
    Pretty slow

    but since the n is not too big, worst case 10^8
    Number of nodes in is 10^4 

    Can probably imporove this by dfsing from only leaf nodes as the longest path is bound to include leaf nodes. 
    Alas lets go for it and fail

    IT WORKS! BUT IT IS TOO SLOW
    lET'S TRY DOING JUST THE LEAF NODES
    It improved but still way too slow! way too slow!


    Approach #3 

    Very simple but I somehow overlooked this

    Do your typical DFS, at each node get the max depth of it left and subtree
    add them, if they greate than what you have seen so far, then it the max
    O(n)

'''
class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right


A = TreeNode(1, TreeNode(3), TreeNode(7, TreeNode(6), TreeNode(5)))

# FUCKKKKKKK!!!!!!! thORFOJASDNG[LJSARNG[ON'LASKDJ 'wlaekn'WL   ]]
def DiameterOfBT(root):
    max_d = float("-inf")
    def dfs(node):
        nonlocal max_d
        if node is None: return 0 

        # print(node.val)
        left = 1 + dfs(node.left)
        right = 1 + dfs(node.right)

        if sum([left, right]) > max_d:
            max_d = sum([left, right])
        
        return max(left, right)
    dfs(root)
    return max_d - 1
# print(DiameterOfBT(A))



def diameter(root):

    depths = []
    sum = 0
    def dfs(node):
        nonlocal sum

        if node is None:
            depths.append(sum)
            return 0
        print(f"sum {sum} at {node.val}")
        sum += 1
        dfs(node.left)
        dfs(node.right)
        sum -= 1
    dfs(root)
    print(f"dpehts {depths}")
    f_max = max(depths)
    depths.remove(f_max)
    s_max = max(depths)
    print(f_max , s_max)
    return f_max + s_max - 1 - 1

# print(diameter(A))



# Approach 2

def diameterofBT(root):
    # empty tree or only root, return 0 (as there are not edges)
    if root is None or (not root.left and not root.right):
        return 0
    
    graph = {}
    leaf_nodes = []
    def builgraph(node) -> None:
        # performing dfs iteratively.
        # stack (node, parent)
        stack = [(node, None)]

        while stack:
            curr, parent = stack.pop()
            neighbours = []

            if curr.right: 
                stack.append((curr.right, curr))
                neighbours.append(curr.right)
            if curr.left: 
                stack.append((curr.left, curr))
                neighbours.append(curr.left)
            if parent:
                neighbours.append(parent)

            # ASSUMING THAT THE LONGEST PATH WITLL ALWAYS INVOLVE A LEAF NODE. tRYING TO REDUC DFS START NODES
            if not curr.right and not curr.left:
                leaf_nodes.append(curr)
        
            graph[curr] = neighbours

    
    builgraph(root)
    # Checking graph
    # for key, value in graph.items():
    #     for n in value:
    #         print(key.val)
    #         print(n.val)
    #         print("-----------")

    def dfs(node):
        visited = set()
        stack = [(node, 0)]
        max_d = float("-inf")
        while stack:
            curr, count = stack.pop()
            visited.add(curr)
            max_d = max(max_d, count)

            for neighbour in graph[curr]:
                if neighbour not in visited:
                    stack.append((neighbour, count + 1))
        return max_d

    max_d = float("-inf")
    for key in leaf_nodes:
        max_d = max(max_d, dfs(key))

    return max_d
# print(diameterofBT(A))
    


# Approach #3

def dia(root):
    if root is None or (not root.left and not root.right):
        return 0
    

    max_d = float("-inf")

    def dfs(node):
        nonlocal max_d
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        max_d = max(max_d, left + right)

        return 1 + max(left, right)
    dfs(root)
    return max_d

print(dia(A))