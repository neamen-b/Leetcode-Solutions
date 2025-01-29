
'''
lEt's try this with recursion

    function regress(curr):

        if curr is none:
            return none
        
        curr.next = regress()
'''

class TreeNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

C = TreeNode(3)
B = TreeNode(2,C)
A = TreeNode(1,B)

old_head = A
val = None
new_head = TreeNode()

# Does not work
def recurse(head):
    print(f"Recursion call at {head.val}")
    if not head:
        return head
    
    val = recurse(head.next)

    # if val.val:
    #     print(f"return value at {val.val}")
    # else:
    #     print(f"return value at {val}")

    if val is not None:
        print("assigning",val.val)
        val.next = head
    if head == old_head:
        old_head.next = None
    return head
# recurse(A)
# print(C.next)
# print(B.next)
# print(A.next)


# This works
def reverse(curr):
    # Keep going until you hit tail, then go back 
    if curr is None:
        return curr
    
    # THe node this variable is assigned to is now going to point to the node that came 
    # before it. Provided it is not None
    returned_node = reverse(curr.next)

    if returned_node is not None:
        # At this point we are in previous node's function call so curr is the previous node
        returned_node.next = curr
    
    # When NOne is returned, the means that we are in the tail node's funciton call. 
    # and the tail becomes the new head. 
    # Interestingly, this varibale cannot be accessed for some bizzare reason even tho it is global
    # have to specifically access it with the modifier
    else:
        global new_head
        new_head = curr
    # This is supposed to make sure that the old head points to None
    if curr == old_head:
        old_head.next = None
    
    # Return the node with which the function was called. 
    return curr

reverse(A)
print(C)
print(B)    
print(A)

print(f"new head {new_head}")