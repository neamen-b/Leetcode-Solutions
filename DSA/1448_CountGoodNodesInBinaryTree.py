'''
keep track of max_val down that path
    if node is >= max_val
        increase count byone
    
    see if node.val is > max_val
        if so, update max-val
    
        call left and right child with max
    return count

    I was worried how the program would use the correct max_Val when going to the right
    But the right subtree is already called with the correct max_val before goinf deeper
        and potentially changing max_val
    
        so when the recursion unwinds the call stack get back to the right call, the max_val for that node is used
        correctly


    Time = O(n) 
    Space  = O(logn),  worst case O(n) - skeweed trree
'''

def goodNodes(root):

    count = 0

    def dfs(node, max_val):

        if node is None:
            return None
        
        if node.val >= max_val:
            count += 1
        
        max_val = max(max_val, node.val)

        dfs(root.left, max_val)
        dfs(root.right, max_val)

    return count